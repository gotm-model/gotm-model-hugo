+++
author = "Jorn Bruggeman, Karsten Bolding and Knut Klingbeil"
categories = []
date = "2017-10-11T12:00:00+02:00"
description = ""
draft = false
featured = ""
featuredalt = ""
featuredpath = ""
image = "blog/img/"
linktitle = ""
title = "GOTM release - v5.0"
type = "blog"

+++

Finally the version 5 of GOTM is ready for release. It comes with a 
very large number of changes and improvements. Some - but not all - 
are mention in the list below.

<!--more-->

Knut Klingbeil, Jorn Bruggeman, Lars Umlauf, Hans Burchard and Karsten Bolding will like to announce the new version of GOTM - v5.0.

After far to long time we are finally ready to release a new version of GOTM. Hopefully we will have a more streamlined release model in the future where new versions will follow new features requiring changes to input specifications.

In the list below we have collected some of the changes that have been done over the last almost 10 years. Many more are hidden in the logs in the GIT repository. We have not put any specific weight on the listed changes/new features/bug fixes - but it should be noted that thay have not taken equal amount of time to implement.

One thing to note though is that utilities to interact with GOTM - i.e. everything that is not strictly Fortran - have been moved away from the core Fortran code.  

The present release has been used in production mode already for a quite some years and is regarded as very stable - but still - if you find errors please report back so we can fix and include in future releases.

### New features
* CVS to GIT transition
* Make to CMake change of build system
* Replaced extras/bio by [FABM](http://www.fabm.net/wiki)
  * First preliminary version in 2011
  * Both FABM and the support has been extended considerable since then.
* Flexible output system
  * Output specifications via YAML formatted configuration file
  * Old ncdf output supports _NCDF_SAVE_DOUBLE_, nfirst and sync_out (deprecated - use flexible system)
* Airsea interface changes
  * Fairall et al. (1999) bulk formulas
  * New air/sea methods (albedo_method, swr_method)
  * Added rain impact to Kondo
  * Truncate surface heat flux (simple ice model)
  * Namelist variables *wind_factor*, *shf_factor* and *swr_factor*.
  * Temporal interpolation of raw meteo data instead of bulk fluxes
* Very long term simulations possible
* Portable floating point declaration
* New input module
* Command line argument for compilation options
  * With new use-cases of GOTM an option to show information of a compiled version is handy
* *extinct_method=7* for user-defined parameters via nml
* Support initial non-zero surface elevation
* New namelist variables *zeta_scale*, *zeta_offset*

### Bugfixes
* Limitation of swr
* Use Craig & Banner wavebreaking parameter cw from nml
* Windstress calculation (sign and magnitude)
* Changed advbcup from zerodiv to onesided
* W_height correction
* Wrong sign in const_NNS
* Bugfix I_0
* Compute h_press also for method 1
* Init of jul1,secs1 for timefmt=1
* Interpolate cloud cover in time
* Proper treatment of observed sst and sss
* NONLOCAL: gamm=>gamv
* Normalization of bottom stress with rho_0
* Buoy_method=2: added avh=nub
* Kondo stability constant s0
* sign of salinity stratification for double-diffusion
* Albedo values for (default) Payne method

### Code refactoring
The *gui.py* directory has been completely removed from the GOTM code base and now forms the basis of a set of utilities in a separate software project. The main reason for this split is to allow for individual development paths for GOTM and the utilities.

  * *editscenario* for manipulating and converting .xml based configuration files to Fortran namelist files
  * *PyNcview* (and *multiplot*)
  * *gotmgui* for configuring and running GOTM via a GUI

More tools are in the pipe-line and will be released on a *'being ready'* basis.

The old GOTM/BIO code has been completely removed - superseded by FABM.

### Note

To be able to manage your own model configurations using *editscenario* with this version of GOTM you must change the version tag in the .xml file from __scenario version="gotm-4.1.0"__ to __scenario version="gotm-5.0"__. This has already been done in the prepared cases.
