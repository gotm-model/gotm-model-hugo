+++
showonlyimage = false
draft = false
date = "2016-11-05T18:25:22+05:30"
title = "Gotland Deep"
weight = 20
author = "Lars Umlauf"
+++


These simulations are made for the location of station 271** Central Eastern 
Gotland Sea of the Baltic Sea** at 20 deg E and 57.3 deg N with a water depth 
of 250 m. Initial conditions for temperature and salinity are derived from 
measurements. Meteorological forcing was available from the ERA15 reanalysis 
data set. For the penetration of solar radiation into the water column, fairly 
turbid water (Jerlov type IB) is assumed. Salinity concentrations are nudged to 
observations with a time scale of 50 days. 
[caption id="attachment_520" align="aligncenter" width="640"]![Simulated temperature, salinity contours and examplary ERGOM state variables in the Central Baltic Sea.](/portfolio/img/gotland-deep.png) 
Simulated temperature, salinity contours and examplary ERGOM state variables 
in the Central Baltic Sea. This plot was created with 
[gotland.py](/portfolio/img/gotland.py).
[/caption]
The simulation is carried out for the years 1980-1990. For the discretisation, 
the water column has been divided into 100 vertical layers, with a strong 
zooming towards the surface, resulting in a mean near-surface resolution of 
less than 0.5 m. The time step for these simulations is set to 10 minutes. For 
details of the gotland scenario see 
[Burchard et al. (2006)](http://dx.doi.org/10.1016/j.jmarsys.2005.04.011).

