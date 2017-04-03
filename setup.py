#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['ros_industrial_dashboard'],
    package_dir={'': 'src'},
    scripts=['scripts/dashboard']
)

setup(**d)
