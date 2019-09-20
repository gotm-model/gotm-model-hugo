+++
title = "Kondo - what was wrong" 
draft = false
author = "Karsten Bolding"
date = "2019-09-19T10:00:00+02:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

The file - kondo.F90 - is one of the oldest and least changed in the GOTM repository. And still - it had issues.


<!--more-->

### Variable naming inconsistencies

The original paper by Kondo(1975) used **d** to refer to momentum, **e** to refer to latent heat and **h** to refer to sensible heat. In _kondo.F90_ - and inherited by _fairall.F90_ - the names of variables **qh** and **qe** for sensible and latent heat respectivly was calculated using wrongly named **ced** and **chd**. On top the naming in the output .nc file was wrong so latent heat was refered to as sensible heat - and vice versa.

If the above all sounds confusing - then relax. Order has been achieved - the variable naming is now consistent and the correct variable meta data are in place in the output files. Old plots of sensible and latent heat will be wrong but the sum of surface heat fluxes are correct.

### Checking the bulk transfer coefficients

During my work with _kondo.F90_ I found ways to optimize the code. I've checked the code and old and new versions give _the same_ - in the sense close enough.

Furthermore, there should not have been any impact on simulation results - or if so - only very, very minor - here from the NNS annual setup.
{{< figure src="../sensible-new-old.png" width="100%" >}}
{{< figure src="../latent-new-old.png" width="100%" >}}

For the actual calcuation of the momentum and heat fluxes the speed up is 40% - but when the percentage of the flux calculations is very, very small - the effect is not very big in a 1D model context. 

In addition I've created a small tool consisting of a Fortran test program and associated Python plot script. 

The following lines show how to use the tool - note CMake configuration must have been done.

```
kb@orca ~ $ BUILDDIR=~/source/build/intel/19.2/code/tests
kb@orca ~ $ cd $BUILDDIR
kb@orca ~/source/build/intel/19.2/code/tests $ make test_bulk
kb@orca ~/source/build/intel/19.2/code/tests $ ./test_bulk
 basic variables:
 rh=      90.0000000000000     
 airp=    101325.000000000     
 tw=      10.0000000000000     
 ta=      10.0010000000475     
 
 humidity related variables:
 rhoa=    1.24112344433306     
 L=       2500000.00000000     
 qs=     7.414878832585809E-003
 qa=     6.807542851252644E-003
kb@orca ~/source/build/intel/19.2/code/tests $ python $GOTM_BASE/scripts/python/plot_bulk.py
```

Adjust your _BUILDDIR_. 

Many other tests can be done by changing *basic_varibles* in test_bulk.F90. the present settings are for stable atmospheric conditions.
