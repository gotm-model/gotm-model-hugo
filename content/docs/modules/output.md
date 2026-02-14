---
title: "Output Module"
weight: 60
bookToc: true
---

# Output Module

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