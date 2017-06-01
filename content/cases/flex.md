+++
showonlyimage = false
draft = false
date = "2016-11-05T18:25:22+05:30"
title = "FLEX"
weight = 20
author = "Lars Umlauf"
+++

A data set which has been used throughout the last 40 years as a calibration 
for mixing parameterisations has been collected during the measurements of the 
**Fladenground Experiment 1976 (FLEX'76)** campaign. Starting from a well-mixed 
winter situation, a surface mixed layer is established, which is several times 
deepened and partly removed by storm events. 

{{< figure src="/cases/img/flex.png" caption="Spring temperature development at the FLEX site in the Northern North Sea." >}}

<!--
[caption id="attachment_443" align="aligncenter" width="640"]![Spring temperature development at the FLEX site in the Northern North Sea](/portfolio/img/flex.png) 
-->

The measurements of meteorological forcing and potential temperature 
profiles were carried out in spring 1976 in the northern North Sea at a water 
depth of about 145 m and a geographical position at 58 deg 55'N and 0 deg 32'E. 
The simulation is run from April 6 to June 7, 1976. The 
[Kondo (1975)](http://link.springer.com/article/10.1007/BF00232256) 
bulk formulae have 
been used for pre-calculating the surface fluxes, which are given in the data 
files momentumflux.dat, and heatflux.dat. Other meteorological data files gives 
sea surface temperature (sst.dat) and short wave radiation (swr.dat). Tidal 
flow is forced by oscillating sea surface slopes (pressure.dat), temperature 
profiles for validation are provided directly from CTD (tprof_ctd.dat) or 
interpolated from CTD to semi-diurnal profiles (tprof.dat). Salinity from CTD 
(s_prof_ctd.dat) or from a 3D model (s_prof.dat) are used for nudging simulated 
salinity to "observed" data at a time scale of 2 days. Six-hourly values for 
light extinction are given by extinction.dat. Model simulations similar to 
those provided here have been published by 
[Burchard & Baumert (1995)](http://dx.doi.org/10.1029/94JC03229). 
As there, also here a k-epsilon 
model is used as turbulence closure model, but here the 
[Cheng et al. (2002) ](http://journals.ametsoc.org/doi/abs/10.1175/1520-0469\(2002\)059%3C1550%3AAIMFTT%3E2.0.CO%3B2)
stability functions are used.

