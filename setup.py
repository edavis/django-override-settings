#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name             = "django-override-settings",
    version          = "1.2",
    author           = "Eric Davis",
    author_email     = "ed@npri.org",
    description      = "Provide a way to override Django's settings when running tests",
    long_description = open('README.rst').read(),
    url              = "http://github.com/edavis/django-override-settings/",
    packages         = ['override_settings'],
    install_requires = ['mock==1.0b1'],
    classifiers      = [
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ],
)
