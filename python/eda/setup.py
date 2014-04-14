#!/usr/bin/env python

from setuptools import setup, find_packages

packages = ['eda.' + p for p in find_packages('eda', exclude=['test', 'test*', '*.t'])]
packages.append('eda')

#packages=['eda', 'eda.components', 'eda.components.ST', 'eda.circuits'],
    
setup(
    name='EDA',
    version='1.0.1',
    author='Paweł Wodnicki',
    author_email='pawel@32bitmicro.com',
    url='https://github.com/32bitmicro/EDA/',
    license='BSD 3-clause',
    description='EDA for generative design.',
    test_suite='eda.tests.gen_test',
    packages=packages
)
