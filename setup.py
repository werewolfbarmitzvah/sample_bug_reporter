#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sample_bug_report',
    version='1.0.0',
    description='Scripts to generate bug reports',
    packages=find_packages(exclude=['tests']),
    install_requires=['jira',
                      'argparse',
                      'xmltodict'],
)
