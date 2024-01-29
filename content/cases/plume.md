+++
showonlyimage = false
draft = false
date = "2024-01-05T18:25:22+05:30"
title = "Subglacial plume"
weight = 10
author = "Hans Burchard"
+++

The subglacial plume scenario described in a simple geometry the vertical structure of a subglacial plume rising under a sloping ice shelf - ocean interface. This scenario has been built by Burchard et al. (2022) to develop consistent ways of coupling melting processes at the ice-ocean interface with the turbulent stucture of the plume. This principle has also been applied by Reinert et al. (2023) for a two-dimensional study with vertical resolution.

The simulations analyzed here start from rest (zero velocity), with an initial plume thickness of D = 5 m. The ice-ocean interface is located at a depth of zb = −300 m and the water column is zb + H = 150 m deep, such that the bottom at z = −H = −450 m is sufficiently far below the ice to allow for an undisturbed plume  deepening. 
This set of initial conditions allows for a subglacial plume that is quickly adjusted  dynamically to the local conditions.
The vertical discretization uses kmax = 500 layers with zooming toward the ice-ocean interface such that the resolution is gradually increasing from 0.5 m at the botttom to 0.09 m at the surface.

The ambient water is at rest and has a high ocean salinity of 34.5 g/kg and potential temperatures of 1°C. The initial plume salinity and potential temperature are 32 g/kg and −1°C, such that its potential density is lower than the potential density of the plume water. With this, the initial pressure gradient drives a subglacial plume rising upwards along the slope of the ice-ocean interface.
The latitude of the water column location is 79 deg N, such that the Coriolis parameter has a value of f = 1.43 X 10^−4 1/s. 
The ice-ocean interface is sloping toward the north, while the slope toward the east vanishes. During the simulation time of 14 days, the plume velocity is expected to point toward the north-east direction as a consequence of the force balance between northward pressure gradient force, Coriolis force and frictional effects. The plume is subject to cooling and freshening due to melt fluxes at the ice-ocean interface and to warming and salinification due to entrainment of warmer and saltier ambient water. This simulation can be thought of as a plume underneath an infinite plain, where all plume properties are homogeneous along the interfacial slope.

{{< figure src="/cases/img/plume_u.png" caption="The along slope velocity." >}}
{{< figure src="/cases/img/plume_v.png" caption="The cross slope velocity." >}}
{{< figure src="/cases/img/plume_temperature.png" caption="Temperature profile." >}}
{{< figure src="/cases/img/plume_salinity.png" caption="Salinity profile." >}}

Literature:

Burchard, H., Bolding, K., Jenkins, A., Losch, M., Reinert, M., & Umlauf, L. (2022). The vertical structure and entrainment of subglacial melt water plumes. Journal of Advances in Modeling Earth Systems, 14, e2021MS002925.

Reinert, M., Lorenz, M., Klingbeil, K., Büchmann, B., Burchard, H. (2023)
High-Resolution Simulations of the Plume Dynamics in
an Idealized 79°N Glacier Cavity Using Adaptive Vertical
Coordinates, Journal of Advances in Modeling Earth Systems, 15, e2023MS003721. 

Figure caption: Simulated cross-slope and along-slope velocity, salinity and potential temperature profiles during the 14-day simulation period.

