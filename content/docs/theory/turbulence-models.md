---
title: "Turbulence Models (Detailed)"
weight: 60
bookToc: true
---

# Turbulence Models (Detailed)

### 9.1 Generic Length Scale (GLS) Framework

**Governing Equations:**

TKE equation:
```
∂k/∂t = ∂/∂z(νₜ/σₖ ∂k/∂z) + P + B - ε
```

Generic length scale equation:
```
∂ψ/∂t = ∂/∂z(νₜ/σψ ∂ψ/∂z) + ψ/k (c₁P + c₃B - c₂ε F_wall)
```

where ψ = k^m L^n, with (p, m, n) defining specific models.

**Eddy viscosity:**
```
νₜ = Sₘ k^(1/2) L
```

Sₘ is a stability function depending on N² and S².

### 9.2 k-ε Model

Parameters: p=3, m=1.5, n=-1

Constants:
- cε1 = 1.44
- cε2 = 1.92
- cε3minus = -0.52 (stable)
- cε3plus = 1.0 (unstable)
- σₖ = 1.0
- σε = 1.3
- cμ0 = 0.5477

Limitations: Flawed under breaking waves (Umlauf et al., 2003)

### 9.3 k-ω Model

Parameters: p=-1, m=0.5, n=-1

Better for wave breaking scenarios.

### 9.4 Mellor-Yamada 2.5

Parameters: p=0, m=1, n=1

Well-established for boundary layers. Reproduces Monin-Obukhov similarity theory.

Two equations:
- q² (twice TKE)
- q²L (TKE × length scale)

### 9.5 KPP (K-Profile Parameterization)

Non-local boundary layer scheme.

Configuration: `kpp.inp` file
- Surface boundary layer: `kpp_sbl`
- Bottom boundary layer: `kpp_bbl`
- Interior: `kpp_interior`
- Critical Ri: `Ric`

### 9.6 Stability Functions

Multiple formulations available:
- Kantha-Clayson (KC): Default
- Canuto A: Alternative
- Galperin: Classical

Different functions require corresponding closure constants.

---