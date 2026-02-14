---
title: "Architecture"
weight: 10
bookToc: true
---

# Architecture

### 7.1 Git Submodules and External Dependencies

GOTM uses Git submodules in `extern/` for modular integration of external libraries. Each submodule is a full clone of its repository, enabling independent development cycles and easy updates.

#### Core Submodules:

**1. yaml-cpp** (`extern/yaml`)
- Purpose: YAML 1.2 parser (C++)
- Function: Parses `gotm.yaml`, `output.yaml`, `fabm.yaml`
- Repository: https://github.com/jbeder/yaml-cpp
- Impact: Enables modern, human-readable configuration

**2. field_manager** (`extern/field_manager`)
- Purpose: Central variable registry with metadata
- Function: 
  - Variable registration with units, long names, CF standard names
  - Attribute system for variable properties
  - Hotstart/restart (variables tagged with `state` attribute saved to `restart.nc`)
  - Coordinates I/O with flexout
- Always required

**3. flexout** (`extern/flexout`)
- Purpose: Flexible output manager with operators
- Integrated: January 2019
- Function:
  - Time-averaging (mean, integrated, instantaneous)
  - Spatial interpolation (sigma → z-coordinates)
  - Multiple output files with different resolutions
  - Custom derived fields
- Configured via `output.yaml`
- Dramatically reduces post-processing needs

**4. FABM** (`extern/fabm`)
- Purpose: Framework for Aquatic Biogeochemical Models
- Repository: https://github.com/fabm-model/fabm
- CMake flag: `-DGOTM_USE_FABM=ON`
- Function:
  - BGC model library (ERSEM, NPZD, ECOSMO, etc.)
  - Pelagic and benthic state variables
  - Feedback to physics (shading, albedo, drag)
- Configuration: `fabm.yaml` + `gotm.yaml` (coupling settings)
- No longer requires manual `FABM_BASE` path

**5. CVMix** (`extern/cvmix`)
- Purpose: Community Ocean Vertical Mixing library
- Repository: [CVMix on GitHub](https://github.com/CVMix/CVMix-src)
- CMake flag: `-DGOTM_USE_CVMIX=ON`
- Configuration: `turb_method: 100` in `gotm.yaml`
- Function:
  - KPP with Langmuir turbulence (Li et al., 2019)
  - Tidal mixing, double diffusion
  - Shear instability, internal wave breaking
- Interface: `do_cvmix()` called alongside `do_turbulence()`

**6. STIM** (`extern/stim`)
- Purpose: Simple Thermodynamic Ice Models
- CMake flag: `-DGOTM_USE_STIM=ON`
- Ice models:
  - Model 1: Lebedev (1938)
  - Model 2: MyLake
  - Model 3: Winton (in development)
- Effects: Ice formation/melting, modified surface fluxes, radiation penetration

#### Submodule Management:

```bash
# Clone with submodules
git clone --recurse-submodules https://github.com/gotm-model/code.git

# Update existing clone
git pull
git submodule update --init --recursive

# Initialize specific submodule
git submodule update --init extern/fabm
```

Benefits:
- No manual path configuration
- Independent component updates
- Shared across GOTM, GETM, 3D models
- Reduces maintenance burden

### 7.2 Modular Source Code Structure

```
gotm (main executable)
├── airsea (surface forcing)
├── meanflow (momentum, T, S)
├── turbulence (closures)
├── observations (data input)
├── output (NetCDF via flexout)
├── util (utilities)
└── extras (seagrass, optional modules)
```

### 7.3 Main Program Flow

1. **init_gotm()**: Parse YAML, initialize modules, setup grid, initial conditions
2. **time_loop()**: 
   - Update forcing
   - Solve momentum equations
   - Apply turbulence closure
   - Solve T/S equations
   - Update FABM (if enabled)
   - Write output
3. **clean_up()**: Close files, deallocate

---