---
title: "Installation"
weight: 10
bookToc: true
---

# Installation

### 14.1 Quick Start

```bash
# Clone repository
git clone --recurse-submodules https://github.com/gotm-model/code.git
cd code

# Configure
cmake -G Ninja -B build -S .

# Compile
cmake --build build

# Install (optional)
cmake --install build --prefix ~/.local
```

### 14.2 Platform-Specific

**Linux:**
```bash
sudo apt-get install gfortran cmake ninja-build libnetcdff-dev
cmake -G Ninja -B build
cmake --build build
```

**macOS:**
```bash
brew install gcc cmake ninja netcdf
cmake -G Ninja -B build
cmake --build build
```

**Windows:**
- Intel Fortran + Visual Studio
- Pre-built NetCDF included

### 14.3 Updating

```bash
git pull
git submodule update --init --recursive
cmake --build build
```

**Critical:** `git pull` alone does NOT update submodules.

---
EOFMARKER