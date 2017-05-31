+++
showonlyimage = false
draft = false
date = "2016-11-05T18:25:22+05:30"
title = "Channel flow"
weight = 10
author = "Lars Umlauf"
+++

Similar to the idealized [Couette scenario](/cases/couette), also in this test case, 
an unstratified, non-rotating water column of 10 m thickness is investigated. 
Here, however, the flow is driven by a constant barotropic pressure gradient 
resulting from the tilt of the free surface. The surface stress is set to zero. 
This type of flow is often referred as turbulent open channel flow. The figure 
below shows the stationary solution approached at the end of simulation. 
Different from the [Couette scenario](/cases/couette), the velocity profile shown in 
panel (a) exhibits only a single shear-layer at the bottom that converges 
toward the logarithmic wall layer close to the bottom. The turbulent 
diffusivity (panel b) is approximately symmetric but exhibits a slight vertical 
asymmetry due to the different boundary conditions at the surface and the 
bottom. Also this quantity converges toward the (linear) law-of-the-wall 
relation near the bottom. While the turbulent momentum flux is vertically 
constant in the [Couette flow](/cases/couette), for the open channel flow we find a 
linear variation. The vertical stress divergence is thus constant, and exactly 
balances the (constant) pressure gradient throughout the water column. The 
solution shown in the figure has been obtained with the k-ε model. Solutions 
for other two-equations models like the k-ω model or Mellor-Yamada model look 
similar (you can easily check this in the scenario directory by typing "make 
komega" or "make MellorYamada" to run GOTM with these alternative turbulence 
models). Technical details for this test case are described in the GOTM 
documentation. We now also provide the 
[MATLAB script](https://www.dropbox.com/s/xg2ccph2s5zjija/couette.m?dl=0) 
used to 
generate the figure for this GOTM scenario. Note that only MATLAB 2015a and 
higher supports direct reading of NetCDF output. 
[caption id="attachment_209" 
align="alignnone" width="500"]![Profiles of \(a\) velocity, \(b\) turbulent 
diffusivity of momentum, and \(c\) turbulent momentum flux for the Channel 
scenario after stationarity has been reached \(in red: law-of-the-wall 
solution\).](/cases/img/channel-705x1024.jpg) Profiles of (a) velocity, (b) 
turbulent diffusivity of momentum, and (c) turbulent momentum flux for the 
Channel scenario after stationarity has been reached (in red: law-of-the-wall 
solution).[/caption]

