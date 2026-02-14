---
title: "Dependencies"
weight: 20
bookToc: true
---

# Dependencies

### 10.1 CMake Configuration

```bash
cmake -G Ninja -B build -S . [OPTIONS]
```

**Options:**
- `-DGOTM_USE_FABM=ON`: Enable biogeochemistry
- `-DGOTM_USE_STIM=ON`: Enable ice
- `-DGOTM_USE_CVMIX=ON`: Enable CVMix turbulence
- `-DGOTM_USE_NetCDF=ON`: NetCDF output (default ON)
- `-DGOTM_USE_SEAGRASS=ON`: Seagrass module

### 10.2 Required Dependencies

**Fortran Compiler:**
- Fortran 2003 support minimum
- gfortran ≥ 4.7, Intel Fortran, or similar
- **Critical:** NetCDF and GOTM must use same compiler on Linux/Mac

**NetCDF:**
- NetCDF with Fortran support (libnetcdff)
- Ubuntu/Debian: `apt-get install libnetcdff-dev`
- Pre-built Windows libraries included in repo

**Build Tools:**
- CMake ≥ 3.0
- Ninja (recommended) or Make

### 10.3 Conda Environment (Cross-Platform: Windows, Linux, macOS)

Conda provides a complete environment with all dependencies. **This works identically on Windows, Linux, and macOS.**

**Install Miniconda:**
- Download from: https://docs.conda.io/en/latest/miniconda.html
- Follow platform-specific installation instructions

**Create and use GOTM environment:**
```bash
# Navigate to GOTM source directory
cd /path/to/gotm/code

# Create environment from file
conda env create -f environment.yml

# Activate environment
conda activate gfortran
```

**Configure and compile (same commands on all platforms):**
```bash
# Configure with CMake
cmake -G Ninja -B build -S .

# Compile
cmake --build build

# Install (optional)
cmake --install build --prefix ~/.local
```

The conda environment provides:
- gfortran compiler
- CMake and Ninja build tools
- NetCDF libraries with Fortran support
- Python tools for analysis

**Advantages:**
- Consistent across platforms
- No manual dependency installation
- Isolated from system packages
- Easy to reproduce

---