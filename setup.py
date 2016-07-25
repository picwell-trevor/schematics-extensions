#!/usr/bin/env python

from distutils.core import setup

requirements = [
    'schematics==1.1.1',
]

setup(name='schematics-extensions',
      version='0.0.5',
      description='Extensions for the Schematics library',
      author='Picwell',
      author_email='dev@picwell.com',
      url='http://github.com/picwell/schematics-extensions',
      packages=['schematics_extensions'],
      install_requires=requirements)
