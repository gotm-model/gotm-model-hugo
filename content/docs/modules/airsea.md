---
title: "Air-Sea Module"
weight: 40
bookToc: true
---

# Air-Sea Module

**Location:** `src/airsea/`

Computes surface boundary conditions:
- Momentum flux: Wind stress (Fairall et al. formulation, stability-dependent)
- Heat fluxes: Solar SW, longwave, sensible, latent
- Freshwater: Precipitation, evaporation
- Albedo: Bio-optical effects

Input: Wind (u10, v10), air temp/pressure/humidity, clouds, solar radiation, precipitation