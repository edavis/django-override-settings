#!/usr/bin/env python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'override_settings.test_settings'

def run_tests(verbosity=1):
    from django.test.simple import DjangoTestSuiteRunner
    runner = DjangoTestSuiteRunner(verbosity=verbosity)
    return runner.run_tests(['override_settings'])
