+++
title = "... now with ice ..." 
draft = false
author = "Karsten Bolding"
date = "2020-02-10T12:00:00+02:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

Version 5.4 of GOTM will contain a feature preview of ice modelling using [STIM](https://github.com/BoldingBruggeman/stim). Additional work will have to go into the development - but the coupled GOTM/STIM system does produce results that resembles reality.

<!--more-->

Updated from 2019-08-07. Ice module is ready for production runs.

The use of submodules has made it much easier to integrate external projects without major risk of side effects.

#### CMake configuration

This blog contains information that goes along with [this](../towards_release_5_4/).

The inclusion of ice follows the method used to include FABM. A CMake variable **GOTM\_USE\_STIM** can be **on** or **off** - default will be **off**. As STIM can only be configured as a submodule no further configuration is necessary.

STIM provides a frame-work for including a number of different simple ice models. Presently two different models are fully working - and a third one is on progess. The STIM page will contain more information and hopefully be expanded in the future.

#### Run-time configuration - YAML only

The configuration is very sipmple and takes only 3 variables. Se below:

```
  ice:
    ice_model: 0                     # [0=None, 1=Lebedev (1938), 2=MyLake, 3=Winton; default=0]
    Hice: 0.0                        # total ice thickness [m; default=0.0]
    ocean_ice_flux: 0.0              # heat flux from ocean to ice [W/m2; default=0.0]
```

valid values for ice_model is 1, 2, (3). Hice is the initial ice thickness. The ocean_ice_flux is a non-resolved flux of heat from ocean water to the ice.

And additional option might be added to use the *old* GOTM implementation - even in the case GOTM is compiled with support for STIM.

```
ice:
   time_unit: hour
   time_step: 24
   sync_interval: 0
   time_method: 1
   variables:
      - source: airt
      - source: ice/*
```

#### A simulation example
Below is shown 7 year simulation with all 3 different ice models compared to observations from the Northern Baltic Sea. Ice thickness data provided by Adolf Stips, JRC.

{{< figure src="../baltic_ice.png" width="100%" >}}

