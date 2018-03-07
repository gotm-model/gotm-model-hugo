+++
title = "GOTM release - v5.2" 
draft = true
author = "Karsten Bolding"
date = "2018-03-07T12:00:00+02:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

Version 5.2 of GOTM is ready for release. It comes relative shortly after the
release of version 5.0. One of the policies for a new release are changes in 
configuration files - releated to the new features.

<!--more-->

As a consequence of the more streamlined release model we are now ready with a new release of GOTM - version 5.2. Updating the stable version implies a new version for the development branch as well - now 5.3.

As a user the following step must be taken in order to use the new stable
version of the code.

* Check out the new branch - v5.2 - of the GOTM source code
* If you are using *editscenario* and related  *.xml*-file to keep track of 
your configuration the version description on the first line of the *.xml* file
must be updated to **gotm-5.2**.

Update to new versions have been done for all the standard test cases provided
with GOTM.

In this release two new features has been implemented as described below.

### New features
* Hot-start facility - developed in the [PROGNOS](http://prognoswater.org) project and further supported by JRC.
* Option to read in longwave back-radiation instaed of calculating - funded by Don Pierson/[Erken](http://katalog.uu.se/organisation/?orgId=X137:6)
* We have also added 3 new test-cases - two for the Mediterranean, one for the
Black Sea and updated the gotland case.

Hot-start (or restart) allow to split a simulation in two or more time-chunks.
GOTM will at the end of a simulation write the state of the model to a NetCDF-
formatted file - *restart.nc*. This file can be used to provide initial 
conditions at a subsequent simulation. The feature is controlled via the 
namelist variable *restart_offline* by setting it to true. There are different 
use-cases for the hot-start facility. One involves spinning up GOTM in physics
only mode and when the physics is in balance enable bio-geochemistry. The 
*restart.nc* file from the spin-up run does not contain any bio-geochemical 
variables - on the other hand - when the bio-geochemical is started the full 
state is a combination of physical and biogeochemical state-variables. In this
case the variable *restart_allow_missing_variable* must be set to .true.. 
Missing variables in *restart.nc* will be reported to the screen - but the
simulation will continue. The default setting of 
*restart_allow_missing_variable* is .false. as it is the safer setting.

The lake people have for a while asked for an option to read in longwave back-
radiation instead of calculating it as part of the normal air-sea flux 
calculation. This feature has been implemented.

Please have a look at the planned [roadmap](../roadmap_2017/).
