#!/usr/bin/env python
from setuptools import setup

setup(
    name='veryprettytable',
    version='0.8.1',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Topic :: Text Processing'
    ],
    license="BSD (3 clause)",
    description='A simple Python library for easily displaying tabular data in a visually appealing ASCII table format',
    author='Scott Blevins',
    author_email='sblevins@gmail.com',
    url='https://github.com/smeggingsmegger/VeryPrettyTable',
    py_modules=['veryprettytable'],
    install_requires=['termcolor', 'colorama']
)
