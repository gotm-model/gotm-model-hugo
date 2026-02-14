---
title: "Input Files"
weight: 20
bookToc: true
---

# Input Files

### 12.1 Input Formats

**Meteorological forcing:**
```
YYYY-MM-DD HH:MM:SS  u10  v10  airp  airt  hum  cloud
```

**Profile data:**
```
YYYY-MM-DD HH:MM:SS  nlev  direction
depth1  value1
depth2  value2
...
```

**Scalar time series (e.g., external pressure gradient):**
```
# External pressure gradient forcing
# Format: YYYY-MM-DD HH:MM:SS  dpdx  dpdy
# Units: dpdx, dpdy in Pa/m

1990-01-01 00:00:00  0.0000E+00  0.0000E+00
1990-01-01 06:00:00  1.2500E-06  3.4500E-07
1990-01-01 12:00:00  2.1000E-06  1.5000E-07
1990-01-01 18:00:00  8.5000E-07 -2.1000E-07
1990-01-02 00:00:00 -5.0000E-07 -8.0000E-07
```

**Example file:** [nns_annual/ext_press_file.dat](https://github.com/gotm-model/cases/blob/master/nns_annual/ext_press_file.dat)

**Format notes:**
- Lines starting with `#` are comments
- Date/time in `YYYY-MM-DD HH:MM:SS` format
- Space-separated values
- Scientific notation allowed
- Linear interpolation between times

### 12.2 NetCDF Output

CF-1.6 compliant with:
- Unlimited time dimension
- Coordinate variables (z, time, lat, lon)
- Variable metadata (units, long_name, standard_name)

Configured via `output.yaml`:
```yaml
output:
  - file: 'result.nc'
    time_unit: 'hour'
    time_step: 1
    variables:
      - name: 'temp'
        operator: 'mean'
```

---