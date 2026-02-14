---
title: "Medsea West"
weight: 10
bookToc: true
---

# Medsea West

Western Mediterranean - Wind mixing, seasonal thermocline

## Overview

**Repository:** [cases/medsea_west](https://github.com/gotm-model/cases/tree/master/medsea_west)

## Running the Case

```bash
cd cases/medsea_west
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
