---
title: "Equation of State & TEOS-10"
weight: 30
bookToc: true
---

# Equation of State and TEOS-10

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