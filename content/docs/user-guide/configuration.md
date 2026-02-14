---
title: "Configuration"
weight: 10
bookToc: true
---

# Configuration System

### 11.1 YAML Configuration

Main file: `gotm.yaml`

**Version requirement:**
```yaml
version: 7  # configuration schema version
```

Legacy configs without version trigger error with auto-update instructions.

### 11.2 Key Configuration Sections

**For a complete, working example, see:**  
**[nns_annual/gotm.yaml](https://github.com/gotm-model/cases/blob/master/nns_annual/gotm.yaml)**

This demonstrates a realistic North Sea simulation with full time/location setup, turbulence configuration (k-ε), and surface forcing from files.

**Location:**
```yaml
location:
  name: 'Station Name'
  latitude: 57.0
  longitude: 10.0
  depth: 50.0
```

**Time:**
```yaml
time:
  start: '2020-01-01 00:00:00'
  stop: '2020-12-31 23:00:00'
  dt: 3600.0  # seconds
```

**Grid:**
```yaml
grid:
  nlev: 100
  method: 0  # 0=analytical, 1=file_sigma, 2=file_h
  ddu: 0.0   # surface zooming
  ddl: 0.0   # bottom zooming
```

**Turbulence:**
```yaml
turbulence:
  turb_method: 2
  tke_method: 2
  len_scale_method: 8
  scnd_method: 1
  stab_method: 1
```

**Surface Fluxes:**
```yaml
surface:
  fluxes:
    heat:
      method: 2  # from file
    tx:
      method: 2
    ty:
      method: 2
```

### 11.3 GOTM Command-Line Interface

**Basic usage:**
```bash
gotm [options]
```

**Writing YAML configuration:**

GOTM can generate template YAML files:

```bash
# Create gotm.yaml with default settings
gotm --write_yaml

# Create all configuration files
gotm --write_yaml --write_schema
```

This creates:
- `gotm.yaml` - main configuration
- `output.yaml` - output specification  
- Schema files for validation

**Custom configuration file:**
```bash
# Use specific config file
gotm --config my_setup.yaml
```

**Help and version:**
```bash
# Display help
gotm --help

# Show version
gotm --version

# Check configuration without running
gotm --check
```

**Advanced options:**
```bash
# Increase verbosity
gotm --verbose

# Dry run (test setup without running)
gotm --dry-run
```

**Typical workflow:**
```bash
# 1. Create template
gotm --write_yaml

# 2. Edit gotm.yaml for your case
nano gotm.yaml

# 3. Check configuration
gotm --check

# 4. Run simulation
gotm
```

---