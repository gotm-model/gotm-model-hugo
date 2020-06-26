+++
title = "CVMix module"
draft = false
author = "Qing Li"
date = "2020-06-22T19:59:15-06:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

CVMix is now included GOTM, bringing more options of turbulence closures including KPP and its variants with Langmuir turbulence.


<!--more-->

The Community Vertical Mixing Project ([CVMix](http://cvmix.github.io)) is a portable vertical mixing software package providing an extensible framework for the development of first-order closures. Currently it includes subroutines allowing the surface and interior turbulent mixing closures in the K-profile parameterization (KPP, [Large et al., 1994](https://doi.org/10.1029/94RG01872)), as well as a few KPP variants that include the effects of Langmuir turbulence (e.g., [Li et al., 2016](https://doi.org/10.1016/j.ocemod.2015.07.020), [Reichl et al., 2016](https://doi.org/10.1175/JPO-D-15-0106.1) and [Li and Fox-Kemper, 2017](https://doi.org/10.1175/JPO-D-17-0085.1)).

Following the efforts of [Li et al., 2019](https://doi.org/10.1029/2019MS001810), CVMix is now included in GOTM as a submodule with an interface enabling KPP and its Langmuir turbulence variants. The CVMix module is enabled by building GOTM with the CMake flag `-DGOTM_USE_CVMIX=true` and using `turb_method=100` in the GOTM configuration file. It includes an interface `do_cvmix()` separate from `do_turbulence()` which assembles the CVMix subroutines to do KPP.


KPP in CVMix (KPP-CVMix) is compared with the generic length scale model (GLS; [Umlauf and Burchard, 2003](https://doi.org/10.1357/002224003322005087)) in the k-epsilon formulation with the weak-equilibrium stability function by [Canuto et al., 2001](https://doi.org/10.1175/1520-0485(2001)031%3C1413:OTPIOP%3E2.0.CO;2) (GLS-C01A) using the [Gotland Deep](https://gotm.net/cases/gotland_deep/) test case. The figure below shows a seasonal cycle of the simulated temperature in the two cases.

{{< figure src="../gotland_cvmix.png" width="100%" >}}



