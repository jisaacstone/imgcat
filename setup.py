#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='imgcat',
    version='0.1',
    description='cat an image to text',
    author='jisaacstone',
    author_email='jisaacstone+pyton@gamil.com',
    license='MIT',
    scripts=['imgcat'],
    requires=['PIL'])
