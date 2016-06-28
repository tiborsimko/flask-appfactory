# -*- coding: utf-8 -*-
#
# This file is part of Flask-AppFactory
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Flask-AppFactory is an dynamic application loader."""

import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    """Integration of PyTest with setuptools."""

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        """Initialize options."""
        TestCommand.initialize_options(self)
        try:
            from ConfigParser import ConfigParser
        except ImportError:
            from configparser import ConfigParser
        config = ConfigParser()
        config.read("pytest.ini")
        self.pytest_args = config.get("pytest", "addopts").split(" ")

    def finalize_options(self):
        """Finalize options."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run tests."""
        # import here, cause outside the eggs aren't loaded
        import pytest
        import _pytest.config
        pm = _pytest.config.get_plugin_manager()
        pm.consider_setuptools_entrypoints()
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

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
    'pytest>=2.6.1',
    'coverage<4.0a1',
]

setup(
    name='Flask-AppFactory',
    version=version,
    description=__doc__,
    url='http://github.com/inveniosoftware/flask-appfactory/',
    license='BSD',
    author='Invenio Collaboration',
    author_email='info@inveniosoftware.org',
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
    },
    cmdclass={'test': PyTest},
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
