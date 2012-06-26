#!/usr/bin/env python

import sys
from distutils.core import setup, Command

cmdclass = {}

# class TestCommand(Command):
#     description = "run package tests"
#     user_options = [
#         # Use None because 'v' would conflict with global verbose option
#         ("verbosity=", None, "Django test runner verbosity level. [default=1]"),
#     ]

#     def initialize_options(self):
#         self.verbosity = 1

#     def finalize_options(self):
#         self.verbosity = int(self.verbosity)

#     def run(self):
#         from override_settings.run_tests import run_tests
#         sys.exit(run_tests(self.verbosity))

# cmdclass['test'] = TestCommand

setup(
    name             = "django-override-settings",
    version          = "1.2",
    author           = "Eric Davis",
    author_email     = "ed@npri.org",
    description      = "Provide a way to override Django's settings when running tests",
    long_description = open('README.rst').read(),
    url              = "http://github.com/edavis/django-override-settings/",
    packages         = ['override_settings'],
    cmdclass         = cmdclass,
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
