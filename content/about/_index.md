+++
date = "2016-11-05T21:05:33+05:30"
title = "About GOTM"
+++

<!---
title: Home
link: http://www.gotm.net/
author: bolding
description: 
post_id: 6
created: 2015/09/30 08:19:38
created_gmt: 2015/09/30 08:19:38
comment_status: closed
post_name: home
status: publish
post_type: page
# Home

### About GOTM
-->

Welcome to the General Ocean Turbulence Model (GOTM), which is a one-dimensional water column model for studying hydrodynamic and biogeochemical processes in marine and limnic waters. GOTM is published under the GNU Public Licence and can be freely used.

The heart of GOTM is a library of traditional and state-of-the-art turbulence closure models for the parameterisation of vertical turbulent fluxes of momentum, heat and dissolved and particulate matter ([Umlauf and Burchard, 2005](http://dx.doi.org/10.1016/j.csr.2004.08.004)). This turbulence module has been linked to, or recoded for, a number of ocean models such as ROMS, FVCOM, SELFE, FESOM, GETM and NEMO in order to parameterize turbulent exchange.

Typically, GOTM is used as a stand-alone model for studying dynamics of boundary layers in natural waters, where lateral gradients can either be neglected or prescribed. Frequent hydrodynamic applications are investigations of air-sea fluxes, surface mixed-layer dynamics, stratification processes in shelf seas, dynamics of bottom boundary layers with or without sediment transport, estuarine and coastal dynamics, and many more. To link biogeochemical or sediment modules to GOTM, the [Framework for Aquatic Biogeochemical Models (FABM)](http://www.fabm.net/wiki) ([Bruggeman and Bolding, 2014](http://dx.doi.org/10.1016/j.envsoft.2014.04.002)) is used, which is also available for several 3D models.

Over the last years we have moved more and more to the services offered by Github for interactions between users and developers. The shift away from using mailing lists is motivated by the better interaction between users and developers offered by Github. 
This includes using [Github Actions](https://github.com/gotm-model/code/actions) for code quality control. It implies compiling and running GOTM on a different operating systems on Github software.
We also encourage people to use the [Github Issues](https://github.com/gotm-model/code/issues) for reporting problems related to GOTM.
Finally, we encourage to use [Pull requests](https://github.com/gotm-model/code/pulls) for contributing code to GOTM.

We have not closed the mailing lists and they are still available here: [Users](https://groups.google.com/g/gotm-users) and [Developers](https://groups.google.com/g/gotm-devel).
