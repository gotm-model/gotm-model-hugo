+++
showonlyimage = false
draft = false
image = "/portfolio/img/software.png"
date = "2016-11-05T18:25:22+05:30"
title = "Software"
weight = 2
author = "Karsten Bolding"
+++

GOTM is relative easy to install and run on most operating systems - just follow the instructions carefully.

<!--more-->

1. The source code for GOTM and [FABM](http://www.fabm.net) must have been cloned from the Git repositories - [GOTM](https://github.com/gotm-model/code) and [FABM](https://github.com/fabm-model/fabm) - respectively. The actual cloning will depend on the platform and Git-utilities used. Further information is provide [here](https://help.github.com/articles/cloning-a-repository/). A number of graphical frontends to Git are available - but the use of these is beyond the instructions provided here.
2. A Fortran compiler supporting at least Fortran 2003 must be avaialble
   * On Linux [gfortran](https://gcc.gnu.org/fortran/) versions including and above 4.7 have been tested as well has the [Intel Fortran compiler](https://software.intel.com/en-us/fortran-compilers).
   * On Windows the [Intel Fortran compiler](https://software.intel.com/en-us/fortran-compilers) configured with VisualStudio is working.
3. [NetCDF](http://www.unidata.ucar.edu/software/netcdf)
   * On Linux/Mac GOTM and NetCDF must be compiled with the same Fortran compiler. The configuration and compilation of the NetCDF library is beyond the purpose of this guide.
   * On Windows NetCDF is provided in the repository - compatible with the Intel Fortran compiler
4. [CMake](http://www.cmake.org) must be installed. CMake is used to configure the compilation and generate native build systems - i.e. Make-based systems on Linux/Mac and VisualStudio on Windows. CMake can be run in command-line and GUI-mode. Further information is provided [here](https://cmake.org/documentation/). A detailed description is beyond the purpose of this guide. CMake advocates *out of source compilation* i.e. the actual compilation is separated from the source code. To facilitate this the use of a temporary build directory is encouraged.

Only when the above 4 points are checked it makes sense to proceed.

The GOTM executable can be configured in a number of ways depending on the intended use. This configuration is controlled by CMake - and its configuration file provided as part of the GOTM source code. The different configuration options have sensible default values so a fully functional executable can be obtained with very little configuration. On the other hand detailed control of included features, installation path etc. is also possible.


-  [Linux/Mac](/software/linux/)
-  [Windows](/software/windows/)

