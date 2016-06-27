# -*- coding: utf-8 -*-
#
# This file is part of Flask-AppFactory
# Copyright (C) 2015, 2016 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Flask-AppFactory is an dynamic application loader."""

import os
import re
import sys

from setuptools import setup
# Get the version string.  Cannot be done with import!
with open(os.path.join('flask_appfactory', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

tests_require = [
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest-runner>=2.7.0',
    'pytest>=2.8.0',
    'coverage>=4.0',
]

setup(
    name='Flask-AppFactory',
    version=version,
    description=__doc__,
    url='http://github.com/inveniosoftware/flask-appfactory/',
    license='BSD',
    author='Invenio Collaboration',
    author_email='info@invenio-software.org',
    long_description=open('README.rst').read(),
    packages=['flask_appfactory', 'flask_appfactory.ext', ],
    zip_safe=False,
    platforms='any',
    tests_require=tests_require,
    install_requires=[
        'Flask>=0.10',
        'Flask-Registry>=0.2.0',
        'Flask-CLI>=0.2.1',
    ],
    extras_require={
        'celery': ['Flask-CeleryExt>=0.1.0'],
        'docs': ['Sphinx'],
        'tests': tests_require,
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
)
