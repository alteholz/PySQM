#!/usr/bin/env python

from distutils.core import setup

setup(name='pysqm',
      version='3.1',
      maintainer='Thorsten Alteholz',
      maintainer_email='python@alteholz.de',
      url='https://github.com/alteholz/PySQM',
      license='GPLv3',
      description='SQM reading and plotting software',
      packages=['pysqm'],
      install_requires=['pyephem','numpy','matplotlib'],
      classifiers=[
                   "Programming Language :: C",
                   "Programming Language :: Cython",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: Implementation :: CPython",
                   'Development Status :: 3 - Alpha',
                   "Environment :: Other Environment",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License (GPL)",
                   "Operating System :: OS Independent",
                   "Topic :: Scientific/Engineering :: Astronomy",
                   ],
      long_description=open('README.txt').read()
      )
