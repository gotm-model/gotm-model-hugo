+++
title = "Check NetCDF library availability" 
draft = false
author = "Karsten Bolding"
date = "2019-08-01T00:00:00+02:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

By far the most frequent issue arising when people want to build GOTM is NetCDF.
We have included a small script that can be used to test if NetCDF requirements are fulfilled.

<!--more-->

The script is only useable for Linux and Mac users as the NetCDF libraries are included for Windows.

Since NetCDF 4.4.1 a utility called - *nf-config* - is installed alongside the libraries. This utility is used by the GOTM CMake configuration to include necessary compile and link information (1).

So first thing is to check the availability of *nf-config*:

```
command -v nf-config
```

If *nf-config* exists we can continue to the next test - can CMake actually find the NetCDF libraries. You must be in the GOTM main folder when executing this command.

```
cmake -P extern/flexout/cmake/Modules/FindNetCDF.cmake
```

If the latter command writes - among other things - Found NetCDF - it is safe to proceed with the configuration and compilation of GOTM.

If the command fails steps must be taken to remedy the problem. How - is beyond this mailing list.

The above have been put in a small script with some additional information written to the terminal. The script is execuated as:

```
./check_netcdf.sh
```

1) There is another way of specifying the information but that is only for very old systems - before 4.4.1 - or in other special cases.


