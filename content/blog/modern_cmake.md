+++
title = "Modern CMake and sub-modules" 
draft = false
author = "Karsten Bolding"
date = "2019-06-16T12:00:00+02:00"
image = "blog/img/"
categories = []
description = ""
linktitle = ""
featured = ""
featuredpath = ""
featuredalt = ""
type = "blog"
+++

We have re-written the CMake configuration file(s) to be in line with principles of Modern CMake. In addition - using these principles - we have moved code pieces not part of _essential_ GOTM out into individual projects.

<!--more-->

### Modern CMake

Modern CMake is about _targets_ and _properties_ and provides a model for creating re-usable software components easy integratable with each other. In order to fully benefit from this we re-wrote the old monolithic _CMakeLists.txt_ to a series of smaller and easier to handle configuration files.

A minimum CMake version of 3.0 is required.

### Using _Git_ submodules

A number of software components are used by FABM, GOTM and GETM (and 3rd party software projects as well). Cross maintaining these components across different use cases has some times been a hassle and resulted in reduced progress. Utilising the Modern CMake principles and _Git_'s submodule facility we have now moved shared code componets out of GOTM.

So far - _yaml_, _flexout_ and _fabm_ are submodules in GOTM.

The submodules are full clones of the respective repositories - we have put the code in the _extern_ folder in the GOTM root folder.

As a consequence of adding FABM as a submodule it is not necessery to specify FABM_BASE anymore.


#### GOTM code already cloned
From a users point of view we have made the transition very smooth and in general things should work just out of the box. There is one small caveat though - when updating the GOTM source code using _git pull_ - an additional argument must be provided to also update the submodules.


```
git pull
```

becomes

```
git pull --recurse-submodules
```

Using the following setting:
```
git config  submodule.recurse true
```
_git pull_ will in the future automatically also update the submodules.

During the update of the code a warning might be issued. The reason is that before the command to configure via CMake was e.g.:
```
cmake ~/GOTM/code/src
```

This has now been changed to:
```
cmake ~/GOTM/code
```

i.e. _src/_ is dropped and we are using _CMakeLists.txt_ in the main GOTM folder.

It is possible to get rid of the warning by editing the _CMakeCache.txt_ in the build directory as follows:

```
sed -i -e "s#/code/src#/code#" CMakeCache.txt
```
followed by:
```
cmake -c CMakeCache.txt
```

#### New GOTM clone
When making a new clone it is important to add options to inform _Git_ about the submodules. This is done like:


```
git clone https://github.com/gotm-model/code.git
git submodule update --init --recursive
```

With _git_ 1.7.3 and up the commands can be combined to one:

```
git clone --recurse-submodules https://github.com/gotm-model/code.git
```
When the code is cloned the instructions just given above can be used.
