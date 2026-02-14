---
title: "Air-Sea Interaction"
weight: 20
bookToc: true
---

# Air-Sea Interaction

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