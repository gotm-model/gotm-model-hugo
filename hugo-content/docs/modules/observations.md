---
title: "Observations Module"
weight: 50
bookToc: true
---

# Observations Module

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