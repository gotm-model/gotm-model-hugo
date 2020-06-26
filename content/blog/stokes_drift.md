+++
title = "Stokes drift"
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

A new Stokes drift module is added. This allows input of Stokes drift and exploration of Langmuir turbulence parameterizations and more in GOTM.

<!--more-->

A Stokes drift module is now added in GOTM, providing a way to include the Stokes drift information in GOTM for use in ocean surface boundary layer turbulence closure schemes. Currently it is used to enable Langmuir turbulence parameterizations in KPP via CVMix. But it supports input of the full vertical profile of Stokes drift and its shear, which allows exploration of Langmuir turbulence parameterizations in various forms and other applications. See [Li et al., 2019](https://doi.org/10.1029/2019MS001810) for some examples.

The Stokes drift module is enabled by default with the Stokes drift set to zero. It provides multiple options to input Stokes drift in GOTM. It introduces the following variables:

- Stokes drift profiles in x- and y-directions (`usprof`, `vsprof`), with input options
  - Read from a file
  - Compute from the input surface value and a decay scale assuming an exponential profile
  - Compute from the input wind using the empirical 'theory wave' approach of [Li et al., 2017](https://doi.org/10.1016/j.ocemod.2017.03.016)
- Stokes drift shear profiles in x- and y-directions (`dusdz`, `dvsdz`), with input options
  - Read from a file
  - Compute from the Stokes drift profile
- Surface value of the Stokes drift in x- and y-directions (`us0`, `vs0`) and a decay scale (`ds`), with input options
  - Constant
  - Read from a file
- (If CVMix is used) A few variants of the turbulent Langmuir number introduced by [McWilliams et al., 1997](https://doi.org/10.1017/S0022112096004375), [Harcourt and D'Asaro, 2008](https://doi.org/10.1175/2007JPO3842.1), [Van Roekel et al., 2012](https://doi.org/10.1029/2011JC007516) and [Reichl et al., 2016](https://doi.org/10.1175/JPO-D-15-0106.1)
- (If CVMix is used) A few variants of the Langmuir enhancement factor introduced by [Li et al., 2016](https://doi.org/10.1016/j.ocemod.2015.07.020) and [Reichl et al., 2016](https://doi.org/10.1175/JPO-D-15-0106.1)

The figure below shows an example of using the Stokes drift module in comparing different variants of Langmuir turbulence parameterizations in KPP ([KPPLT-VR12](https://doi.org/10.1016/j.ocemod.2015.07.020), [KPPLT-LF17](https://doi.org/10.1175/JPO-D-17-0085.1)) and the original KPP without Langmuir turbulence ([KPP-CVMix](https://doi.org/10.1029/94RG01872)). The top panel shows the simulated temperature in KPP-CVMix whereas the lower two panels show the differences in KPPLT-VR12 and KPPLT-LF17 from KPP-CVMix. The test case is initialized and forced with conditions during the winter months (Sep. 22, 2012 - Dec. 5, 2012) of the Ocean Surface Mixing, Ocean Submesoscale Interaction Study in the northeast Atlantic (OSMOSIS, 48.7N, 16.2W; [Damerell et al., 2016](https://doi.org/10.1002/2015JC011423)). See more details of this test case in [Li et al., 2019](https://doi.org/10.1029/2019MS001810).

{{< figure src="../osmosis-winter_cvmix.png" width="100%" >}}


