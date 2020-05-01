#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-01 17:05:53
# @Version : 0.0.1

from setuptools import setup

setup(
    name='py3lsd',
    version='0.0.1',
    description='py3lsd is the python bindings for LSD - Line Segment Detector',
    author='ShiKun Zhang',
    author_email='m15326861966@163.com',
    license='BSD',
    keywords="LSD",
    url='https://github.com/dakun333/py3lsd',
    packages=['pylsd', 'pylsd.bindings', 'pylsd.lib'],
    package_dir={'pylsd.lib': 'pylsd/lib'},
    package_data={'pylsd.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},
)
