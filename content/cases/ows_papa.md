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
[caption id="attachment_488" align="aligncenter" width="640"]![Annual cycle of temperature development at the OWS Papa site in the North East Pacific. Left: observations; right: model results.](/portfolio/img/ows_papa.png)
Annual cycle of 
temperature development at the OWS Papa site in the North East Pacific. This 
plot was created with 
[ows_papa.py](/portfolio/img/ows_papa.py).
[/caption]
The way how bulk formulae for the surface momentum and heat 
fluxes have been used here is discussed in detail in 
[Burchard et al. (1999)](http://io-warnemuende.de/tl_files/staff/burchard/pdf/papers/report.pdf).
The maximum simulation time allowed by the included surface forcing file and 
the temperature profile file is January 1 (17.00 h), 1960 - December 31 (12.00 
h), 1968. In this scenario, the simulation time is run from March 25, 1961 
(0.00 h) to March 25, 1962 (0.00 h). For further information, see 
[Burchard and Bolding (2001)](http://journals.ametsoc.org/doi/abs/10.1175/1520-0485\(2001\)031%3C1943:CAOFSM%3E2.0.CO%3B2).
