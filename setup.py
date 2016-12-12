#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'schematics<=1.0.2',
    'six',
]

setup(name='schematics_extensions',
      packages=find_packages(exclude=['*.test', '*.tests']),
      version='0.1',
      description='Extensions for the Schematics library',
      author='Picwell',
      author_email='dev@picwell.com',
      url='http://github.com/picwell/schematics-extensions',
      install_requires=requirements,
      dependency_links=[],
      include_package_data=True)
