---
title: "Governing Equations"
weight: 10
bookToc: true
---

# Governing Equations

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