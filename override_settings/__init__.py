import copy
import mock
from functools import wraps
from django.conf import global_settings, settings

SETTING_DELETED = mock.sentinel.SETTING_DELETED

class override_settings(object):
    def __init__(self, **kwargs):
        self.patcher = mock.patch('django.conf.settings._wrapped', **kwargs)

    def __call__(self, test_func):
        if isinstance(test_func, type):
            def _pre_setup(innerself):
                self.enable()
                test_func.setUp(innerself)
            def _post_teardown(innerself):
                test_func.tearDown(innerself)
                self.disable()

            # When decorating a class, we need to construct a new class
            # with the same name so that the test discovery tools can
            # get a useful name.
            inner = type(
                test_func.__name__,
                (test_func,),
                {
                    'setUp': _pre_setup,
                    'tearDown': _post_teardown,
                    '__module__': test_func.__module__,
                })
            return inner
        else:
            @wraps(test_func)
            def inner(*args, **kwargs):
                with self:
                    return test_func(*args, **kwargs)
            return inner

    def enable(self):
        self.mocked = self.patcher.start()
        return self.mocked

    def disable(self):
        self.patcher.stop()

    def __enter__(self):
        self.enable()

    def __exit__(self, exc_type, exc_value, traceback):
        self.disable()

def with_apps(*apps):
    """
    Class decorator that makes sure the passed apps are present in
    INSTALLED_APPS.
    """
    apps_set = set(settings.INSTALLED_APPS)
    apps_set.update(apps)
    return override_settings(INSTALLED_APPS=list(apps_set))

def without_apps(*apps):
    """
    Class decorator that makes sure the passed apps are not present in
    INSTALLED_APPS.
    """
    apps_list = [a for a in settings.INSTALLED_APPS if a not in apps]
    return override_settings(INSTALLED_APPS=apps_list)
