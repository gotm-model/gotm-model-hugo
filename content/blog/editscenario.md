+++
title = "EditScenario and friends" 
draft = false
author = "Karsten Bolding"
date = "2019-09-13T10:00:00+02:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

Updated status on September 13. 2019.

Updated status on EditScenario and friends. Jorn has an Python3 only laptop. It made an incentive to update some of the tools making it easier to handle GOTM.

<!--more-->

### Status on Python

I use Intels Python distribution - with mixed feelings - and lately when I've done Python sysadm I've started to reciecve messages about ending support. We have also tested how the tools work with package-manager installed Python3 on debian based distributions - with success.

On Windows we suggest to use Anaconda as Python distribution.

From [here](https://www.python.org/dev/peps/pep-0373/#maintenance-releases) it is also clear the Python2 is approaching the end:
```
The End Of Life date (EOL, sunset date) for Python 2.7 has been moved five years into the future, to 2020. 
```


In combination with Jorns new Python3 only laptop it made it clear that steps were needed in order to be able to operate GOTM in the usual way also after January 1. 2020. This has lead to a number of changes in the python code so basic functionallity is available both in Python2 and Python3. 
It has also lead to the fact that certain features are only available in Python2. These are typically GUI related extra features. 

Good news is that the different packages are available from PyPi and are as easy to install as:

```
pip install <package_name> [--user]  
```
   
For further information see [PyPi](https://pypi.org/)

### Status on packages


|&nbsp;| Name     |&nbsp;&nbsp;  Py2 &nbsp;&nbsp; | &nbsp;&nbsp; Py3 &nbsp;&nbsp; |
|----|----------|:-----:|:-----:|
|    | _xmlstore_     |   x   |   x   |
|    | _xmlplot_      |   x   |   x   |
|    | _editscenario_ |   x   |   x<sup>1</sup>   |
|    | _gotmgui_      |   x   |       |
|    | _pygotm_<sup>2</sup>       |   x   |   x   |
|    | _PyNcView_<sup>3</sup>     |   x   |   x   |  
|&nbsp;|                |                   |       |  

In principle Python is platform independent and we have tested on Mac, Linux and Windows but there are so many things that can influence compatability that there is no guarantee that it will work on all computers.

1. The graphical part of _editscenario_ - i.e viewing GOTM [_time-series_](https://github.com/fabm-model/fabm/wiki/GOTM#depth-independent-variables) and [_profiles_](https://github.com/fabm-model/fabm/wiki/GOTM#depth-dependent-variables) - will likely not work with Python3. 
2. We have not uploaded _pygotm_ to PyPi yet (as of the release of this blog). As _pygotm_ is not a pure Python package it also includes a shared library basically containing all the functionality of GOTM. _pygotm_ will in principle work with Python3 - _import pygotm_ will produce no errors - but as _gotmgui_ will not work with Python3 the usefullness will be very limited.
3. Maintaining _PyNcView_ is time consuming but has turned out to be quite essential to our daily workflow. Jorn has as a consequence upgraded _PyNcView_ to work in Python3.

Some of the tools require _PyQt_ 4 or 5, or _PySide_. Installing these is beyond this blog.

So the short message of this blog is really:
```
pip install pyncview <--user>
```

Futher development will only provide support for Python3.

