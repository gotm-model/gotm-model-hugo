+++
showonlyimage = false
draft = false
date = "2016-11-05T18:25:22+05:30"
title = "Entrainment"
weight = 10
author = "Lars Umlauf"
+++

The entrainment scenario is similar to the 
[Couette scenario](/cases/couette/), 
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
width="500"]![entrainment](/cases/img/entrainment-705x1024.jpg) Temporal 
variability of (a) velocity, (b) stratification, and (c) turbulent diffusivity 
for the entrainment scenario. The white dashed line shows the entrainment depth 
according to 
[Price (1979)](http://dx.doi.org/10.1017/S0022112079002366).[/caption]

