#!/usr/bin/env python

from distutils.core import setup

setup(
    name='epub2',
    version='1.0',
    description='Build an EPUB2 file from Python scripts',
    author='yapper-git',
    author_email='yapper-git@users.noreply.github.com',
    url='https://github.com/yapper-git/python-epub2',
    py_modules=['epub2'],
    install_requires=['jinja2'],
)
