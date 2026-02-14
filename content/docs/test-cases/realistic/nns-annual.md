---
title: "Nns Annual"
weight: 10
bookToc: true
---

# Nns Annual

Northern North Sea annual - Full seasonal cycle, temperate shelf

## Overview

**Repository:** [cases/nns_annual](https://github.com/gotm-model/cases/tree/master/nns_annual)

## Running the Case

```bash
cd cases/nns_annual
gotm
```

Output: `result.nc`

## Configuration

This case uses realistic forcing data. See files in the case directory:
- `gotm.yaml` - Main configuration
- `*_file.dat` - Forcing data files

## Validation

Compare results with observations or climatology where available.

## Analysis Tips

```python
import netCDF4 as nc
import matplotlib.pyplot as plt

ds = nc.Dataset('result.nc')
temp = ds.variables['temp'][:]
z = ds.variables['z'][:]

# Hovmoller diagram
plt.contourf(temp.T, levels=20)
plt.colorbar(label='Temperature (°C)')
plt.ylabel('Depth (m)')
plt.xlabel('Time')
plt.show()
```

## References

See the [publications](../../reference/publications/) page for papers using this case.
