#!/usr/bin/env python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'override_settings.test_settings'

def main():
    from django.test.simple import DjangoTestSuiteRunner
    runner = DjangoTestSuiteRunner(verbosity=2)
    runner.run_tests(['override_settings'])

if __name__ == "__main__":
    main()
