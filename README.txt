

This repository has been moved to codeberg and is now available at

    https://codeberg.org/alteholz/PySQM.git





PySQM
=====

PySQM is a multi-platform, open-source software designed to read and
plot data from Unihedron SQM-LE and SQM-LU photometers, giving as 
an output files with the 'International Dark Sky Association (IDA) 
NSBM Community Standards for Reporting Skyglow Observations' format
(http://www.darksky.org/night-sky-conservation/248).

PySQM is distributed under GNU GPL, either version 3 of the License, 
or (at your option) any later version. See the file LICENSE.txt for details.

This software has been developed by Mireia Nievas <mnievas@ucm.es> with
the invaluable help of:

 - Sergio Pascual (UCM)
 - Jaime Zamorano (UCM)
 - Laura Barbas (OAN)
 - Pablo de Vicente (OAN)

The initial port to Python3 has been done by Anthony Tekatch (Unihedron).

SETUP
=====

After downloading the software, you need to modify the file config.py. 
In this file you will find several variables that need to be configured
to match your hardware settings. For example:

 - Location of the observatory (geographical coordinates).
 - Device identifier.
 - Device address (either IP address for SQM-LE or COM/ttyUSB port).
 - Location of the data files.
 - Axis limits for the plot.

Remember that python (2.7) syntax is mandatory in this file


HOW TO USE THE SOFTWARE
=======================

After configuring the software, make sure you are in the parent directory were
the README, LICENSE and MANIFEST files are located
> ls 
LICENSE.txt  MANIFEST.in  README.txt  pysqm  config.py  setup.py

And then run the software.
> python -m pysqm 

The program should find your SQM device and the data adquisition.will start 
(if it's night-time). 

In some systems, where python3 is the default version of python, you need 
to specify python2 as the interpreter to use. This is done usually running 
it as:

> python2 -m pysqm

or

> python2.7 -m pysqm

Note: running the setup.py script is neither tested nor required.
The program is currently being redesigned as a normal python package, but at 
present no setup is required.


HOW IT WORKS
============

In a first step, the program tries to connect to the SQM photometer and takes
some 'tests' measures (metadata/information, calibration and data) to check 
that the device is working as expected. 

After that, the program begins data acdquisition. In each iteration, it checks 
whether it is night-time. In that case new data is taken. 

Each N measurements, the main program calls a plotting function to generate 
a graphical representation of the current nightly data.


PySQM known issues
==================

Non-ASCII characters are not supported in the config.py file. Please, avoid using 'ñ', accented vowels, etc.
In headless systems, such as the Raspberry PI, if you run the program without X, you may suffer from the following fatal error when the program tries to generate the plot:

This application failed to start because it could not find or load the Qt platform plugin “xcb”.
Available platform plugins are: eglfs, kms, linuxfb, minimal, minimalegl, offscreen, xcb.
Reinstalling the application may fix this problem.  Aborted (core dumped)

In order to avoid this problem, you need to create (or modify if the file exists) in your HOME directory the following file: 

.config/matplotlib/matplotlibrc

You just need to set the matplotlib backend to Agg:
backend : Agg

Save the changes and exit. Now, PySQM should make the plots without issues. You may need to restart PySQM to apply the changes.

Path to EXE files (windows only):
https://www.dropbox.com/s/xlbr6ktk8spjsse/PySQM.exe?dl=0

CHANGELOG
=========

v0.3:
    Added datacenter option (optional, disabled by default)

v0.2:
    ...

v0.1:
    ...

