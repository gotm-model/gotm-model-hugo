+++
showonlyimage = false
draft = false
date = "2016-11-05T18:25:22+05:30"
title = "Surface-wave breaking"
weight = 10
author = "Lars Umlauf"
+++

The wave-breaking scenario has many similarities with the
[couette scenario]({{< relref "couette.md" >}}):
A shallow, non-rotating and unstratified water column is forced by a constant wind stress
until the flow has become stationary. Now, however, near-surface turbulence generated
by breaking surface waves is taken into acount as suggested by
[Craig and Banner (1994)](https://journals.ametsoc.org/view/journals/phoc/24/12/1520-0485_1994_024_2546_mwetit_2_0_co_2.xml).
In their approach, the injection of turbulence during the breaking process is modeled
as a surface TKE flux that is proportional to the cube of the friction velocity.
In this case, a so-called "transport layer" develops near the surface, in which TKE dissipation
and vertical TKE transport balance,  and all turbulence quantities follow power-law relationships.
Data summarized in
[Umlauf and Burchard (2003)](https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=1008&context=journal_of_marine_research)
suggest, for example, that the TKE decays away from the surface with a power of approximately -2,
whereas the turbulence length scale increases linearly with a slope close to L=0.2. As shown by
[Umlauf and Burchard (2003)](https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=1008&context=journal_of_marine_research),
this implies a linear decrease of the velocity profile. While all two-equation models investigated by
[Umlauf and Burchard (2003)](https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=1008&context=journal_of_marine_research)
do show a power-law decay of the TKE away from the surface, only their generic length scale (GLS) model
reproduces the observed TKE decay rate of -2. Also the k-omega model with a predicted decay rate of -2.53
is approximately consistent with the observations, while the k-epsilon model fails
([Umlauf et al., 2003)](https://www.sciencedirect.com/science/article/abs/pii/S1463500302000392). Below the
transport layer, the solutions gradually converge to the classical law of the wall behavior of the couette
scenario (logarithmic velocity profile, constant TKE, etc.).

The solutions for the k-omega models and the theoretical power-law relationships are shown in the
figure below. After running GOTM for this scenario, you can reproduce the figure with the help
of the plotting script
[plot_wave_breaking.py](https://raw.githubusercontent.com/gotm-model/cases/master/wave_breaking/plot_wave_breaking.py),
which can also be found in the scenario directory. For this scenario, we also provide an alternative
yaml file to run the GLS model for comparison. If you run GOTM with this input file, make sure to adjust
the parameters and filename in
[plot_wave_breaking.py](https://raw.githubusercontent.com/gotm-model/cases/master/wave_breaking/plot_wave_breaking.py).

{{< figure src="/cases/img/wave_breaking.png"
caption="Profiles of (a) velocity, (b) turbulence kinetic energy, and (c) turbulence length scale (in red: theoretical power-law solutions). Results are shown for the k-omega model." >}}
