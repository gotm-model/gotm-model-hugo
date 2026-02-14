---
title: "Meanflow Module"
weight: 20
bookToc: true
---

# Meanflow Module

**Location:** `src/meanflow/`

Handles mean flow dynamics:
- Grid management: `updategrid.F90` (sigma/z-coordinate)
- Coriolis: `coriolis.F90` (rotation effects)
- Momentum: `uequation.F90`, `vequation.F90` (U, V transport with friction)
- Pressure gradients: `extpressure.F90` (barotropic), `intpressure.F90` (baroclinic)
- Vertical velocity: `wequation.F90`

State variables: U, V, T, S, buoyancy, grid spacing