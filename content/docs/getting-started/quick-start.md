---
title: "Quick Start"
weight: 5
bookToc: true
---

# Quick Start Guide

## Installation in 3 Steps

```bash
# 1. Clone with submodules
git clone --recurse-submodules https://github.com/gotm-model/code.git
cd code

# 2. Configure and build
cmake -G Ninja -B build -S .
cmake --build build

# 3. Install (optional)
cmake --install build --prefix ~/.local
```

## Run Your First Test Case

```bash
# Clone test cases
git clone --recurse-submodules https://github.com/gotm-model/cases.git
cd cases/nns_annual

# Run simulation
gotm

# Output: result.nc
```

## Analyze Results

**Using Python:**
```python
import netCDF4 as nc
import matplotlib.pyplot as plt

# Load data
ds = nc.Dataset('result.nc')
temp = ds.variables['temp'][:]
z = ds.variables['z'][:]

# Plot
plt.contourf(temp.T, levels=20)
plt.colorbar(label='Temperature (°C)')
plt.show()
```

**Using command-line tools:**
```bash
ncdump -h result.nc    # View metadata
ncview result.nc       # Visual inspection (if installed)
```

## Next Steps

- Explore [test cases](../test-cases/) for more examples
- Learn about [configuration](configuration/) options
- Understand the [theory](../theory/) behind GOTM
- Read about [modules](../modules/) for customization

## Getting Help

- Browse [documentation](../)
- Check [GitHub Issues](https://github.com/gotm-model/code/issues)
- Join [GitHub Discussions](https://github.com/gotm-model/code/discussions)
