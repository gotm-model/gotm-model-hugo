---
title: "Numerical Methods"
weight: 50
bookToc: true
---

# Numerical Methods

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