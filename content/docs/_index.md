---
title: "GOTM Documentation"
weight: 1
bookFlatSection: false
bookToc: true
---

# GOTM - General Ocean Turbulence Model

**Authors:**  
Karsten Bolding¹, Hans Burchard², Lars Umlauf², Jorn Bruggeman³

**Contributors:**  
Knut Klingbeil², Qing Li⁴, and many others worldwide

¹ Bolding & Bruggeman, Denmark  
² Leibniz Institute for Baltic Sea Research Warnemünde (IOW), Germany  
³ National Oceanography Centre, UK  
⁴ Los Alamos National Laboratory, USA

---

**Repository:** https://github.com/gotm-model/code  
**Development Branch:** `master` (actively developed, recommended)  
**Stable Releases:** Tagged versions (e.g., `v6.0.7`)  
**License:** GPL-2.0  
**Language:** Fortran (84.2%), C, CMake, Python  
**Latest Stable Release:** v6.0.7 (July 2024)  
**Official Website:** https://gotm.net

> **Important:** This documentation describes the `master` branch, which is the main development branch. Stable releases use version tags. For most applications and all test cases, use the `master` branch.

---

## Overview

GOTM (General Ocean Turbulence Model) is a one-dimensional water column model for marine and limnological applications. It simulates vertical transport of momentum, heat, salt, and tracers, coupled with state-of-the-art turbulence parameterizations. Since the mid-1990s, GOTM has become one of the most widely used turbulence models in aquatic science.

The model excels at:
- Process studies isolating vertical mixing physics
- Validation of turbulence closure schemes
- Rapid testing of scenarios and sensitivity analyses
- Biogeochemical modeling in stratified waters
- Providing turbulence schemes for 3D circulation models

### Key Features

- **Comprehensive turbulence library**: From simple zero-equation models to sophisticated second-moment closures
- **Modular design**: Clean separation of physics (meanflow, turbulence, airsea, biogeochemistry)
- **Modern configuration**: YAML-based setup replacing legacy namelists
- **Flexible output**: Integrated flexout system with time-averaging and interpolation operators
- **Biogeochemical coupling**: Seamless [FABM](https://fabm.net) integration for ecosystem modeling
- **3D model integration**: Used in [FVCOM](http://fvcom.smast.umassd.edu/), [TELEMAC](http://www.opentelemac.org/), [GETM](https://getm.eu), [NEMO](https://www.nemo-ocean.eu/), and others
- **Git submodules**: Clean dependency management (FABM, CVMix, flexout, STIM)

### Primary State Variables

- Horizontal velocities: U(z,t), V(z,t)
- Temperature: T(z,t)
- Salinity: S(z,t)
- Turbulent kinetic energy: k(z,t)
- Dissipation rate or length scale: ε(z,t) or L(z,t)
- Optional tracers via [FABM](https://fabm.net)
- Optional ice properties via STIM (Simple Thermodynamic Ice Models)

Horizontal gradients must be prescribed, making GOTM ideal for one-dimensional process studies.

---

## Quick Links

- [Getting Started](getting-started/) - Installation and first simulation
- [Theory](theory/) - Governing equations and turbulence closures
- [User Guide](user-guide/) - Configuration and running simulations
- [Modules](modules/) - Core GOTM modules explained
- [Test Cases](test-cases/) - Example simulations
- [Reference](reference/) - Publications and API reference

---

## Community

- **Code Repository:** https://github.com/gotm-model/code
- **Issues & Bug Reports:** https://github.com/gotm-model/code/issues
- **Discussions:** https://github.com/gotm-model/code/discussions
- **Contributing:** Contributions via pull requests on GitHub are welcome

GOTM uses [GitHub Actions](https://github.com/gotm-model/code/actions) extensively for continuous integration, with automated testing on multiple platforms (Linux, macOS, Windows).
