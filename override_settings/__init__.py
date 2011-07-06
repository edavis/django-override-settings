from __future__ import with_statement
from django.conf import settings, UserSettingsHolder
from django.utils.functional import wraps

SETTING_DELETED = object()

# Backported from Django trunk (r16377)
class override_settings(object):
    """
    Temporarily override Django settings.

    Acts as either a decorator, or a context manager.  If it's a decorator it
    takes a function and returns a wrapped function.  If it's a contextmanager
    it's used with the ``with`` statement.  In either event entering/exiting
    are called before and after, respectively, the function/block is executed.
    """
    def __init__(self, **kwargs):
        self.options = kwargs
        self.wrapped = settings._wrapped

    def __enter__(self):
        self.enable()

    def __exit__(self, exc_type, exc_value, traceback):
        self.disable()

    def __call__(self, test_func):
        from django.test import TestCase
        if isinstance(test_func, type) and issubclass(test_func, TestCase):
            class inner(test_func):
                def _pre_setup(innerself):
                    self.enable()
                    super(inner, innerself)._pre_setup()
                def _post_teardown(innerself):
                    super(inner, innerself)._post_teardown()
                    self.disable()
        else:
            @wraps(test_func)
            def inner(*args, **kwargs):
                with self:
                    return test_func(*args, **kwargs)
        return inner

    def enable(self):
        settings._wrapped = None
        new = [(k, v) for (k, v) in self.options.iteritems() \
                   if v is not SETTING_DELETED]
        settings.configure(**dict(new))

    def disable(self):
        settings._wrapped = self.wrapped

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
