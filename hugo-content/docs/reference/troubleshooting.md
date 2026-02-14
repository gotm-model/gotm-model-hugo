---
title: "Troubleshooting"
weight: 30
bookToc: true
---

# Troubleshooting

**Problem:** CMake cannot find NetCDF  
**Solution:** Set `NetCDF_ROOT` environment variable or install `libnetcdff-dev`

**Problem:** Submodules not initialized  
**Solution:** `git submodule update --init --recursive`

**Problem:** Compiler mismatch errors  
**Solution:** Ensure NetCDF and GOTM use same Fortran compiler

**Problem:** NaN values in output  
**Solution:** Check timestep (CFL condition), initial conditions, forcing data

**Problem:** Test case won't run  
**Solution:** Verify you're on `master` branch, update submodules