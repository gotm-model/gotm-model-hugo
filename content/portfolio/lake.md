+++
showonlyimage = false
draft = false
image = "portfolio/img/sunset-549677_960_720.jpg"
date = "2018-08-14T12:00:00+00:00"
title = "Lake cases"
weight = 20
author = "Dennis Trolle"
+++

GOTM configured in Lake mode - i.e. using a hypsograph to specify depth-area relations. The GOTM lake branch is kept in sync with the master branch and merging is hopefully soon to occur.

-   [Ravn](/cases/ravn/)

Picture from [here](https://pixabay.com/en/sunset-lake-water-reflection-clouds-549677/)

<!--more-->

Models are widely used in the management of lake and reservoir water quality, particularly for setting maximum allowable nutrient load targets. Mechanistic models, in particular, are increasingly used for decision support and management e.g. [Trolle et al. 2008](https://doi.org/10.1016/j.ecolmodel.2008.08.005), since they are able to account for multiple stressors, such as the effects of changes in nitrogen and phosphorus loads and climate e.g. [Nielsen et al. 2014]([200~https://doi.org/10.1890/13-0790.1). One of the earliest examples of mechanistic lake modelling is the Danish Lake Glumsø model by Jørgensen [1976], which already then was highly parameterized and involved dynamics of three trophic levels, including phytoplankton, zooplankton and fish. Additional mechanistic models have since been developed, such as SALMO by Recknagel and Benndorf [1982], DYRESM-CAEDYM by Hamilton and Schladow [1997], PCLake by Janse [1997] and PROTECH by Reynolds et al. [2001]. PCLake has since its origin undergone further development and today represent one of the most complex lake ecosystem models available. PCLake describe four trophic levels, including multiple phytoplankton groups, macrophytes, zooplankton, zoobenthos, and zooplanktivorous, benthivorous and piscivorous fish. [Hu et al. 2016](https://doi.org/10.5194/gmd-9-2271-2016 ) produced a FABM implementation of PCLake, thereby enabling PCLake applications to physically heterogeneous water bodies, including also water bodies that stratify, in contrast to the original fully-mixed box model. Hence, the coupled GOTM-FABM-PCLake model can now be applied to stratifying lakes and reservoirs.

{{< figure src="/portfolio/img/sunset-549677_960_720.jpg" >}}


