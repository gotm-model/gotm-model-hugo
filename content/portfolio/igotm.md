+++
author = "Jorn Bruggeman and Karsten Bolding"
date = "2018-02-05T00:00:00+02:00"
description = ""
draft = true
image = "portfolio/img/igotm.png"
showonlyimage = false
title = "iGOTM"
weight = 25

+++

Selecting a geographical position using Google Maps and optionally adjusting position and depth clicking 'Simulate' will make an one year GOTM simulation for year 2016 with results presented in the browser.

Try it out [here](https://igotm.bolding-bruggeman.com).

<!--more-->

### The technical details ...

iGOTM uses [nginx](https://nginx.org/en/) as frontend webserver. Nginx distibutes simulation tasks to a [tornado](http://www.tornadoweb.org/en/stable/) server that is responsible for the actual GOTM simulation via a [python](http://www.python.org/) wrapper around the Fortran based GOTM executable. Plots are fed back to Nginx for presentation.

iGOTM uses a secure connection using [LetsEncrypt](https://letsencrypt.org/) issued certificates.

All plots use the [cmocean](https://matplotlib.org/cmocean/) color maps.

### So why did we do it?

Because we can - and because in the future complex simulations will be controlled via web-interfaces where many technical details will be hidden from the user and she can concentrate on the science.

The iGOTM homepage will be expanded with additional features in the future - like e.g. user selected simulation period, additional configuration options, download of model set-ups.

