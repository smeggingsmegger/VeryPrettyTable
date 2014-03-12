#!/usr/bin/env python
from setuptools import setup

setup(
    name='prettytable',
    version='0.8.1',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Topic :: Text Processing'
    ],
    license="BSD (3 clause)",
    description='A simple Python library for easily displaying tabular data in a visually appealing ASCII table format',
    author='Luke Maurits',
    author_email='luke@maurits.id.au',
    url='http://code.google.com/p/prettytable',
    py_modules=['prettytable'],
    test_suite = "prettytable_test",
    install_requires=['termcolor', 'colorama']
)
