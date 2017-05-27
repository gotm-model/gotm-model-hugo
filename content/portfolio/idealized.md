+++
showonlyimage = false
draft = false
image = "portfolio/img/idealized.jpg"
date = "2016-11-05T18:25:22+05:30"
title = "Idealized test cases"
weight = 10
author = "Lars Umlauf"
+++

Idealized test case demonstrating various GOTM features.

<!--
- Coutte flow
- Channel flow
- Entrainment


Table of content
----------------

-   [Introduction](#introduction)
-->
-   [Couette](#couette)
-   [Channel](#channel)
    -   [Sublevel](#sublevel)
-   [Entrainment](#entrainment)
-   [Conclusion](#conclusion)

<!--more-->

<!--
Introduction
------------
-->

Unstratified Couette flow driven by a constant surface wind stress

Unstratified open-channel flow driven by a constant barotropic pressure gradient

Stress-driven entrainment into a linearly stratified turbulent


Couette
-------

The Couette scenario is the most basic of all GOTM scenarios. It represents a 
shallow (10 m deep), unstratified layer of fluid above a flat bottom that is 
driven by a constant surface stress in the x-direction. Earth's rotation is 
ignored. This flow is often referred to as turbulent Couette flow. After the 
onset of the surface stress, a thin turbulent near-surface layer is generated 
that rapidly entrains into the non-turbulent deeper parts of the water column. 
The solution at the end of the simulation, when the problem has become fully 
stationary, is shown in the figure below. The velocity profile in panel (a) 
reveals the existence of two shear layers in the near-surface and near-bottom 
regions, respectively, that converge toward that analytical law-of-the-wall 
solutions (dashed red lines in the figure). The diffusivity profile in the 
turbulent Couette flow is nearly parabolic (panel b), and also converges to the 
linear law-of-the-wall solution near the boundaries. The Reynolds stress (or, 
likewise, the turbulent momentum flux) shown in panel (c) is perfectly constant 
throughout the water column, and corresponds exactly to the applied surface 
stress. This is easily understood from the fact that all momentum entering the 
water column at the surface has to leave it again at the bottom under 
stationary conditions. The solution shown in the figure has been obtained with 
the k-ε model. Solutions for other two-equations models like the k-ω model or 
Mellor-Yamada model look similar (you can easily check this in the scenario 
directory by typing "make komega" or "make MellorYamada" to run GOTM with these 
alternative turbulence models). Technical details for this test case are 
described in the GOTM documentation. We now also provide the 
[MATLAB script](https://www.dropbox.com/s/xg2ccph2s5zjija/couette.m?dl=0) 
used to 
generate the figure for this GOTM scenario. Note that only MATLAB 2015a and 
higher supports direct reading of NetCDF output. 
[caption id="attachment_191" 
align="alignnone" width="500"]![](/portfolio/img/couette-705x1024.jpg) Profiles 
of (a) velocity, (b) turbulent diffusivity of momentum, and (c) turbulent 
momentum flux for the Couette scenario after stationarity has been reached (in 
red: law-of-the-wall solution).[/caption]


Channel
-------

Similar to the idealized [Couette scenario](#couette), also in this test case, 
an unstratified, non-rotating water column of 10 m thickness is investigated. 
Here, however, the flow is driven by a constant barotropic pressure gradient 
resulting from the tilt of the free surface. The surface stress is set to zero. 
This type of flow is often referred as turbulent open channel flow. The figure 
below shows the stationary solution approached at the end of simulation. 
Different from the [Couette scenario](#couette), the velocity profile shown in 
panel (a) exhibits only a single shear-layer at the bottom that converges 
toward the logarithmic wall layer close to the bottom. The turbulent 
diffusivity (panel b) is approximately symmetric but exhibits a slight vertical 
asymmetry due to the different boundary conditions at the surface and the 
bottom. Also this quantity converges toward the (linear) law-of-the-wall 
relation near the bottom. While the turbulent momentum flux is vertically 
constant in the [Couette flow](#couette), for the open channel flow we find a 
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
solution\).](/portfolio/img/channel-705x1024.jpg) Profiles of (a) velocity, (b) 
turbulent diffusivity of momentum, and (c) turbulent momentum flux for the 
Channel scenario after stationarity has been reached (in red: law-of-the-wall 
solution).[/caption]


Entrainment
-----------

The entrainment scenario is similar to the 
[Couette scenario](/examples/nns/couette/), 
except that the water column is now stably 
stratified by a vertically constant density gradient. Also in this scenario, 
the effect of Earth's rotation is ignored. The entrainment scenario  is 
ideally suited to benchmark the model performance in stress-driven entrainment 
situations against available experiments (see 
[Umlauf and Burchard, 2005](http://dx.doi.org/10.1016/j.csr.2004.08.004)) 
The results shown in the 
figure below illustrate that after the onset of the constant surface stress in 
the x-direction, a thin near-surface layer is accelerated (panel a), and slowly 
entrains into the stratified, non-turbulent interior region. Shear-driven 
turbulence in this region is mirrored in the large turbulent diffusivities 
shown in panel (c), which generate a nearly well-mixed surface layer  that is 
separated from the interior by a pycnocline of gradually increasing strength 
(panel b). The white dashed line indicates the solution suggested by 
[Price (1979)](http://dx.doi.org/10.1017/S0022112079002366) 
for shear-driven 
entrainment into a linearly stratified fluid 
[see Eq. (53) in [Umlauf and Burchard, 2005](http://dx.doi.org/10.1016/j.csr.2004.08.004)]. 
The numerical 
solution shown in the figure has been obtained with the k-ε model. Solutions 
for other two-equation models available in GOTM look similar. You can easily 
check this by modifying the GOTM namelist files to run the k-ω model 
([Umlauf et al., 2003](http://dx.doi.org/10.1016/S1463-5003\(02\)00039-2)) 
or the GLS (generic length scale) model described in 
[Umlauf and Burchard (2003)](http://dx.doi.org/10.1357/002224003322005087). 
Technical details for this GOTM scenario may be found in the GOTM documentation. 
We now also provide the 
[MATLAB script](https://www.dropbox.com/s/7tlj1kqibon4n4w/entrainment.m?dl=0) 
used to generate the figure below. Note that only MATLAB 2015a and higher supports 
direct reading of NetCDF output. 
[caption id="attachment_217" align="alignnone" 
width="500"]![entrainment](/portfolio/img/entrainment-705x1024.jpg) Temporal 
variability of (a) velocity, (b) stratification, and (c) turbulent diffusivity 
for the entrainment scenario. The white dashed line shows the entrainment depth 
according to 
[Price (1979)](http://dx.doi.org/10.1017/S0022112079002366).[/caption]


Conclusion
----------

Maybe add a few sentences here
