---
title: "Turbulence Module"
weight: 30
bookToc: true
---

# Turbulence Module

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