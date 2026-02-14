# GOTM Technical Documentation
## General Ocean Turbulence Model

**Authors:**  
Karsten Bolding¹, Hans Burchard², Lars Umlauf², Jorn Bruggeman³

**Contributors:**  
Knut Klingbeil², Qing Li⁴, and many others worldwide

¹ Bolding & Bruggeman, Denmark  
² Leibniz Institute for Baltic Sea Research Warnemünde (IOW), Germany  
³ National Oceanography Centre, UK  
⁴ Los Alamos National Laboratory, USA

---

**Repository:** https://github.com/gotm-model/code  
**Development Branch:** `master` (actively developed, recommended)  
**Stable Releases:** Tagged versions (e.g., `v6.0.7`)  
**License:** GPL-2.0  
**Language:** Fortran (84.2%), C, CMake, Python  
**Latest Stable Release:** v6.0.7 (July 2024)  
**Official Website:** https://gotm.net

> **Important:** This documentation describes the `master` branch, which is the main development branch. Stable releases use version tags. For most applications and all test cases, use the `master` branch.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Governing Equations and One-Dimensional Simplification](#2-governing-equations-and-one-dimensional-simplification)
3. [Air-Sea Interaction and Surface Forcing](#3-air-sea-interaction-and-surface-forcing)
4. [Equation of State and TEOS-10](#4-equation-of-state-and-teos-10)
5. [Introduction to Turbulence Closure Models](#5-introduction-to-turbulence-closure-models)
6. [Numerical Methods](#6-numerical-methods)
7. [Architecture and Design](#7-architecture-and-design)
8. [Core Modules](#8-core-modules)
9. [Turbulence Closure Models in Detail](#9-turbulence-closure-models-in-detail)
10. [Build System and Dependencies](#10-build-system-and-dependencies)
11. [Configuration System](#11-configuration-system)
12. [File I/O System](#12-file-io-system)
13. [Optional Extensions](#13-optional-extensions)
14. [Installation and Compilation](#14-installation-and-compilation)
15. [Test Cases and Examples](#15-test-cases-and-examples)
16. [Publications](#16-publications)

---

## 1. Overview

### 1.1 What is GOTM?

GOTM (General Ocean Turbulence Model) is a one-dimensional water column model for marine and limnological applications. It simulates vertical transport of momentum, heat, salt, and tracers, coupled with state-of-the-art turbulence parameterizations. Since the mid-1990s, GOTM has become one of the most widely used turbulence models in aquatic science.

The model excels at:
- Process studies isolating vertical mixing physics
- Validation of turbulence closure schemes
- Rapid testing of scenarios and sensitivity analyses
- Biogeochemical modeling in stratified waters
- Providing turbulence schemes for 3D circulation models

### 1.2 Key Features

- **Comprehensive turbulence library**: From simple zero-equation models to sophisticated second-moment closures
- **Modular design**: Clean separation of physics (meanflow, turbulence, airsea, biogeochemistry)
- **Modern configuration**: YAML-based setup replacing legacy namelists
- **Flexible output**: Integrated flexout system with time-averaging and interpolation operators
- **Biogeochemical coupling**: Seamless [FABM](https://fabm.net) integration for ecosystem modeling
- **3D model integration**: Used in FVCOM, TELEMAC, GETM, NEMO, and others
- **Git submodules**: Clean dependency management (FABM, CVMix, flexout, STIM)

### 1.3 Primary State Variables

- Horizontal velocities: U(z,t), V(z,t)
- Temperature: T(z,t)
- Salinity: S(z,t)
- Turbulent kinetic energy: k(z,t)
- Dissipation rate or length scale: ε(z,t) or L(z,t)
- Optional tracers via FABM
- Optional ice properties via STIM (Simple Thermodynamic Ice Models)

Horizontal gradients must be prescribed, making GOTM ideal for one-dimensional process studies.

---

## 2. Governing Equations and One-Dimensional Simplification

### 2.1 Three-Dimensional Momentum Equations

The motion of oceanic and lake waters is governed by the incompressible Navier-Stokes equations. In their most general form, the momentum equations in Cartesian coordinates (x, y, z) are:

**Horizontal momentum (x-direction):**
```
∂u/∂t + u∂u/∂x + v∂u/∂y + w∂u/∂z - fv = -1/ρ₀ ∂p/∂x + ∂/∂z(ν ∂u/∂z) + Fₓ
```

**Horizontal momentum (y-direction):**
```
∂v/∂t + u∂v/∂x + v∂v/∂y + w∂v/∂z + fu = -1/ρ₀ ∂p/∂y + ∂/∂z(ν ∂v/∂z) + Fᵧ
```

**Hydrostatic balance (z-direction):**
```
∂p/∂z = -ρg
```

where:
- (u, v, w) = velocity components in (x, y, z) directions
- f = Coriolis parameter = 2Ω sin(φ), where Ω is Earth's rotation rate and φ is latitude
- ρ = density
- ρ₀ = reference density
- p = pressure
- ν = kinematic viscosity (molecular + turbulent)
- g = gravitational acceleration
- Fₓ, Fᵧ = additional forcing terms (e.g., horizontal diffusion, wave forces)

**Continuity equation (incompressibility):**
```
∂u/∂x + ∂v/∂y + ∂w/∂z = 0
```

### 2.2 Reynolds Decomposition and Averaging

In turbulent flows, we decompose each variable into mean and fluctuating components:
```
u = ū + u'
v = v̄ + v'
w = w̄ + w'
p = p̄ + p'
```

where overbar denotes time or ensemble average, and prime denotes turbulent fluctuations.

After Reynolds averaging, the momentum equations become:
```
∂ū/∂t + ū∂ū/∂x + v̄∂ū/∂y + w̄∂ū/∂z - fv̄ = -1/ρ₀ ∂p̄/∂x + ∂/∂z(ν ∂ū/∂z - ⟨u'w'⟩)
```

The term ⟨u'w'⟩ is the Reynolds stress (turbulent momentum flux), which must be parameterized through turbulence closure models.

### 2.3 One-Dimensional Simplification in GOTM

GOTM assumes **horizontal homogeneity**, meaning all horizontal gradients of mean quantities are either:
1. Prescribed from observations or theory
2. Neglected (set to zero)
3. Parameterized

This reduces the 3D equations to 1D (vertical) while retaining the essential physics of vertical mixing.

**Key assumptions:**
- ∂ū/∂x = ∂ū/∂y = 0 (horizontal velocity gradients prescribed or zero)
- ∂T̄/∂x = ∂T̄/∂y = 0 (horizontal temperature gradients prescribed)
- ∂S̄/∂x = ∂S̄/∂y = 0 (horizontal salinity gradients prescribed)
- w̄ can be computed diagnostically from prescribed vertical velocity or from continuity

**Resulting 1D momentum equations:**
```
∂ū/∂t - fv̄ = -1/ρ₀ ∂p̄ₓ/∂x + ∂/∂z(νₜ ∂ū/∂z) + Fₓ

∂v̄/∂t + fū = -1/ρ₀ ∂p̄ᵧ/∂y + ∂/∂z(νₜ ∂v̄/∂z) + Fᵧ
```

where:
- νₜ = eddy viscosity (from turbulence closure)
- ∂p̄ₓ/∂x, ∂p̄ᵧ/∂y = external (barotropic) + internal (baroclinic) pressure gradients
- Fₓ, Fᵧ = additional body forces

**Temperature and salinity equations:**
```
∂T̄/∂t = ∂/∂z(κₜ ∂T̄/∂z) + Q_heat

∂S̄/∂t = ∂/∂z(κₛ ∂S̄/∂z) + Q_salt
```

where:
- κₜ, κₛ = eddy diffusivities for heat and salt
- Q_heat = source terms (shortwave penetration, etc.)
- Q_salt = source terms (rarely used)

### 2.4 Pressure Gradient Treatment

GOTM handles pressure gradients through two components:

**External (barotropic) pressure gradient:**
- Associated with sea surface slope
- Can be prescribed from observations, tidal analysis, or wind setup
- Uniform with depth in absence of stratification

**Internal (baroclinic) pressure gradient:**
- Arises from horizontal density gradients
- Computed from prescribed horizontal density gradients:
  ```
  1/ρ₀ ∂p̄/∂x = g ∂η/∂x + g ∫ᶻ₋ₕ (1/ρ₀ ∂ρ/∂x) dz'
  ```
  where η is sea surface elevation and the integral represents baroclinic contribution

**Common configurations:**
1. **Coastal upwelling**: Prescribe along-shore wind → cross-shore Ekman transport → sea surface slope
2. **Estuaries**: Prescribe horizontal salinity gradient → baroclinic pressure gradient
3. **Open ocean**: Often neglect horizontal pressure gradients (wind-driven only)

### 2.5 Coordinate Systems

GOTM supports multiple vertical coordinate systems:

**Sigma coordinates (terrain-following):**
```
σ = (z - η)/(H + η)
```
where H is bottom depth and η is surface elevation. Ranges from σ = 0 (surface) to σ = -1 (bottom).

**Advantages:**
- Follows topography
- Equal resolution in surface and bottom boundary layers
- Natural for varying water depth

**Z-coordinates (geopotential):**
Fixed vertical levels independent of surface/bottom topography.

**Advantages:**
- No pressure gradient errors
- Simpler interpretation

**Adaptive coordinates:**
GOTM can use non-uniform grids with zooming (higher resolution) near surface/bottom:
- `ddu` = surface zooming parameter
- `ddl` = bottom zooming parameter

### 2.6 Why One-Dimensional Models?

Despite the simplifications, 1D models like GOTM are invaluable because:

1. **Physical insight**: Isolate vertical mixing processes from horizontal advection
2. **Validation**: Test turbulence closures against observations before implementing in 3D models
3. **Computational efficiency**: Run thousands of scenarios for sensitivity analysis
4. **Process studies**: Understand fundamental mechanisms (e.g., diurnal cycle, storm mixing, ice formation)
5. **3D model components**: GOTM's turbulence module is used in [GETM](https://getm.eu), [FVCOM](http://fvcom.smast.umassd.edu/), [TELEMAC](http://www.opentelemac.org/), and others
6. **Biogeochemical modeling**: Focus on vertical nutrient/light gradients without horizontal complexity

**Limitations:**
- Cannot simulate horizontal processes (fronts, eddies, lateral advection)
- Requires prescribed or parameterized horizontal gradients
- Not suitable for regions where horizontal dynamics dominate

---

## 3. Air-Sea Interaction and Surface Forcing

### 3.1 Overview of Air-Sea Fluxes

The ocean or lake surface is where the water column exchanges momentum, heat, and freshwater with the atmosphere. These exchanges fundamentally control:
- Mixed layer depth and temperature
- Evaporation and precipitation balance
- Storm-driven mixing and deepening
- Diurnal warming and nocturnal cooling
- Ice formation and melting

GOTM's **airsea module** (`src/airsea/`) computes surface boundary conditions for momentum, heat, and freshwater fluxes using bulk formulae based on atmospheric forcing data.

### 3.2 Momentum Flux (Wind Stress)

Wind blowing over the water surface transfers momentum, creating a **wind stress** that drives currents.

**Wind stress components:**
```
τₓ = ρₐᵢᵣ Cᴅ |U₁₀| u₁₀
τᵧ = ρₐᵢᵣ Cᴅ |U₁₀| v₁₀
```

where:
- τₓ, τᵧ = wind stress in x, y directions (N/m² or Pa)
- ρₐᵢᵣ = air density (~1.2 kg/m³)
- Cᴅ = drag coefficient (dimensionless, typically 0.001-0.003)
- U₁₀ = (u₁₀, v₁₀) = wind velocity at 10 m height
- |U₁₀| = wind speed = √(u₁₀² + v₁₀²)

**Drag coefficient parameterization:**

GOTM supports multiple formulations for stability-dependent drag coefficients:

**1. Fairall et al. (COARE 3.0/3.5)** - Recommended for ocean applications
- Accounts for wind speed dependency
- Atmospheric stability effects
- Wave age and sea state
- Most widely validated
- Reference: Fairall et al. (1996, 2003)
- Code: [COARE algorithm on GitHub](https://github.com/NOAA-PSL/COARE-algorithm)

**2. Kondo (1975)** - Alternative formulation
- Widely used in Asian/Pacific applications
- Different stability functions
- Simpler than COARE
- Reference: Kondo (1975)
- Paper: [Kondo (1975) on JMSJ](https://www.jstage.jst.go.jp/article/jmsj1965/53/1/53_1_1/_article)

Simple parameterization (Large & Pond, 1981):
```
Cᴅ = 0.0011,  for U₁₀ ≤ 10 m/s
Cᴅ = (0.49 + 0.065 U₁₀) × 10⁻³,  for U₁₀ > 10 m/s
```

**Configuration:**
```yaml
airsea:
  fluxes_method: 2  # 1=Kondo, 2=Fairall (COARE)
```

**Surface boundary condition:**
Wind stress appears as the upper boundary condition for momentum equations:
```
νₜ ∂ū/∂z|ᶻ⁼⁰ = τₓ/ρ₀
νₜ ∂v̄/∂z|ᶻ⁼⁰ = τᵧ/ρ₀
```

**Friction velocity:**
A key derived quantity is the friction velocity:
```
u* = √(τ/ρ₀) = √(τₓ² + τᵧ²)/ρ₀
```
This sets the scale for turbulent kinetic energy production at the surface.

### 3.3 Heat Fluxes

The net heat flux at the surface determines heating/cooling of the water column:
```
Q_net = Q_sw + Q_lw + Q_sens + Q_lat
```

All fluxes use the convention: **positive = heat into ocean**.

#### 3.3.1 Shortwave (Solar) Radiation (Q_sw)

**Source**: Direct and diffuse solar radiation

**Measurement/Input**: Typically measured by pyranometer or estimated from cloud cover and solar geometry

**Typical values**: 
- Clear sky, noon, summer: 800-1000 W/m²
- Overcast: 100-200 W/m²
- Night: 0 W/m²

**Absorption profile:**
Shortwave radiation penetrates into the water column following Beer's law:
```
I(z) = I₀ [A e^(-k₁z) + (1-A) e^(-k₂z)]
```

where:
- I₀ = surface radiation
- A = fraction in visible band (~0.62)
- k₁ = attenuation for visible light (0.01-1 m⁻¹, depends on water clarity)
- k₂ = attenuation for infrared (~10-100 m⁻¹)

**Bio-optical feedback:**
In productive waters, phytoplankton absorption increases k₁, limiting penetration depth. GOTM can couple to FABM for chlorophyll-dependent light attenuation.

**Surface albedo:**
Fraction of incident radiation reflected:
```
Q_sw(absorbed) = (1 - α) Q_sw(incident)
```
where α = albedo (~0.06 for water, 0.3-0.8 for ice/snow)

GOTM computes albedo using **Payne's (1972)** or **Cogley's (1979)** formulation accounting for:
- Solar zenith angle
- Cloud cover
- Surface roughness
- Ice/snow cover (if STIM enabled)

#### 3.3.2 Longwave (Infrared) Radiation (Q_lw)

**Source**: Thermal radiation from atmosphere (downward) and water surface (upward)

```
Q_lw = Q_lw↓ - Q_lw↑
```

**Downward longwave (Q_lw↓):**
Emitted by atmosphere, depends on air temperature, humidity, and cloud cover.

GOTM includes **multiple formulations** for downward longwave radiation:

**1. Clark et al. (1974)**
```
Q_lw↓ = εₐ σ Tₐᵢᵣ⁴
```
where εₐ = atmospheric emissivity (~0.7-0.95, increases with humidity and clouds)

**2. Hastenrath & Lamb (1978)** - For tropical regions

**3. Bignami et al. (1995)** - Mediterranean applications  

**4. Berliand & Berliand (1952)** - Classic formulation

**5. Josey et al. (2003)** - Modern synthesis

**6. Other empirical formulations**

All formulations calculate atmospheric emissivity (εₐ) from:
- Air temperature (Tₐᵢᵣ)
- Water vapor pressure or relative humidity
- Cloud cover fraction

where:
- σ = Stefan-Boltzmann constant = 5.67×10⁻⁸ W m⁻² K⁻⁴
- Tₐᵢᵣ = air temperature (Kelvin)

**Upward longwave (Q_lw↑):**
Emitted by water surface:
```
Q_lw↑ = εw σ Tsea⁴
```
where εw ≈ 0.97 (water emissivity)

**Typical values**: 
- Q_lw↓: 300-450 W/m² (warmer, more humid = higher)
- Q_lw↑: 350-500 W/m²
- Q_lw (net): -50 to +50 W/m² (usually cooling)

**Cloud effects:**
Clouds increase Q_lw↓ (warmer bodies radiating down), reducing nighttime cooling.

#### 3.3.3 Sensible Heat Flux (Q_sens)

**Physical process**: Conduction/convection of heat between air and water when they are at different temperatures.

**Bulk formula:**
```
Q_sens = ρₐᵢᵣ cₚ Cₕ |U₁₀| (Tsea - Tair)
```

where:
- cₚ = specific heat of air (~1005 J kg⁻¹ K⁻¹)
- Cₕ = heat transfer coefficient (~0.001, similar magnitude to Cᴅ)
- Tsea - Tair = sea-air temperature difference

**Sign convention:**
- Tsea > Tair → Q_sens > 0 → ocean loses heat to atmosphere
- Tsea < Tair → Q_sens < 0 → ocean gains heat (rare, except in cold air outbreaks)

**Typical values**: -50 to +50 W/m²

**Stability dependence:**
Like Cᴅ, Cₕ depends on atmospheric stability:
- Unstable (warm water, cold air): Enhanced transfer
- Stable (cold water, warm air): Suppressed transfer

#### 3.3.4 Latent Heat Flux (Q_lat)

**Physical process**: Energy consumed/released by evaporation/condensation

**Bulk formula:**
```
Q_lat = ρₐᵢᵣ Lᵥ Cₑ |U₁₀| (qsea - qair)
```

where:
- Lᵥ = latent heat of vaporization (~2.5×10⁶ J/kg)
- Cₑ = moisture transfer coefficient (~0.001)
- qsea = saturation specific humidity at sea surface temperature
- qair = specific humidity of air at 10 m

**Specific humidity:**
Related to relative humidity (RH) and saturation vapor pressure (esat):
```
q = 0.622 e/(P - 0.378 e)
```
where e = RH × esat(T), and P = atmospheric pressure

**Sign convention:**
- Evaporation (qsea > qair): Q_lat > 0 → ocean loses heat
- Condensation (qsea < qair): Q_lat < 0 → ocean gains heat (rare)

**Typical values**: 
- Tropics: 100-150 W/m²
- Mid-latitudes: 50-100 W/m²
- High latitudes: 10-50 W/m²

Latent heat flux is often the **largest** component of ocean heat loss.

### 3.4 Freshwater Flux

```
FW = E - P - R
```

where:
- E = evaporation rate (m/s), derived from Q_lat/Lᵥ
- P = precipitation rate (m/s)
- R = runoff (rivers, rarely used in GOTM)

**Effect on salinity:**
```
∂S̄/∂t|ᶻ⁼⁰ = -S₀ FW/Δz
```
where S₀ is surface salinity and Δz is top layer thickness.

**Virtual salt flux vs. real freshwater flux:**
Many models use "virtual salt flux" instead of actually changing volume. GOTM can do both.

### 3.5 Combined Surface Boundary Conditions

**Momentum:**
```
νₜ ∂ū/∂z|ᶻ⁼⁰ = τₓ/ρ₀
νₜ ∂v̄/∂z|ᶻ⁼⁰ = τᵧ/ρ₀
```

**Temperature:**
```
κₜ ∂T̄/∂z|ᶻ⁼⁰ = Q_net/(ρ₀ cₚ) - Q_sw(penetrating)/Δz
```

Note: Surface shortwave is handled specially since it penetrates.

**Salinity:**
```
κₛ ∂S̄/∂z|ᶻ⁼⁰ = -S₀ (E - P)/Δz
```

**Turbulent kinetic energy:**
```
k(z=0) = (u*/cμ₀)²
```
where cμ₀ ≈ 0.5477 relates surface TKE to friction velocity.

### 3.6 Diurnal Cycle and Ocean Skin

**Diurnal warm layer (DWL):**
Under calm, sunny conditions, shortwave heating creates a shallow (~1-3 m) warm layer that is destroyed by evening cooling or wind mixing. GOTM resolves DWL with sufficient vertical resolution (1 m or finer near surface).

**Cool skin:**
At the exact air-sea interface (~1 mm), strong longwave and evaporative cooling creates a ~0.1-0.5°C temperature drop. GOTM does not explicitly resolve the cool skin (requires specialized parameterization), but uses bulk sea surface temperature.

**Importance:**
- Satellite SST measures skin temperature (cool skin)
- In-situ buoys measure subsurface temperature (~1 m depth)
- Differences can be 0.5-1°C, affecting heat flux calculations

### 3.7 Ice-Covered Conditions

When STIM (Sea Thermodynamics Ice Module) is enabled:

**Modified surface fluxes:**
- Wind stress transmitted through ice (with coupling coefficient)
- Shortwave radiation attenuated by ice and snow before reaching water
- Longwave, sensible, latent fluxes computed for ice-atmosphere interface
- Ice growth/melt determined by energy balance

**Ice formation:**
When water temperature reaches freezing point, excess cooling forms ice.

**Radiation penetration:**
Some shortwave transmits through ice (10-50% depending on thickness and snow cover), supporting under-ice phytoplankton blooms.

### 3.8 Implementation in GOTM

**Key source files:**
- `do_air_sea.F90`: Main routine computing all fluxes
- `fairall.F90`: COARE 3.0 bulk algorithm
- `albedo.F90`: Surface albedo computation
- `set_sst.F90`: Sets sea surface temperature for flux calculations

**Input requirements:**
- Wind speed/direction at 10 m (u10, v10)
- Air temperature at 10 m (Tair)
- Air pressure (typically 1013 hPa if not provided)
- Relative humidity or specific humidity
- Cloud cover (0-1) or direct shortwave radiation
- Precipitation rate (optional)

**Typical input file format:**
```
# YYYY-MM-DD HH:MM:SS  u10  v10  airp   airt   hum   cloud
2020-01-01 00:00:00    5.2  2.1  101300  10.5  0.75  0.6
2020-01-01 01:00:00    5.5  2.3  101250  10.3  0.77  0.7
```

**Output diagnostics:**
GOTM can output:
- Individual flux components (Q_sw, Q_lw, Q_sens, Q_lat)
- Wind stress (tx, ty)
- Friction velocity (u*)
- Drag coefficient (Cd)
- Evaporation rate
- Net heat flux

These diagnostics are essential for understanding mixed layer evolution and validating against observations.

### 3.9 References for Air-Sea Interaction

**Bulk flux algorithms:**
- **Fairall et al. (1996)**: "Bulk parameterization of air-sea fluxes for Tropical Ocean-Global Atmosphere Coupled-Ocean Atmosphere Response Experiment." *J. Geophys. Res.*, 101(C2), 3747-3764. [DOI](https://doi.org/10.1029/95JC03205)
- **Fairall et al. (2003)**: "Bulk parameterization of air–sea fluxes: Updates and verification for the COARE algorithm." *J. Climate*, 16(4), 571-591. [DOI](https://doi.org/10.1175/1520-0442(2003)016%3C0571:BPOASF%3E2.0.CO;2)
- **COARE Algorithm:** [GitHub Repository](https://github.com/NOAA-PSL/COARE-algorithm)
- **Kondo (1975)**: "Air-sea bulk transfer coefficients in diabatic conditions." *Boundary-Layer Meteorol.*, 9, 91-112. [DOI](https://doi.org/10.1007/BF00232256)

**Drag coefficients:**
- **Large & Pond (1981)**: "Open ocean momentum flux measurements in moderate to strong winds." *J. Phys. Oceanogr.*, 11(3), 324-336. [DOI](https://doi.org/10.1175/1520-0485(1981)011%3C0324:OOMFMI%3E2.0.CO;2)

**Longwave radiation:**
- **Clark et al. (1974)**: "Short wave radiation and its relation to cooling of a lake." *J. Atmos. Sci.*, 31, 592-596. [DOI](https://doi.org/10.1175/1520-0469(1974)031%3C0592:SWRAIR%3E2.0.CO;2)
- **Hastenrath & Lamb (1978)**: "Heat budget atlas of the tropical Atlantic and eastern Pacific oceans." University of Wisconsin Press.
- **Bignami et al. (1995)**: "Longwave radiation budget in the Mediterranean Sea." *J. Geophys. Res.*, 100(C2), 2501-2514. [DOI](https://doi.org/10.1029/94JC02496)
- **Berliand & Berliand (1952)**: "Determining the net long-wave radiation of the earth with consideration of the effect of cloudiness." *Izv. Akad. Nauk SSSR Ser. Geofiz.*, 1, 64-78.
- **Josey et al. (2003)**: "A new formula for determining the atmospheric longwave flux at the ocean surface at mid-high latitudes." *J. Geophys. Res.*, 108(C4), 3108. [DOI](https://doi.org/10.1029/2002JC001418)

**Solar radiation:**
- **Payne (1972)**: "Albedo of the sea surface." *J. Atmos. Sci.*, 29(5), 959-970. [DOI](https://doi.org/10.1175/1520-0469(1972)029%3C0959:AOTSS%3E2.0.CO;2)
- **Paulson & Simpson (1977)**: "Irradiance measurements in the upper ocean." *J. Phys. Oceanogr.*, 7(6), 952-956. [DOI](https://doi.org/10.1175/1520-0485(1977)007%3C0952:IMITUO%3E2.0.CO;2)
- **Cogley (1979)**: "The albedo of water as a function of latitude." *Mon. Weather Rev.*, 107(6), 775-781. [DOI](https://doi.org/10.1175/1520-0493(1979)107%3C0775:TAOWAA%3E2.0.CO;2)

---

## 4. Equation of State and TEOS-10

### 4.1 Density in Aquatic Systems

Water density (ρ) is fundamental to aquatic dynamics, controlling:
- Buoyancy and stratification
- Baroclinic pressure gradients
- Vertical stability (via buoyancy frequency N²)
- Mixing and entrainment

Density depends on:
- **Temperature (T):** Warming decreases density (thermal expansion)
- **Salinity (S):** Increased salt increases density
- **Pressure (p):** Compression increases density (important for deep ocean)

### 4.2 Traditional vs. Modern Temperature and Salinity Measures

#### Traditional Measures (Pre-TEOS-10)

**In Situ Temperature (T):**
- Temperature measured by a thermometer at depth
- Affected by adiabatic compression
- Unit: °C
- Symbol: T

**Potential Temperature (θ):**
- Temperature a water parcel would have if moved adiabatically to surface (0 dbar)
- Removes pressure effects
- Conserved for adiabatic processes
- Unit: °C
- Symbol: θ

**Practical Salinity (SP):**
- Dimensionless quantity based on conductivity ratio
- Practical Salinity Scale 1978 (PSS-78)
- Symbol: SP
- Range: Typically 0-42 in ocean (average ~35)
- Unit: Traditionally quoted as "psu" (practical salinity units), but officially dimensionless

**Traditional Equation of State:**
- UNESCO 1980 (EOS-80)
- ρ = ρ(SP, θ, p)
- Empirical fit to laboratory measurements

#### TEOS-10 Standard (Modern, Recommended)

The **Thermodynamic Equation Of Seawater - 2010 (TEOS-10)** represents a major advance in oceanographic thermodynamics.

**Conservative Temperature (Θ):**
- Proportional to potential enthalpy
- Better conserved than potential temperature under mixing
- Unit: °C
- Symbol: Θ (capital theta)
- Relationship: Θ ≈ θ - 0.02°C (small offset)

**Why conservative temperature?**
When two water parcels mix:
- Potential temperature (θ) is **not** exactly conserved due to pressure differences
- Conservative temperature (Θ) **is** conserved (to within TEOS-10 accuracy)
- This improves accuracy in mixing calculations

**Absolute Salinity (SA):**
- True mass fraction of dissolved material in seawater
- Unit: g/kg
- Symbol: SA
- Accounts for spatial variations in seawater composition
- Relationship: SA = (35.16504/35) × SP × (1 + δSA)
  - δSA corrects for composition anomalies (typically < 1%)
  - δSA varies geographically (requires lookup tables)

**Why absolute salinity?**
- Different ocean regions have different dissolved compositions (not just NaCl)
- Baltic Sea, Mediterranean, Red Sea have measurable δSA
- Absolute salinity is the true thermodynamic variable

**TEOS-10 Equation of State:**
- Based on Gibbs potential
- Thermodynamically rigorous
- ρ = ρ(SA, Θ, p)
- Website: http://www.teos-10.org/

**Reference:**  
IOC, SCOR and IAPSO, 2010: *The international thermodynamic equation of seawater – 2010: Calculation and use of thermodynamic properties.* Intergovernmental Oceanographic Commission, Manuals and Guides No. 56, UNESCO. [TEOS-10 Manual](http://www.teos-10.org/pubs/TEOS-10_Manual.pdf)

### 4.3 Buoyancy Frequency

GOTM can work with temperature and salinity **or** directly with buoyancy.

**Buoyancy (b):**
```
b = -g(ρ - ρ₀)/ρ₀
```

**Buoyancy frequency (N²):**
```
N² = -g/ρ₀ ∂ρ/∂z = ∂b/∂z
```

- N² > 0: Stable stratification (suppresses turbulence)
- N² = 0: Neutral (no stratification)
- N² < 0: Unstable (convection occurs)

**Typical values:**
- Surface mixed layer: N² ~ 10⁻⁵ to 10⁻⁴ s⁻²
- Thermocline: N² ~ 10⁻⁴ to 10⁻³ s⁻²
- Deep ocean: N² ~ 10⁻⁶ s⁻²

### 4.4 GOTM Implementation

**Configuration options (Development version):**

GOTM currently supports the following equation of state formulations:

1. **TEOS-10 (Recommended):**
   ```yaml
   eq_state_method: 3
   eq_state_mode: 2  # use conservative temp and absolute salinity
   ```
   - Uses: Conservative temperature Θ, absolute salinity SA
   - Thermodynamically consistent
   - Recommended for all new simulations
   - Reference: IOC et al. (2010) - [TEOS-10 Manual](http://www.teos-10.org/pubs/TEOS-10_Manual.pdf)

2. **Direct buoyancy:**
   ```yaml
   eq_state_mode: 3  # prognostic buoyancy
   ```
   - Solves for buoyancy directly, not T and S
   - Useful for idealized studies

**Legacy formulations (Reference only - not in current development version):**

The following formulations were available in earlier GOTM versions but have been **removed from the development (master) branch** in favor of TEOS-10:

- **UNESCO 1980 (EOS-80):** Used in situ temperature T and practical salinity SP
  - Reference: UNESCO (1981): "The practical salinity scale 1978 and the international equation of state of seawater 1980." *UNESCO technical papers in marine science*, 36, 25pp.
  
- **Jackett et al. (2006):** Improved fit over wider ranges
  - Reference: Jackett et al. (2006): "Algorithms for density, potential temperature, conservative temperature, and the freezing temperature of seawater." *J. Atmos. Ocean. Technol.*, 23(12), 1709-1728. [DOI](https://doi.org/10.1175/JTECH1946.1)

For simulations requiring these legacy formulations (e.g., to reproduce historical results), use an older tagged GOTM release (v6.0.x or earlier).

### 4.5 Practical Recommendations

**For ocean simulations:**
- Use TEOS-10 for new work
- Essential for high-accuracy studies
- Required for comparison with modern observations

**For lake simulations:**
- Temperature-only equation of state available (S ≈ 0)
- Or use TEOS-10 with S = 0

**For legacy comparison:**
- Use EOS-80 to match historical simulations

**For idealized studies:**
- Linear equation of state or direct buoyancy

### 4.6 TEOS-10 Resources

- **Website:** http://www.teos-10.org/
- **Software:** [GSW (Gibbs SeaWater) toolbox](http://www.teos-10.org/software.htm)
  - Available in Fortran, C, MATLAB, Python, R
- **Getting Started:** http://www.teos-10.org/pubs/Getting_Started.pdf

---

## 5. Introduction to Turbulence Closure Models

### 5.1 The Closure Problem

Ocean and lake turbulence spans scales from millimeters (Kolmogorov) to hundreds of meters (basin). Direct Numerical Simulation (DNS) of all scales is computationally prohibitive. Instead, we use Reynolds-Averaged Navier-Stokes (RANS) equations, decomposing variables into mean and fluctuating parts:

```
u = ū + u'    (velocity)
θ = θ̄ + θ'    (temperature)
```

Averaging introduces Reynolds stresses ⟨u'w'⟩ and scalar fluxes ⟨θ'w'⟩ as new unknowns. **Turbulence closure models** provide relationships between these fluxes and mean quantities, closing the system of equations.

### 5.2 Closure Hierarchy

**Zero-Equation Models:**
- Algebraic prescriptions for eddy viscosity
- Examples: Pacanowski-Philander, constant viscosity
- Pro: Simple, fast
- Con: No memory, cannot respond to transient forcing

**One-Equation Models:**
- Prognostic equation for turbulent kinetic energy (TKE)
- Length scale prescribed algebraically
- Pro: Responds to time-varying forcing
- Con: Length scale parameterization limits accuracy

**Two-Equation Models:**
- Prognostic equations for TKE and length-scale determining variable
- Examples: k-ε, k-ω, Mellor-Yamada 2.5, Generic Length Scale (GLS)
- Pro: Well-validated, efficient, physically consistent
- Con: Assumes local isotropy

**Second-Moment Closures:**
- Prognostic equations for all Reynolds stress components
- Examples: Full Mellor-Yamada, Kantha-Clayson
- Pro: Handles anisotropy, rotation
- Con: Computationally expensive, many empirical constants

GOTM specializes in **two-equation models** via the Generic Length Scale (GLS) framework, which unifies k-ε, k-ω, and Mellor-Yamada under one formulation.

### 5.3 Eddy Viscosity/Diffusivity

Most GOTM closures employ the eddy viscosity concept:

```
⟨u'w'⟩ = -νₜ ∂ū/∂z    (momentum flux)
⟨θ'w'⟩ = -κₜ ∂θ̄/∂z    (heat flux)
```

where νₜ (eddy viscosity) and κₜ (eddy diffusivity) are computed from:

```
νₜ = Sₘ L k^(1/2)
κₜ = Sₕ L k^(1/2)
```

Here:
- k = turbulent kinetic energy
- L = turbulent length scale
- Sₘ, Sₕ = stability functions (depend on stratification)

### 2.4 Key Physical Processes

**Shear Production (P):**
- Generated by velocity gradients: P = νₜ S²
- S² = (∂ū/∂z)² + (∂v̄/∂z)² (shear squared)
- Always positive (creates turbulence)

**Buoyancy Production (B):**
- Controlled by stratification: B = -g κₜ ∂ρ̄/∂z
- Negative in stable stratification (suppresses turbulence)
- Positive in unstable stratification (enhances turbulence, convection)

**Dissipation (ε):**
- Energy cascade to molecular scales: ε ∝ k^(3/2) / L
- Removes TKE from the system

**Richardson Number:**
```
Ri = N² / S²
```
where N² = -g/ρ₀ ∂ρ̄/∂z (buoyancy frequency squared)

- Ri << 1: Shear-dominated, strong mixing
- Ri ~ 0.25: Critical value for shear instability
- Ri >> 1: Stratification-dominated, weak mixing

### 2.5 Why Turbulence Matters

Vertical mixing controls:
- **Ocean**: Mixed layer depth, SST, air-sea fluxes, biological productivity, CO₂ uptake
- **Lakes**: Thermal structure, anoxia, nutrients, algal blooms, water quality
- **Estuaries**: Salinity intrusion, sediment dynamics, residence times

Errors in mixing propagate to ecosystem predictions, making turbulence closure critical.

### 2.6 GOTM's Approach

GOTM implements the **Generic Length Scale (GLS)** framework (Umlauf & Burchard, 2003), which unifies multiple two-equation models through parameters (p, m, n):

| Model | p | m | n | Second Variable |
|-------|---|---|---|-----------------|
| k-ε | 3.0 | 1.5 | -1.0 | Dissipation rate |
| k-ω | -1.0 | 0.5 | -1.0 | Specific dissipation |
| Mellor-Yamada | 0.0 | 1.0 | 1.0 | Length scale × TKE |
| Generic | 2.0 | 1.0 | -0.67 | Umlauf-Burchard |

This framework has been extensively validated and is used in many 3D ocean models.

**Key References:**
- Mellor & Yamada (1982): Foundation of hierarchy
- Burchard & Bolding (2001): GOTM comparative study
- Umlauf & Burchard (2003): GLS framework
- Umlauf & Burchard (2005): Review of second-order closures
- Warner et al. (2005): Performance comparisons

---

## 6. Numerical Methods

### 6.1 Overview

GOTM employs robust numerical methods to solve the one-dimensional partial differential equations governing ocean and lake dynamics. The methods balance accuracy, stability, efficiency, and conservation.

### 6.2 Time Discretization

GOTM uses a **generalized θ-method** for time stepping.

**General form:**
For an equation ∂u/∂t = F(u), discretize as:
```
(uⁿ⁺¹ - uⁿ)/Δt = θF(uⁿ⁺¹) + (1-θ)F(uⁿ)
```

**Special cases:**
- θ = 0: **Forward Euler** (explicit, conditionally stable)
- θ = 0.5: **Crank-Nicolson** (implicit, 2nd-order accurate, unconditionally stable) **← default**
- θ = 1: **Backward Euler** (implicit, 1st-order accurate, unconditionally stable)

**Configuration:**
```yaml
time:
  dt: 3600.0  # time step in seconds
  theta: 0.5  # Crank-Nicolson (recommended)
```

**Typical time steps:**
- Ocean: 300-3600 s (5 min to 1 hour)
- Lakes: 60-600 s (1-10 min)
- Idealized cases: 1-60 s for high resolution

### 6.3 Vertical Discretization

GOTM uses **finite differences** on a staggered grid.

**Grid arrangement:**
```
z = 0 (Surface)  ━━━━━━━━━━━━━━━  ← Boundary condition (flux)
                 ┃              
  Δz/2           ┃              ← T, S, u, v (cell center, level 1)
                 ┃
                 ━━━━━━━━━━━━━━━  ← νₜ, κₜ, TKE, ε (interface 1-2)
                 ┃
  Δz             ┃              ← T, S, u, v (cell center, level 2)
                 ┃
                 ━━━━━━━━━━━━━━━  ← νₜ, κₜ, TKE, ε (interface 2-3)
                 ┃
                 ┃              ← T, S, u, v (cell center, level 3)
                 .
                 .
                 .
                 ━━━━━━━━━━━━━━━  ← νₜ, κₜ, TKE, ε (interface N-1,N)
                 ┃
  Δz/2           ┃              ← T, S, u, v (cell center, level N)
                 ┃
z = -H (Bottom)  ━━━━━━━━━━━━━━━  ← Boundary condition (no-flux or drag)
```

**Key points:**
- **Scalars** (T, S, u, v): Located at **cell centers** (half-layer thickness from interfaces)
- **Turbulent quantities** (νₜ, κₜ, k, ε): Located at **cell interfaces**
- **Boundary conditions**: Applied at z=0 (surface) and z=-H (bottom)
- Top cell has thickness Δz/2 (from surface to first interface)
- Bottom cell has thickness Δz/2 (from last interface to bottom)

**Why staggered?**
- Natural placement of variables
- Turbulent fluxes (νₜ∂u/∂z) evaluated at interfaces where gradients are computed
- Improved accuracy and stability
- Exact energy conservation possible

**Vertical grid options:**

1. **Equidistant (uniform spacing):**
   ```yaml
   grid:
     nlev: 100
     ddu: 0.0
     ddl: 0.0
   ```

2. **Zoomed grid (higher resolution near surface/bottom):**
   ```yaml
   grid:
     nlev: 100
     ddu: 2.0  # surface zooming
     ddl: 2.0  # bottom zooming
   ```
   Higher ddu/ddl = more zooming (exponential grid stretching)

**Typical vertical resolution:**
- Open ocean: 100-200 levels over 50-200 m
- Coastal/shelf: 50-100 levels over 20-100 m
- Lakes: 50-150 levels over 10-50 m

### 6.4 Diffusion Solver

The core of GOTM is solving diffusion equations of the form:
```
∂φ/∂t = ∂/∂z(D ∂φ/∂z) + source
```

**Solution method:**
- Forms tridiagonal system: Aφⁿ⁺¹ = b
- Solved with **Thomas algorithm** (O(N), very fast)
- Direct solution, no iteration required
- Numerically stable

### 6.5 Turbulence Integration

**Patankar scheme** for production-destruction equations ensures:
- Positivity (k, ε > 0 always)
- Stability for stiff systems
- Energy conservation

**Reference:** Burchard et al. (2003): "A high-order conservative Patankar-type discretisation for stiff systems of production-destruction equations." *Appl. Numer. Math.*, 47(1), 1-30. [DOI](https://doi.org/10.1016/S0168-9274(03)00101-6)

### 6.6 Computational Performance

**Typical cost:**
- 100 levels, annual simulation: 1-10 seconds on modern CPU
- Bottleneck: Often I/O, not computation
- FABM coupling increases cost 10-100x (depending on BGC complexity)

### 6.7 Key References

**GOTM numerical methods:**
- Burchard & Bolding (2001): General framework
- Burchard (2002): Energy-conserving discretization - [DOI](https://doi.org/10.1016/S1463-5003(02)00009-4)
- Burchard et al. (2003): Patankar scheme - [DOI](https://doi.org/10.1016/S0168-9274(03)00101-6)
- Burchard & Beckers (2004): Adaptive grids - [DOI](https://doi.org/10.1016/S1463-5003(02)00060-4)

---

## 7. Architecture and Design

### 7.1 Git Submodules and External Dependencies

GOTM uses Git submodules in `extern/` for modular integration of external libraries. Each submodule is a full clone of its repository, enabling independent development cycles and easy updates.

#### Core Submodules:

**1. yaml-cpp** (`extern/yaml`)
- Purpose: YAML 1.2 parser (C++)
- Function: Parses `gotm.yaml`, `output.yaml`, `fabm.yaml`
- Repository: https://github.com/jbeder/yaml-cpp
- Impact: Enables modern, human-readable configuration

**2. field_manager** (`extern/field_manager`)
- Purpose: Central variable registry with metadata
- Function: 
  - Variable registration with units, long names, CF standard names
  - Attribute system for variable properties
  - Hotstart/restart (variables tagged with `state` attribute saved to `restart.nc`)
  - Coordinates I/O with flexout
- Always required

**3. flexout** (`extern/flexout`)
- Purpose: Flexible output manager with operators
- Integrated: January 2019
- Function:
  - Time-averaging (mean, integrated, instantaneous)
  - Spatial interpolation (sigma → z-coordinates)
  - Multiple output files with different resolutions
  - Custom derived fields
- Configured via `output.yaml`
- Dramatically reduces post-processing needs

**4. FABM** (`extern/fabm`)
- Purpose: Framework for Aquatic Biogeochemical Models
- Repository: https://github.com/fabm-model/fabm
- CMake flag: `-DGOTM_USE_FABM=ON`
- Function:
  - BGC model library (ERSEM, NPZD, ECOSMO, etc.)
  - Pelagic and benthic state variables
  - Feedback to physics (shading, albedo, drag)
- Configuration: `fabm.yaml` + `gotm.yaml` (coupling settings)
- No longer requires manual `FABM_BASE` path

**5. CVMix** (`extern/cvmix`)
- Purpose: Community Ocean Vertical Mixing library
- Repository: [CVMix on GitHub](https://github.com/CVMix/CVMix-src)
- CMake flag: `-DGOTM_USE_CVMIX=ON`
- Configuration: `turb_method: 100` in `gotm.yaml`
- Function:
  - KPP with Langmuir turbulence (Li et al., 2019)
  - Tidal mixing, double diffusion
  - Shear instability, internal wave breaking
- Interface: `do_cvmix()` called alongside `do_turbulence()`

**6. STIM** (`extern/stim`)
- Purpose: Simple Thermodynamic Ice Models
- CMake flag: `-DGOTM_USE_STIM=ON`
- Ice models:
  - Model 1: Lebedev (1938)
  - Model 2: MyLake
  - Model 3: Winton (in development)
- Effects: Ice formation/melting, modified surface fluxes, radiation penetration

#### Submodule Management:

```bash
# Clone with submodules
git clone --recurse-submodules https://github.com/gotm-model/code.git

# Update existing clone
git pull
git submodule update --init --recursive

# Initialize specific submodule
git submodule update --init extern/fabm
```

Benefits:
- No manual path configuration
- Independent component updates
- Shared across GOTM, GETM, 3D models
- Reduces maintenance burden

### 7.2 Modular Source Code Structure

```
gotm (main executable)
├── airsea (surface forcing)
├── meanflow (momentum, T, S)
├── turbulence (closures)
├── observations (data input)
├── output (NetCDF via flexout)
├── util (utilities)
└── extras (seagrass, optional modules)
```

### 7.3 Main Program Flow

1. **init_gotm()**: Parse YAML, initialize modules, setup grid, initial conditions
2. **time_loop()**: 
   - Update forcing
   - Solve momentum equations
   - Apply turbulence closure
   - Solve T/S equations
   - Update FABM (if enabled)
   - Write output
3. **clean_up()**: Close files, deallocate

---

## 8. Core Modules

### 8.1 Meanflow Module

**Location:** `src/meanflow/`

Handles mean flow dynamics:
- Grid management: `updategrid.F90` (sigma/z-coordinate)
- Coriolis: `coriolis.F90` (rotation effects)
- Momentum: `uequation.F90`, `vequation.F90` (U, V transport with friction)
- Pressure gradients: `extpressure.F90` (barotropic), `intpressure.F90` (baroclinic)
- Vertical velocity: `wequation.F90`

State variables: U, V, T, S, buoyancy, grid spacing

### 8.2 Turbulence Module

**Location:** `src/turbulence/`

Core of GOTM with multiple closure schemes.

**Closure Selection** (`turb_method`):
- `0`: Convective adjustment
- `1`: Analytical eddy viscosity
- `2`: First-order (TKE + length scale)
- `3`: Second-order (Reynolds stress)
- `99`: KPP
- `100`: CVMix (requires CVMix submodule)

**TKE Equation** (`tke_method`):
- `1`: Algebraic
- `2`: Dynamic (k-ε style)
- `3`: Dynamic (Mellor-Yamada style)

**Length Scale** (`len_scale_method`):
- `1-7`: Algebraic prescriptions
- `8`: Dynamic ε-equation
- `9`: Dynamic generic (GLS)

Components:
- `tkeeq.F90`: TKE equation
- `lengthscaleeq.F90`: Length scale/dissipation equation
- `cmue_*.F90`: Stability functions
- `production.F90`: Shear/buoyancy production

### 8.3 Air-Sea Exchange Module

**Location:** `src/airsea/`

Computes surface boundary conditions:
- Momentum flux: Wind stress (Fairall et al. formulation, stability-dependent)
- Heat fluxes: Solar SW, longwave, sensible, latent
- Freshwater: Precipitation, evaporation
- Albedo: Bio-optical effects

Input: Wind (u10, v10), air temp/pressure/humidity, clouds, solar radiation, precipitation

### 8.4 Observations Module

**Location:** `src/observations/`

Manages external forcing and data input.

**File formats:**
- **Profile**: `YYYY-MM-DD HH:MM:SS  nlev  direction`
  ```
  depth_1  value_1
  depth_2  value_2
  ...
  ```
- **Time series**: `YYYY-MM-DD HH:MM:SS  val1  val2 ...`

Interpolation: Linear in time and space, extrapolation uses nearest values.

Profile methods (`t_prof_method`, `s_prof_method`):
- `0`: None
- `1`: Analytical initial
- `2`: From file with temporal interpolation

### 8.5 Output Module

**Location:** `src/output/`

Modern NetCDF output via flexout.

**Output operators:**
- `mean`: Temporal averaging
- `integrated`: Time integration
- `instantaneous`: Snapshots
- `interp`: Interpolation to z-levels

**Configuration** (via `output.yaml`):
- Variables to save
- Time/space resolution
- Operator type
- Multiple output files

**Standard variables:**
- State: temp, salt, u, v, h, tke, eps, num, nuh, nus
- Diagnostics: NN (N²), SS (S²), Rig, P, G
- Fluxes: heat, tx, ty, swr, I_0
- Derived: mld_surf, mld_bott

---

## 9. Turbulence Closure Models in Detail

### 9.1 Generic Length Scale (GLS) Framework

**Governing Equations:**

TKE equation:
```
∂k/∂t = ∂/∂z(νₜ/σₖ ∂k/∂z) + P + B - ε
```

Generic length scale equation:
```
∂ψ/∂t = ∂/∂z(νₜ/σψ ∂ψ/∂z) + ψ/k (c₁P + c₃B - c₂ε F_wall)
```

where ψ = k^m L^n, with (p, m, n) defining specific models.

**Eddy viscosity:**
```
νₜ = Sₘ k^(1/2) L
```

Sₘ is a stability function depending on N² and S².

### 9.2 k-ε Model

Parameters: p=3, m=1.5, n=-1

Constants:
- cε1 = 1.44
- cε2 = 1.92
- cε3minus = -0.52 (stable)
- cε3plus = 1.0 (unstable)
- σₖ = 1.0
- σε = 1.3
- cμ0 = 0.5477

Limitations: Flawed under breaking waves (Umlauf et al., 2003)

### 9.3 k-ω Model

Parameters: p=-1, m=0.5, n=-1

Better for wave breaking scenarios.

### 9.4 Mellor-Yamada 2.5

Parameters: p=0, m=1, n=1

Well-established for boundary layers. Reproduces Monin-Obukhov similarity theory.

Two equations:
- q² (twice TKE)
- q²L (TKE × length scale)

### 9.5 KPP (K-Profile Parameterization)

Non-local boundary layer scheme.

Configuration: `kpp.inp` file
- Surface boundary layer: `kpp_sbl`
- Bottom boundary layer: `kpp_bbl`
- Interior: `kpp_interior`
- Critical Ri: `Ric`

### 9.6 Stability Functions

Multiple formulations available:
- Kantha-Clayson (KC): Default
- Canuto A: Alternative
- Galperin: Classical

Different functions require corresponding closure constants.

---

## 10. Build System and Dependencies

### 10.1 CMake Configuration

```bash
cmake -G Ninja -B build -S . [OPTIONS]
```

**Options:**
- `-DGOTM_USE_FABM=ON`: Enable biogeochemistry
- `-DGOTM_USE_STIM=ON`: Enable ice
- `-DGOTM_USE_CVMIX=ON`: Enable CVMix turbulence
- `-DGOTM_USE_NetCDF=ON`: NetCDF output (default ON)
- `-DGOTM_USE_SEAGRASS=ON`: Seagrass module

### 10.2 Required Dependencies

**Fortran Compiler:**
- Fortran 2003 support minimum
- gfortran ≥ 4.7, Intel Fortran, or similar
- **Critical:** NetCDF and GOTM must use same compiler on Linux/Mac

**NetCDF:**
- NetCDF with Fortran support (libnetcdff)
- Ubuntu/Debian: `apt-get install libnetcdff-dev`
- Pre-built Windows libraries included in repo

**Build Tools:**
- CMake ≥ 3.0
- Ninja (recommended) or Make

### 10.3 Conda Environment (Cross-Platform: Windows, Linux, macOS)

Conda provides a complete environment with all dependencies. **This works identically on Windows, Linux, and macOS.**

**Install Miniconda:**
- Download from: https://docs.conda.io/en/latest/miniconda.html
- Follow platform-specific installation instructions

**Create and use GOTM environment:**
```bash
# Navigate to GOTM source directory
cd /path/to/gotm/code

# Create environment from file
conda env create -f environment.yml

# Activate environment
conda activate gfortran
```

**Configure and compile (same commands on all platforms):**
```bash
# Configure with CMake
cmake -G Ninja -B build -S .

# Compile
cmake --build build

# Install (optional)
cmake --install build --prefix ~/.local
```

The conda environment provides:
- gfortran compiler
- CMake and Ninja build tools
- NetCDF libraries with Fortran support
- Python tools for analysis

**Advantages:**
- Consistent across platforms
- No manual dependency installation
- Isolated from system packages
- Easy to reproduce

---

## 11. Configuration System

### 11.1 YAML Configuration

Main file: `gotm.yaml`

**Version requirement:**
```yaml
version: 7  # configuration schema version
```

Legacy configs without version trigger error with auto-update instructions.

### 11.2 Key Configuration Sections

**For a complete, working example, see:**  
**[nns_annual/gotm.yaml](https://github.com/gotm-model/cases/blob/master/nns_annual/gotm.yaml)**

This demonstrates a realistic North Sea simulation with full time/location setup, turbulence configuration (k-ε), and surface forcing from files.

**Location:**
```yaml
location:
  name: 'Station Name'
  latitude: 57.0
  longitude: 10.0
  depth: 50.0
```

**Time:**
```yaml
time:
  start: '2020-01-01 00:00:00'
  stop: '2020-12-31 23:00:00'
  dt: 3600.0  # seconds
```

**Grid:**
```yaml
grid:
  nlev: 100
  method: 0  # 0=analytical, 1=file_sigma, 2=file_h
  ddu: 0.0   # surface zooming
  ddl: 0.0   # bottom zooming
```

**Turbulence:**
```yaml
turbulence:
  turb_method: 2
  tke_method: 2
  len_scale_method: 8
  scnd_method: 1
  stab_method: 1
```

**Surface Fluxes:**
```yaml
surface:
  fluxes:
    heat:
      method: 2  # from file
    tx:
      method: 2
    ty:
      method: 2
```

### 11.3 GOTM Command-Line Interface

**Basic usage:**
```bash
gotm [options]
```

**Writing YAML configuration:**

GOTM can generate template YAML files:

```bash
# Create gotm.yaml with default settings
gotm --write_yaml

# Create all configuration files
gotm --write_yaml --write_schema
```

This creates:
- `gotm.yaml` - main configuration
- `output.yaml` - output specification  
- Schema files for validation

**Custom configuration file:**
```bash
# Use specific config file
gotm --config my_setup.yaml
```

**Help and version:**
```bash
# Display help
gotm --help

# Show version
gotm --version

# Check configuration without running
gotm --check
```

**Advanced options:**
```bash
# Increase verbosity
gotm --verbose

# Dry run (test setup without running)
gotm --dry-run
```

**Typical workflow:**
```bash
# 1. Create template
gotm --write_yaml

# 2. Edit gotm.yaml for your case
nano gotm.yaml

# 3. Check configuration
gotm --check

# 4. Run simulation
gotm
```

---

## 12. File I/O System

### 12.1 Input Formats

**Meteorological forcing:**
```
YYYY-MM-DD HH:MM:SS  u10  v10  airp  airt  hum  cloud
```

**Profile data:**
```
YYYY-MM-DD HH:MM:SS  nlev  direction
depth1  value1
depth2  value2
...
```

**Scalar time series (e.g., external pressure gradient):**
```
# External pressure gradient forcing
# Format: YYYY-MM-DD HH:MM:SS  dpdx  dpdy
# Units: dpdx, dpdy in Pa/m

1990-01-01 00:00:00  0.0000E+00  0.0000E+00
1990-01-01 06:00:00  1.2500E-06  3.4500E-07
1990-01-01 12:00:00  2.1000E-06  1.5000E-07
1990-01-01 18:00:00  8.5000E-07 -2.1000E-07
1990-01-02 00:00:00 -5.0000E-07 -8.0000E-07
```

**Example file:** [nns_annual/ext_press_file.dat](https://github.com/gotm-model/cases/blob/master/nns_annual/ext_press_file.dat)

**Format notes:**
- Lines starting with `#` are comments
- Date/time in `YYYY-MM-DD HH:MM:SS` format
- Space-separated values
- Scientific notation allowed
- Linear interpolation between times

### 12.2 NetCDF Output

CF-1.6 compliant with:
- Unlimited time dimension
- Coordinate variables (z, time, lat, lon)
- Variable metadata (units, long_name, standard_name)

Configured via `output.yaml`:
```yaml
output:
  - file: 'result.nc'
    time_unit: 'hour'
    time_step: 1
    variables:
      - name: 'temp'
        operator: 'mean'
```

---

## 13. Optional Extensions

### 13.1 FABM

BGC framework supporting ERSEM, NPZD, ECOSMO, etc.

Enable: `-DGOTM_USE_FABM=ON`
Configure: `fabm.yaml` + coupling in `gotm.yaml`

### 13.2 STIM

Ice thermodynamics with 3 model options.

Enable: `-DGOTM_USE_STIM=ON`

### 13.3 CVMix

Additional turbulence schemes, especially Langmuir.

Enable: `-DGOTM_USE_CVMIX=ON`
Use: `turb_method: 100`

---

## 14. Installation and Compilation

### 14.1 Quick Start

```bash
# Clone repository
git clone --recurse-submodules https://github.com/gotm-model/code.git
cd code

# Configure
cmake -G Ninja -B build -S .

# Compile
cmake --build build

# Install (optional)
cmake --install build --prefix ~/.local
```

### 14.2 Platform-Specific

**Linux:**
```bash
sudo apt-get install gfortran cmake ninja-build libnetcdff-dev
cmake -G Ninja -B build
cmake --build build
```

**macOS:**
```bash
brew install gcc cmake ninja netcdf
cmake -G Ninja -B build
cmake --build build
```

**Windows:**
- Intel Fortran + Visual Studio
- Pre-built NetCDF included

### 14.3 Updating

```bash
git pull
git submodule update --init --recursive
cmake --build build
```

**Critical:** `git pull` alone does NOT update submodules.

---
EOFMARKER

## 15. Test Cases and Examples

### 15.1 Overview

The GOTM test cases repository provides ready-to-run scenarios demonstrating different physical processes, turbulence closures, and environmental conditions. All test cases are designed for the `master` branch.

**Repository:** https://github.com/gotm-model/cases

```bash
git clone --recurse-submodules https://github.com/gotm-model/cases.git
cd cases/<case_name>
gotm
```

### 15.2 Available Test Cases

| Case | Type | Description | Key Features | Link |
|------|------|-------------|--------------|------|
| **blacksea** | Realistic | Black Sea water column | Permanent stratification, anoxic conditions | [View](https://github.com/gotm-model/cases/tree/master/blacksea) |
| **channel** | Idealized | Tidal channel flow | Periodic forcing, bottom stress | [View](https://github.com/gotm-model/cases/tree/master/channel) |
| **couette** | Idealized | Couette flow | Constant shear, turbulence fundamentals | [View](https://github.com/gotm-model/cases/tree/master/couette) |
| **entrainment** | Idealized | Entrainment processes | Mixed layer deepening, interfacial mixing | [View](https://github.com/gotm-model/cases/tree/master/entrainment) |
| **estuary** | Idealized | Estuarine circulation | Density-driven flow, periodic stratification | [View](https://github.com/gotm-model/cases/tree/master/estuary) |
| **flex** | Realistic | Fladen Ground Experiment (FLEX'76) | Historic North Sea measurements, spring bloom | [View](https://github.com/gotm-model/cases/tree/master/flex) |
| **gotland** | Realistic | Baltic Sea Gotland Deep | Seasonal stratification, Baltic dynamics | [View](https://github.com/gotm-model/cases/tree/master/gotland) |
| **lago_maggiore** | Realistic | Lake Maggiore (Italian lake) | Lake stratification, seasonal overturn | [View](https://github.com/gotm-model/cases/tree/master/lago_maggiore) |
| **langmuir** | Idealized | Langmuir turbulence | Wave-driven mixing, CVMix demonstration | [View](https://github.com/gotm-model/cases/tree/master/langmuir) |
| **liverpool_bay** | Realistic | Liverpool Bay, Irish Sea | Tidal mixing, ROFI dynamics | [View](https://github.com/gotm-model/cases/tree/master/liverpool_bay) |
| **medsea_east** | Realistic | Eastern Mediterranean | Oligotrophic, deep convection | [View](https://github.com/gotm-model/cases/tree/master/medsea_east) |
| **medsea_west** | Realistic | Western Mediterranean | Wind mixing, seasonal thermocline | [View](https://github.com/gotm-model/cases/tree/master/medsea_west) |
| **nns_annual** | Realistic | Northern North Sea annual | Full seasonal cycle, temperate shelf | [View](https://github.com/gotm-model/cases/tree/master/nns_annual) |
| **nns_seasonal** | Realistic | Northern North Sea seasonal | Stratified summer period | [View](https://github.com/gotm-model/cases/tree/master/nns_seasonal) |
| **ows_papa** | Realistic | Ocean Weather Station Papa | North Pacific, storm mixing | [View](https://github.com/gotm-model/cases/tree/master/ows_papa) |
| **plume** | Idealized | Buoyant plume dynamics | Convection, density-driven flow | [View](https://github.com/gotm-model/cases/tree/master/plume) |
| **resolute** | Realistic | Arctic Resolute Passage | Sea ice, under-ice mixing | [View](https://github.com/gotm-model/cases/tree/master/resolute) |
| **reynolds** | Idealized | Reynolds stress demonstration | Second-moment closure | [View](https://github.com/gotm-model/cases/tree/master/reynolds) |
| **rouse** | Idealized | Rouse profile for sediments | Suspended sediment, equilibrium profiles | [View](https://github.com/gotm-model/cases/tree/master/rouse) |
| **seagrass** | Idealized | Seagrass canopy effects | Vegetation drag, modified mixing | [View](https://github.com/gotm-model/cases/tree/master/seagrass) |
| **wave_breaking** | Idealized | Surface wave breaking | Wave-enhanced turbulence | [View](https://github.com/gotm-model/cases/tree/master/wave_breaking) |

### 15.3 Case Categories

**Idealized Process Studies:**
- `couette`: Fundamental turbulence
- `entrainment`: Mixed layer physics
- `estuary`: Density-driven circulation
- `channel`: Tidal dynamics
- `plume`: Convection
- `reynolds`: Stress anisotropy
- `rouse`: Sediment transport
- `wave_breaking`: Wave-turbulence interaction
- `langmuir`: Langmuir circulation
- `seagrass`: Vegetation effects

**Realistic Ocean/Lake Scenarios:**
- `ows_papa`: Open ocean (North Pacific)
- `nns_annual`, `nns_seasonal`: Temperate shelf sea (North Sea)
- `liverpool_bay`: Coastal/estuarine (Irish Sea)
- `medsea_east`, `medsea_west`: Mediterranean
- `gotland`: Semi-enclosed sea (Baltic)
- `blacksea`: Anoxic basin
- `lago_maggiore`: Deep lake
- `resolute`: Ice-covered waters (Arctic)
- `flex`: Fladen Ground Experiment 1976 (North Sea)

### 15.4 Using Test Cases

**Basic workflow:**
```bash
cd cases/nns_annual
gotm
```

Output: `result.nc` (NetCDF file with model results)

**Analysis:**
```bash
ncdump -h result.nc    # View metadata
ncview result.nc       # Visual inspection
```

**Python analysis:**
```python
import netCDF4 as nc
import matplotlib.pyplot as plt

ds = nc.Dataset('result.nc')
temp = ds.variables['temp'][:]  # [time, z]
z = ds.variables['z'][:]
time = ds.variables['time'][:]

plt.contourf(time, z, temp.T, levels=20)
plt.colorbar(label='Temperature (°C)')
plt.xlabel('Time (days)')
plt.ylabel('Depth (m)')
plt.title('Temperature Evolution')
plt.show()
```

### 15.5 Creating Custom Cases

1. Copy an existing case as template
2. Modify `gotm.yaml` for your scenario
3. Provide forcing files in correct format
4. Adjust `output.yaml` for desired diagnostics
5. Run: `gotm`

**Tips:**
- Start with idealized cases to understand model behavior
- Use realistic cases for model validation
- Combine with FABM for biogeochemical studies
- Experiment with different turbulence closures

### 15.6 Case Figures (Future)

Visualization figures for each case will be available at:
https://github.com/gotm-model/gotm-model-hugo/tree/master/static/cases/img

These will show typical results including:
- Temperature/salinity evolution
- Mixed layer depth
- Turbulent kinetic energy
- Stratification metrics
- Comparison with observations (where applicable)

---

## 16. Publications

GOTM has been extensively used and validated in the scientific literature. Below is a comprehensive list of publications using or describing GOTM, organized chronologically.

### 16.1 GOTM Core Development and Theory

**Foundational Papers:**

1. **Burchard & Baumert (1995)**: "On the performance of a mixed-layer model based on the κ-ε turbulence closure." *J. Geophys. Res. Oceans*, 100(C5), 8523-8540. [DOI](https://doi.org/10.1029/94JC03229)

2. **Burchard et al. (1998a)**: "Comparing the performance of the Mellor-Yamada and the κ-ε two-equation turbulence models." *J. Geophys. Res. Oceans*, 103(C5), 10543-10554. [DOI](https://doi.org/10.1029/98JC00261)

3. **Burchard & Petersen (1999)**: "Models of turbulence in the marine environment—a comparative study of two-equation turbulence models." *J. Mar. Syst.*, 21(1-4), 29-53. [DOI](https://doi.org/10.1016/S0924-7963(99)00004-4)

**Key GOTM Theory:**

4. **Burchard & Bolding (2001)**: "Comparative analysis of four second-moment turbulence closure for the oceanic mixed layer." *J. Phys. Oceanogr.*, 31, 1943-1968. [DOI](http://dx.doi.org/doi:10.1175/1520-0485(2001)031%3C1943:CAOFSM%3E2.0.CO;2)
   - Landmark comparison of turbulence models in GOTM

5. **Burchard (2001)**: "On the q²l equation by Mellor and Yamada (1982)." *J. Phys. Oceanogr.*, 31(5), 1377-1387. [DOI](https://doi.org/10.1175/1520-0485(2001)031%3C1377:OTQLEB%3E2.0.CO;2)

6. **Umlauf & Burchard (2003)**: "A generic length-scale equation for geophysical turbulence models." *J. Marine Research*, 61, 235-265. [DOI](http://dx.doi.org/doi:10.1357/002224003322005087)
   - Generic Length Scale (GLS) framework unifying k-ε, k-ω, MY models

7. **Umlauf & Burchard (2005)**: "Second-order turbulence closure models for geophysical boundary layers. A review of recent work." *Cont. Shelf Res.*, 25, 795-827. [DOI](http://dx.doi.org/doi:10.1016/j.csr.2004.08.004)
   - Comprehensive review of closure schemes

8. **Burchard et al. (2006)**: "Description of a flexible and extendable physical-biogeochemical model system for the water column." *J. Marine Systems*, 61, 180-211. [DOI](http://dx.doi.org/doi:10.1016/j.jmarsys.2005.04.011)
   - GOTM architecture and FABM coupling

**Recent Core Advances:**

9. **Li et al. (2021)**: "Integrating CVMix into GOTM (v6.0): A consistent framework for testing, comparing, and applying ocean mixing schemes." *Geosci. Model Devel.*, 14, 4261-4282. [DOI](https://doi.org/10.5194/gmd-14-4261-2021)
   - CVMix integration, Langmuir turbulence

### 16.2 Selected Applications (2020-2025)

**2025:**

10. Peng et al. (2025): "Interactions between diurnal warm layers and surface-layer fronts." *J. Geophys. Res. Oceans*, 130(1), e2024JC021380. [DOI](https://doi.org/10.1029/2024JC021380)

11. Miracca-Lage et al. (2025): "Turbulence observations and energetics of diurnal warm layers." *J. Phys. Oceanogr.*, 55(11), 2141-2158. [DOI](https://doi.org/10.1175/JPO-D-25-0026.1)

12. Feldbauer et al. (2025): "Learning from a large-scale calibration effort of multiple lake temperature models." *Hydrol. Earth Syst. Sci.*, 29(4), 1183-1199. [DOI](http://dx.doi.org/10.5194/hess-29-1183-2025)

**2024:**

13. Schmitt et al. (2024): "Diurnal warm layers in the ocean: Energetics, nondimensional scaling, and parameterization." *J. Phys. Oceanogr.*, 54(4), 1037-1055. [DOI](https://doi.org/10.1175/JPO-D-23-0129.1)

14. Mesman et al. (2024): "Timing of spring events changes under modelled future climate scenarios in a mesotrophic lake." *Hydrol. Earth Syst. Sci.*, 28(8), 1791-1802. [DOI](http://dx.doi.org/10.5194/hess-28-1791-2024)

15. Shikhani et al. (2024): "Combining a multi-lake model ensemble and a multi-domain CORDEX climate data ensemble for assessing climate change impacts on Lake Sevan." *Water Resources Res.*, 60(11), e2023WR036511. [DOI](https://doi.org/10.1029/2023WR036511)

**2023:**

16. Umlauf et al. (2023): "Hydrodynamic control of sediment-water fluxes: Consistent parameterization and impact in coupled benthic-pelagic models." *J. Geophys. Res. Oceans*, 128(6), e2023JC019651. [DOI](https://doi.org/10.1029/2023JC019651)

17. Burchard et al. (2023): "Decomposition of estuarine circulation and residual stratification under landfast sea ice." *J. Phys. Oceanogr.*, 53(1), 57-80. [DOI](https://doi.org/10.1175/JPO-D-22-0088.1)

18. Clayer et al. (2023): "Sources of skill in lake temperature, discharge and ice-off seasonal forecasting tools." *Hydrol. Earth Syst. Sci.*, 27(6), 1361-1381. [DOI](https://doi.org/10.5194/hess-27-1361-2023)

**2022:**

19. Burchard et al. (2022): "The vertical structure and entrainment of subglacial melt water plumes." *J. Adv. Model. Earth Syst.*, 14(3), e2021MS002925. [DOI](https://doi.org/10.1029/2021MS002925)

20. Golub et al. (2022): "A framework for ensemble modelling of climate change impacts on lakes worldwide: the ISIMIP Lake Sector." *Geosci. Model Devel.*, 15, 4597-4623. [DOI](https://doi.org/10.5194/gmd-15-4597-2022)

21. Feldbauer et al. (2022): "Ensemble of models shows coherent response of a reservoir's stratification and ice cover to climate warming." *Aquatic Sci.*, 84(4), 50. [DOI](http://dx.doi.org/10.1007/s00027-022-00883-2)

**2021:**

22. Moore et al. (2021): "LakeEnsemblR: An R package that facilitates ensemble modelling of lakes." *Environ. Modell. Software*, 143, 105101. [DOI](http://dx.doi.org/10.1016/j.envsoft.2021.105101)

23. Mercado-Bettín et al. (2021): "Forecasting water temperature in lakes and reservoirs using seasonal climate prediction." *Water Res.*, 201, 117286. [DOI](https://doi.org/10.1016/j.watres.2021.117286)

24. Woolway et al. (2021): "Phenological shifts in lake stratification under climate change." *Nature Comm.*, 12(1), 2318. [DOI](https://doi.org/10.1038/s41467-021-22657-4)

### 16.3 Ocean Modeling Applications

**Turbulence and Mixing:**

25. Li et al. (2019): "Comparing ocean surface boundary vertical mixing schemes including Langmuir turbulence." *J. Adv. Model. Earth Syst.*, 11(11), 3545-3592. [DOI](https://doi.org/10.1029/2019MS001810)

26. Reichl & Hallberg (2018): "A simplified energetics based planetary boundary layer (ePBL) approach for ocean climate simulations." *Ocean Modell.*, 132, 112-129. [DOI](https://doi.org/10.1016/j.ocemod.2018.10.004)

27. Reichl et al. (2016): "Langmuir turbulence parameterization in tropical cyclone conditions." *J. Phys. Oceanogr.*, 46(3), 863-886. [DOI](http://dx.doi.org/10.1175/JPO-D-15-0106.1)

**Estuarine Dynamics:**

28. Burchard & Hetland (2010): "Quantifying the contributions of tidal straining and gravitational circulation to residual circulation in periodically stratified tidal estuaries." *J. Phys. Oceanogr.*, 40, 1243-1262. [DOI](http://dx.doi.org/10.1175/2010JPO4270.1)

29. Burchard (2009): "Combined effects of wind, tide and horizontal density gradients on stratification in estuaries and coastal seas." *J. Phys. Oceanogr.*, 39, 2117-2136. [DOI](http://dx.doi.org/doi:10.1175/2009JPO4142.1)

30. Lange & Burchard (2019): "The relative importance of wind straining and gravitational forcing in driving exchange flows in tidally energetic estuaries." *J. Phys. Oceanogr.*, 49(3), 723-736. [DOI](https://doi.org/10.1175/JPO-D-18-0014.1)

### 16.4 Lake and Reservoir Studies

31. Mesman et al. (2020): "Performance of one-dimensional hydrodynamic lake models during short-term extreme weather events." *Environ. Modell. Software*, 133, 104852. [DOI](http://dx.doi.org/10.1016/j.envsoft.2020.104852)

32. Ayala et al. (2020): "Simulations of future changes in thermal structure of Lake Erken: proof of concept for ISIMIP2b lake sector local simulation strategy." *Hydrol. Earth Syst. Sci.*, 24(6), 3311-3330. [DOI](http://dx.doi.org/10.5194/hess-24-3311-2020)

33. Andersen et al. (2020): "Predicting ecosystem state changes in shallow lakes using an aquatic ecosystem model: Lake Hinge, Denmark, an example." *Ecological Applications*, 30(7), e2160. [DOI](http://dx.doi.org/10.1002/eap.2160)

### 16.5 Biogeochemistry and Ecosystems

34. Bruggeman & Bolding (2014): "A general framework for aquatic biogeochemical models." *Environmental Modelling and Software*, 61, 249-265. [DOI](http://dx.doi.org/10.1016/j.envsoft.2014.04.002)
   - FABM framework description

35. Wirtz et al. (2022): "Vertically migrating phytoplankton fuel high oceanic primary production." *Nature Clim. Change*, 12(8), 750-756. [DOI](https://doi.org/10.1038/s41558-022-01430-5)

36. Yakushev et al. (2011): "Modeling of influence of oxygenated inflows on biogeochemical structure of the Gotland Sea, central Baltic Sea: changes in distribution of manganese." *Computers and Geosciences*, 37, 398-409. [DOI](http://dx.doi.org/doi:10.1016/j.marchem.2009.09.007)

### 16.6 Arctic and Sea Ice

37. Mortenson et al. (2017): "A model-based analysis of physical and biological controls on ice algal and pelagic primary production in Resolute Passage." *Elem Sci Anth*, 5, e229. [DOI](http://dx.doi.org/10.1525/elementa.229)

38. Hayashida et al. (2017): "Implications of sea-ice biogeochemistry for oceanic production and emissions of dimethyl sulfide in the Arctic." *Biogeosciences*, 14, 3129-3155. [DOI](http://dx.doi.org/10.5194/bg-14-3129-2017)

39. Abraham et al. (2015): "Effects of subgrid-scale snow thickness variability on radiative transfer in sea ice." *J. Geophys. Res. Oceans*, 120, 5597-5614. [DOI](http://dx.doi.org/10.1002/2015JC010741)

### 16.7 Numerical Methods

40. Burchard (2002): "Energy-conserving discretisation of turbulent shear and buoyancy production." *Ocean Modell.*, 4(3-4), 347-361. [DOI](https://doi.org/10.1016/S1463-5003(02)00009-4)

41. Burchard et al. (2003): "A high-order conservative Patankar-type discretisation for stiff systems of production-destruction equations." *Appl. Numer. Math.*, 47(1), 1-30. [DOI](https://doi.org/10.1016/S0168-9274(03)00101-6)

42. Burchard & Beckers (2004): "Non-uniform adaptive vertical grids in one-dimensional numerical ocean models." *Ocean Modell.*, 6(1), 51-81. [DOI](https://doi.org/10.1016/S1463-5003(02)00060-4)

### 16.8 Complete Publication List

For the complete and continuously updated list of GOTM publications, see:
**https://gotm.net/html/gotm_pub.html**

This list includes over 135 peer-reviewed publications spanning:
- Turbulence theory and parameterization
- Ocean and coastal modeling
- Lake and reservoir dynamics
- Biogeochemistry and ecosystems
- Climate change impacts
- Numerical methods
- Arctic and sea ice
- Sediment dynamics

The diversity of applications demonstrates GOTM's versatility and the trust the scientific community places in its turbulence schemes.

---

## Appendix A: Quick Reference

### A.1 Common Turbulence Configurations

**Standard k-ε:**
```yaml
turbulence:
  turb_method: 2
  tke_method: 2
  len_scale_method: 8
  scnd_method: 1
  stab_method: 1
```

**Mellor-Yamada 2.5:**
```yaml
turbulence:
  turb_method: 2
  tke_method: 3
  len_scale_method: 9
  GLS_p: 0.0
  GLS_m: 1.0
  GLS_n: 1.0
```

**k-ω:**
```yaml
turbulence:
  turb_method: 2
  tke_method: 2
  len_scale_method: 9
  GLS_p: -1.0
  GLS_m: 0.5
  GLS_n: -1.0
```

**KPP:**
```yaml
turbulence:
  turb_method: 99
```

**CVMix with Langmuir:**
```yaml
turbulence:
  turb_method: 100
```

### A.2 Essential Files

- `gotm.yaml`: Main configuration
- `output.yaml`: Output specification
- `fabm.yaml`: Biogeochemistry (if FABM enabled)
- `kpp.inp`: KPP parameters (if using KPP)
- `result.nc`: Default output file

### A.3 Useful Commands

```bash
# Check version
gotm --version

# Validate configuration
gotm --check

# Generate template configuration
gotm --write_yaml

# Run simulation
gotm

# Run with specific config
gotm --config my_setup.yaml
```

### A.4 Python Analysis Template

```python
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np

# Load data
ds = nc.Dataset('result.nc')
temp = ds.variables['temp'][:]  # [time, depth]
z = ds.variables['z'][:]
time = nc.num2date(ds.variables['time'][:], 
                   ds.variables['time'].units)

# Hovmöller diagram
fig, ax = plt.subplots(figsize=(10, 6))
cf = ax.contourf(time, z, temp.T, levels=20, cmap='RdYlBu_r')
plt.colorbar(cf, label='Temperature (°C)')
ax.set_xlabel('Time')
ax.set_ylabel('Depth (m)')
ax.invert_yaxis()
plt.title('Temperature Evolution')
plt.tight_layout()
plt.show()
```

---

## Appendix B: Troubleshooting

**Problem:** CMake cannot find NetCDF  
**Solution:** Set `NetCDF_ROOT` environment variable or install `libnetcdff-dev`

**Problem:** Submodules not initialized  
**Solution:** `git submodule update --init --recursive`

**Problem:** Compiler mismatch errors  
**Solution:** Ensure NetCDF and GOTM use same Fortran compiler

**Problem:** NaN values in output  
**Solution:** Check timestep (CFL condition), initial conditions, forcing data

**Problem:** Test case won't run  
**Solution:** Verify you're on `master` branch, update submodules

---

**Document Version:** 3.0 (Complete Integrated Edition)  
**Based on:** GOTM `master` branch (development version, February 2026)  
**Last Updated:** February 13, 2026

**Changes in Version 3.0:**
- Added authors and contributors
- New Section 4: Equation of State and TEOS-10
- New Section 6: Numerical Methods
- Enhanced air-sea interaction with Kondo and multiple longwave formulations
- Updated equation of state (UNESCO/Jackett marked as legacy, not in dev version)
- Corrected grid arrangement diagram
- Added GitHub Actions and contribution information
- Comprehensive links to references (DOI links added)
- Cross-platform conda instructions
- GOTM command-line options documented
- Scalar input file example added
- FLEX case corrected (Fladen Ground Experiment)
- Bolding & Bruggeman affiliation corrected

**Notes:**
- This documentation describes the `master` (development) branch
- For maximum stability, consider tagged releases (e.g., v6.0.7)
- Test cases require `master` branch
- Submodule updates are critical - always run `git submodule update` after `git pull`

**Contacts and Contributions:**
- **Website:** https://gotm.net
- **Code Repository:** https://github.com/gotm-model/code
- **Issues & Bug Reports:** https://github.com/gotm-model/code/issues
- **Discussions:** https://github.com/gotm-model/code/discussions
- **Contributing:** Contributions via pull requests on GitHub are welcome

**Quality Control:**
- GOTM uses [GitHub Actions](https://github.com/gotm-model/code/actions) extensively for continuous integration
- Automated testing on multiple platforms (Linux, macOS, Windows)
- Code quality checks and regression testing
- All pull requests undergo automated testing before merge

**Acknowledgments:**
GOTM development has been supported by numerous research projects and institutions over three decades. Core developers include Hans Burchard, Karsten Bolding, Lars Umlauf, Jorn Bruggeman, and many contributors worldwide.

---

*End of Documentation*
