+++
title = "... now with ice ..." 
draft = false
author = "Karsten Bolding"
date = "2019-08-07T12:00:00+02:00"
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

The use of submodules has made it much easier to integrate external projects without major risk of side effects.

#### CMake configuration

This blog contains information that goes along with [this](../towards_release_5_4/).

The inclusion of ice follows the method used to include FABM. A CMake variable **GOTM\_USE\_STIM** can be **on** or **off** - default will be **off**. As STIM can only be configured as a submodule no further configuration is necessary.

STIM provides a frame-work for including a number of different simple ice models. Presently two different models are fully working - and a third one is on progess. The STIM page will contain more information and hopefully be expanded in the future.

#### New run-time configuration - YAML

The resolute case has been used to test and develop the implementation - further set-ups will follow during the fall.

The present version must be run with the *--read_nml* option and an empty gotm.yaml.

The ice simulations is controlled via a *namelist* called *ice.nml*

```
&ice
ice_model = 2,
Hice = 1.29,
sensible_ice_water = 20.,
/
```

valid values for ice_model is 1, 2, (3). Hice is the initial ice thickness. The last parameter is a future fudge parameter - but is not used for now.

To have a view at the ice related variables the following can be added to *output.yaml*

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

#### A few results
 Will come shortly - my plot system is down ...
