---
title: "Channel"
weight: 10
bookToc: true
---

# Channel

Tidal channel flow - Periodic forcing and bottom stress

## Overview

**Repository:** [cases/channel](https://github.com/gotm-model/cases/tree/master/channel)

## Running the Case

```bash
cd cases/channel
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
