+++
showonlyimage = false
draft = false
date = "2016-11-05T18:25:22+05:30"
title = "OWS Papa"
weight = 20
author = "Lars Umlauf"
+++

This scenario is a classical scenario for the **Northern Pacific**, for which 
long term observations of meteorological parameters and temperature profiles 
are available. The station <a href="https://www.google.com/maps/@50,-144,5z/" target="_blank">Papa</a> at 145 deg W, 50 deg N has the advantage that 
it is situated in a region where the horizontal advection of heat and salt is 
assumed to be small. Various authors used these data for validating turbulence 
closure schemes. 

{{< figure src="/cases/img/ows_papa.png" caption="Annual cycle of temperature development at the OWS Papa site in the North East Pacific. Upper panel: observations; lower panel: model results. This simulation was published by [Burchard and Bolding (2001)](http://journals.ametsoc.org/doi/abs/10.1175/1520-0485\(2001\)031%3C1943:CAOFSM%3E2.0.CO%3B2). The plot was created with [ows_papa.py](/portfolio/img/ows_papa.py).">}}

The way how bulk formulae for the surface momentum and heat 
fluxes have been used here is discussed in detail in 
[Burchard et al. (1999)](https://www.io-warnemuende.de/files/staff/burchard/pdf/papers/report.pdf).

Here, 12 different model configurations are used, each contained in a 
different yaml file. Here is the list of the yaml files included:

1. [gotm\_cvmix\_era5.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm_cvmix_era5.yaml)
2. [gotm\_cvmix\_flux.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_cvmix\_flux.yaml)
2. [gotm\_cvmix\_legacy.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_cvmix\_legacy.yaml)
2. [gotm\_cvmix\_meteo.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_cvmix\_meteo.yaml)
2. [gotm\_keps\_era5.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_keps\_era5.yaml)
2. [gotm\_keps\_flux.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_keps\_flux.yaml)
2. [gotm\_keps\_legacy.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_keps\_legacy.yaml)
2. [gotm\_keps\_meteo.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_keps\_meteo.yaml)
2. [gotm\_kw\_era5.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_kw\_era5.yaml)
2. [gotm\_kw\_flux.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_kw\_flux.yaml)
2. [gotm\_kw\_legacy.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_kw\_legacy.yaml)
2. [gotm\_kw\_meteo.yaml](https://raw.githubusercontent.com/gotm-model/cases/master/ows_papa/gotm\_kw\_meteo.yaml)



The difference between the model simulations 
are given in terms of 

(i) three different turbulence 
closure models, indicated by keps (for the k-epsilon model), kw (for the
k-omega model) and cvmix (for the KPP model inside the cvmix environment); 

(ii) four different sets of forcing types, indicated by era5 (for meteo files from the ERA5 reanalysis), meteo (for meteo files from observations), 
flux (for air-sea fluxes precalculated from observed meteorology) and legacy
(for the original flux-driven scenario described by [Burchard and Bolding (2001)](http://journals.ametsoc.org/doi/abs/10.1175/1520-0485\(2001\)031%3C1943:CAOFSM%3E2.0.CO%3B2).

Different forcing scenarios will use different simulation periods. 

It can be seen that for multi-annual flux-driven scenarios
a drift in temperature occurs due to missing feedback between
sea surface temperature and air temperature. 

The default yaml file is set to gotm\_keps\_era5.yaml.

For further information, see 
[Burchard and Bolding (2001)](http://journals.ametsoc.org/doi/abs/10.1175/1520-0485\(2001\)031%3C1943:CAOFSM%3E2.0.CO%3B2) and [Li et al. (2021)](https://gmd.copernicus.org/articles/14/4261/2021/).
