#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='Simple Binary Tree Implementation',
    version='1.1',
    description='Simple binary tree implementation',
    author='Brandon Doyle',
    author_email='bjd2385@aperiodicity.com',
    license='MIT',
    modules=['bt.bt'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)