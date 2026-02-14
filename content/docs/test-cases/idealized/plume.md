---
title: "Plume"
weight: 10
bookToc: true
---

# Plume

Buoyant plume dynamics - Convection and density-driven flow

## Overview

**Repository:** [cases/plume](https://github.com/gotm-model/cases/tree/master/plume)

## Running the Case

```bash
cd cases/plume
gotm
```

Output: `result.nc`

## Configuration Highlights

See `gotm.yaml` in the case directory for complete configuration.

## Expected Results

Examine temperature, velocity, and turbulence evolution in `result.nc`.

## Analysis

```python
import netCDF4 as nc
import matplotlib.pyplot as plt

ds = nc.Dataset('result.nc')
# Add your analysis here
```

## Further Reading

See [theory section](../../theory/) for background on the physics simulated in this case.
