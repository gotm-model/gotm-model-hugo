+++
title = "GOTM Roadmap - as of end of 2017" 
draft = false
author = "Karsten Bolding"
date = "2017-12-22T12:00:00+02:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

Below we will give a short description of the planned developments in the next 1 to 2 years. These plans do not in any way exclude other developments but only list what we have planned or have already started (likely because of project deliverables).

<!--more-->

### List of planned stable releases

  * Version 5.2 (upcoming)
    * Restart facility - developed in the [PROGNOS](http://prognoswater.org) project and further supported by JRC.
    * Option to read in longwave back-radiation instaed of calculating - funded by Don Pierson/[Erken](http://katalog.uu.se/organisation/?orgId=X137:6)
  * Version 5.4
    * A rewrite of the standard *namelist* based initialization to a *yaml* based one.
  * Version 5.6
    * The ability of GOTM to natively do ensemble simulations.
  * Version 6.0
    * Merge of the lake-branch into master.
  * Version 6.2
    * Ice model in GOTM


### Rationale

The exact sequence of the releases is not carved in stone - especially the merge of the lake branch might be moved forward in time - but presently we are awaiting a publication related to this very important new feature.

#### Version 5.2

A proper restart facility in GOTM has been asked for for a very long time and finally we are almost there. The implementation has been greatly facilitated by the flexible output module Jorn Bruggeman has developed. The issue is how to create a list of necessary variables to store in the restart-file when the actual list of (state-)variables are not determined before at run-time. This problem has been solved by adding an attribute - *part_of_state* - during variable registration. Based on checking for this attribute when traversing the list of all variables a NetCDF file can be written/read as part of the restart logic. A further complication is the possible mis-match between the variables in the simulation and the content of the restart-file. This could be the case if e.g. a simulation warm-up period was done with physics only - and at the end of this period bio-geochemistry is enabled. In this case the state will contain all bio-geochemical variables - but the restart file will only contain the physical variables. To overcome this problem we have implemented a *logical* variable allowing for missing variables in the restart file. This option is false by default and must be explicity set to true in the namelist file in cases like the above.

A wish from the lake-modelling people have been the abillity to read in observed longwave back-radiation - instead of calculating together with sensible and latent heat - as is is frequently measured for lake-sites (opposed to proper cloud-cover data). This will be available in this version - the format of the file is the standard scalar GOTM-format.

#### Version 5.4

Partly based on the experinces using YAML-based configuration in FABM and partly required by some of the other developments we do - autocalibration, sensitivity analysis and ensemble simulations - it has shown that the Fortran only namelist based initialization method does not really cut it with the use cases we have. This is a change that will have relative little impact on users - unless you do a lot of hand-editing of namelist files in which case you'll have to get used to edit yaml-files instead - but it will require substantial changes to the code it self (but only all the *init_* routines. A new blog will be written when we approach the first release candidates.

#### Version 5.6

As written above the change to the yaml-based configuration is partly a consequence of different use cases - like auto-calibration. This typically requires a very large number of simulations - counting from 1000's to tens of 1000's and maybe even more depending on the complexity of the problem. To facilitate this GOTM will be extended to run in **ensemble** mode where in principle any number of simulations can be done with one program invocation. GOTM will only be doing the forward integration - the actual definition of the ensemble members will be done by external programs. The most advanced method will use a master/worker self-scheduling algorihtm implemented using [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) to do any number of individual simulations from a single GOTM invocation. This work is already beyond proff of concept but will need some more testing before being released and the full functionallity still awaits the yaml-configuration feature.

#### Version 6.0

Since almost 6 years work has been done to make GOTM applicable for lake applications. This mainly involves incorporating the effect of the hypsograph - the ralationship between depth and area. A number of people have been involved but the work has never really been finished even though the code (a separate lake branch in the main repository) has been in production for some years. In addition to the *dA/dz* in the advection/diffusion equations inflow/outflow is also very important for lakes as they carry the nutrient loadings. A very flexible method has been implemented allowing any number of inflows and outsflows each inflow with individual loadings and for all separate configuration of interleaving of fixed depth ranges for the flow. The GOTM/Lake branch is tightly connected to FABM and the majority of the development has been carried out in projects where the main focus has been on bio-geochemistry instead of the physics. As mentioned the code is ready but we are awaiting the finishing of a publication on the changes in the algorithms in order to account for *dA/dz*.

#### Version 6.2
Until now an ice-model has not been integrated into the master branch. Two specific efforts has been made in 2014-2015 but not the Winton ice-model nor the Flato ice-model made it into the repository even though the latter has been published by University of Victoria, Canada. Recently, it has been decided to revive the efforts to have - at least - the Flato model included. GOTM has not been used a lot in the arctic - maybe explanined by the lack of aproper ice-model - but with the recent increased use in the lake community the need for ice is increasing. In accordance with the solution methods used in GOTM - the Flato model is likely the best choice solving differential equations for light and temperature layered configuration where the number of layers can be determined by the user - much like the way it is done in GOTM.
