#!/usr/bin/env python
import os
from setuptools import setup, find_packages

version = '0.0.0'
dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, 'version.txt')) as f:
    version = f.read().strip()

setup(
    name='sigil',
    version=version,
    packages=find_packages(),
    package_data={'': ['version.txt']},
)
