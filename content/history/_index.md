+++
date = "2017-05-24T14:40:05+02:00"
title = "The GOTM history"
+++

<!---
title: The GOTM history
link: http://test.gotm.net/information/early-history/
author: bolding
description: 
post_id: 128
created: 2015/12/09 10:43:37
created_gmt: 2015/12/09 10:43:37
comment_status: closed
post_name: early-history
status: publish
post_type: page

# The GOTM history
-->

Many people have been giving important impulses to the development of GOTM. The first lines of the first PASCAL code had been programmed in late 1992 by Hans Burchard as part of a Ph.D. project at the Institute of Oceanography at the University of Hamburg, Germany, under the supervision of Jürgen Sündermann and Helmut Baumert. This was the basis for a one-dimensional water column model for simulating the so-called FLEX’76 data in the Northern North Sea. Substantial advice for these modelling activities (such as the introduction to the Patankar trick) came also from Eckard Kleine (Bundesamt für Seeschiffahrt und Hydrographie, Hamburg, Germany) who together with Helmut Baumert had a long time experience in turbulence modelling.

A strong motivation for extending the model code (which at that stage only included the k-epsilon model) came in 1995 from George Mellor who provoked with the statement that he never saw a k-epsilon model (as contrasted to his Mellor-Yamada model) reproducing the Monin-Obukhov similarity theory. In an effort together with Ole Petersen (International Centre of Computational Hydrodynamics, Hørsholm, Denmark) the equivalence of the k-epsilon and the Mellor-Yamada models under certain circumstances and thus the successful reproduction of the Monin-Obukhov similarity theory could be demonstrated. Numerical stability problems occurred when the water column model (now already with a switch for choosing either the k-epsilon or the Mellor-Yamada model) was transferred to FORTRAN in late 1996. It was Boris Kagan who insisted that oscillations in the turbulent macro length scale under very small stable stratification are numerical artifacts and therefore unacceptable. The solution to that problem was finally to use double instead of single precision for the calculations. In a cooperation with Nadia Pinardi and Sergio Castellari during 1997 and 1998, the turbulence model code was incorporated into a version of MOM for calculating the general circulation and convective events in the Mediterranean Sea. During the same years, the one-dimensional water column model was challenged by in-situ turbulence observations by Walter Eifler and Adolf Stips. During this effort both, the strategies for modelling and measurements, were significantly improved.

The idea (and the name) of GOTM as a community model was born in spring 1998, when Karsten Bolding joined the development. It was a major effort to collect the many different codes (each set up for only one test case), written in different programming languages, stored on different computers and merge them together into one product. In summer 1998, Manuel Ruiz Villarreal joined the GOTM developers for a few years. Later, Pierre-Philippe Mathieu carried out some changes which simplified the use of GOTM, such that he became GOTM author no. 4 for a few years (see photograph). 

![Bild](http://www.gotm.net/pics/gotmgroup.jpg)

_October 18-22, 1999 in Ispra, Italy for the CARTUM autumn school This shows the still small GOTM developers group with Karsten Bolding, Manuel Ruiz Villarreal, Hans Burchard and Pierre-Philippe Mathieu._

At this stage, the first version of GOTM was copied to the anonymous-ftp server of the Institute of Oceanography in Hamburg, Germany and started as a community model on May 1, 1999 as gotm1.0.

Shortly after all four early GOTM developers left the inspiring environment of the Lago Maggiore, Lars Umlauf met Hans Burchard and Karsten Bolding in Irkutsk at Lake Baikal, where Lars surprised them with a presentation showing that the k-epsilon model is flawed under breaking surface waves and that the k-omega model should be preferably used
([Umlauf et al., 2003)](https://www.sciencedirect.com/science/article/abs/pii/S1463500302000392). The following intensive vodka-fueled discussions finally led to the inclusion of the k-omega model into GOTM and, more importantly, to the inspiration to construct a "generic length scale" equation from which most of the existing two-equations models (e.g., Mellor-Yamada, k-epsilon, k-omega) can be recovered as special cases
[Umlauf and Burchard (2003)](https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=1008&context=journal_of_marine_research). The generic length-scale (GLS) model received a great push after being implemented into ROMS.

Another important addition by Lars Umlauf was the inclusions of the parametric KPP turbulence model in GOTM, mainly for comparison with the second-moment closures that are based on a rather different modeling philosophy. More recently, however, this implementation of the KPP model has been replaced by a coupling of GOTM with the turbulence modeling toolbox [CVMix](https://e3sm.org/wp-content/uploads/2018/03/ResearchHighlight_CVMix_V11.pdf), which contains an implementation of the KPP model that is often considered as a reference. Here, Qing Li stepped on the scence and played a key role [(see Li et al., 2021)](https://gmd.copernicus.org/articles/14/4261/2021). Qing's particular focus is the parameterization of Langmuir turbulence (LT) effects in ocean turbulence models (both KPP and second-moment closures), which has inspired numerous important extensions in GOTM. Qing's most recent extension is the inclusion of a bottom boundary mixing module for the KPP model in CVMix, making this model more suitable for shallow shelf, coastal and estuarine applications.     

![Bild](http://www.gotm.net/pics/gotm_net_hawaii.jpg)

_GOTM web address carved into a leaf on Hawaii during the Ocean Sciences Meeting 2006 in Honolulu_ 

Beyond these purely physics-based model developments, GOTM has also been coupled to biogeochemical models in a generic way (then called gotm-bio), including new numerical schemes for the dynamics of the sink and source terms to guarantee non-negativity of concentrations. In that stage, Jorn Bruggeman as a first-year PhD student in Biology joined the GOTM development after identifying weaknesses of these schemes and proposing improved numerics (such that now conservation could be achieved on the element level). Once engaged in GOTM, Jorn coded a graphical user interface (GUI) for GOTM, such that also non-UNIX people could use GOTM. Along with the GUI, a powerful graphical tool for displaying GOTM results had been written by Jorn. A lot of useful GOTM infrastructure has been added by Jorn such as the automatic generation of namelists.

Together with Karsten Bolding, Jorn developed then the Framework of Aquatic Biogeochemical Models ([FABM](http://sourceforge.net/projects/fabm/)) which was far more generic than the gotm-bio coupling in linking biogeochemical modules to GOTM and many other hydrodynamic drivers.

In recent years, GOTM has been extended towards a one-dimensional model for lakes by including the hypsometric effects. Here, besides Karsten Bolding and Jorn Bruggeman, also the new GOTM developer Knut Klingbeil has been very active in testing the code and making it more consistent. Through the nature of the GOTM project - and the interest of the active participants - the features of GOTM will change over time. This reflects the fact that the project is fundamentally driven by the participants and that only few resources have been available for targeted development. As a consequence the support for lake simluation using a hypsograph has been de facto abandoned. The lake branch was developed in parallel to the main branch, and a proper merge was never achieved. With all the newer developments in the main branch a merge will be very resource requiring.

To better link GOTM to ongoing developments in external software projects, the code structure has more recently incorporated the use of GIT *submodules*. The most important external projects integrated into GOTM with this approach are [CVMix](https://e3sm.org/wp-content/uploads/2018/03/ResearchHighlight_CVMix_V11.pdf) (see above) and the [TEOS-10](https://www.teos-10.org) thermodynamics toolbox which now forms the basis of all thermodynamic computations in GOTM. On a more technical level, the package [flexout](https://github.com/BoldingBruggeman/flexout) created by Jorn allows many flexible output option (different files with different variables at different temporal resolution).
More recently, the GOTM runtime configuration has shifted from standard Fortran namelists to [YAML](https://yaml.org) through a new [Fortran YAML handler](https://github.com/BoldingBruggeman/fortran-yaml), written by Jorn. Handling of namelists is limited to Fortran, whereas YAML can be interpreted by a number of additional languages, opening GOTM to new types of applications, e.g. ensemble simulations.




