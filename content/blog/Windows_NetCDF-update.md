+++
author = "Karsten Bolding"
categories = []
date = "2017-11-25T12:00:00+02:00"
description = ""
draft = false
featured = ""
featuredalt = ""
featuredpath = ""
image = "blog/img/"
linktitle = ""
title = "Updated Windows NetCDF libraries"
type = "blog"

+++

Mainly for developers.

Updated NetCDF libraries for Windows. Still 3.6.3 but now both 32 and 64 bit are supported.

<!--more-->

Jorn Bruggeman has compiled the old NetCDF 3.6.3 version for both 32- and 64bit architectures. The FindNetCDF.cmake module has been updated to choose the correct library depending on how ifort is used.

