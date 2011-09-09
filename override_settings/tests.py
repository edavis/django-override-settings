from django.conf import settings
from django.test import TestCase
from override_settings import (
    override_settings, SETTING_DELETED, with_apps, without_apps)

@override_settings(FOO="abc")
class TestOverrideSettingsDecoratedClass(TestCase):
    """
    Provide a decorated class.
    """
    def test_override_settings_class_decorator(self):
        """
        Settings overwritten at the class level are available in each method.
        """
        self.assertEqual(settings.FOO, "abc")

    @override_settings(FOO="abc123")
    def test_override_settings_method_decorator(self):
        """
        Method level overrides overwrite class level overrides.
        """
        self.assertEqual(settings.FOO, "abc123")

    @override_settings(FOO="321")
    def test_override_settings_context_manager(self):
        """
        Context managers overwrite method and class level decorations.
        """
        with override_settings(FOO="xyz"):
            self.assertEqual(settings.FOO, "xyz")

    def test_decorated_testcase_module(self):
        """
        Make sure __name__ is correctly reported.
        """
        self.assertEqual(TestOverrideSettingsDecoratedClass.__module__, __name__)

class TestOverrideSettingsUndecoratedClass(TestCase):
    """
    Provide an undecorated class.
    """
    @override_settings(FOO="123")
    def test_override_settings_on_a_method(self):
        """
        Override settings can be used for an individual method.
        """
        self.assertEqual(settings.FOO, "123")

    def test_override_settings_as_context_manager(self):
        """
        Can use override_settings as a context manager.
        """
        with override_settings(FOO="321"):
            self.assertEqual(settings.FOO, "321")

class TestAppModifiers(TestCase):
    @with_apps('django.contrib.sites')
    def test_with_apps(self):
        """
        The `with_apps` decorator adds apps to INSTALLED_APPS.
        """
        self.assertTrue('django.contrib.sites' in settings.INSTALLED_APPS)

    @without_apps("django.contrib.sites")
    def test_without_apps(self):
        """
        The `without_apps` decorator removes apps from INSTALLED_APPS.
        """
        self.assertFalse('django.contrib.sites' in settings.INSTALLED_APPS)

@override_settings(DUMMY_OPTION=42)
class TestSettingDeleted(TestCase):
    def test_dummy_option_exists(self):
        """
        Deleted options should return after the context manager is finished.
        """
        self.assertEqual(settings.DUMMY_OPTION, 42)

        with override_settings(DUMMY_OPTION=SETTING_DELETED):
            self.assertRaises(AttributeError, getattr, settings, 'DUMMY_OPTION')

        self.assertEqual(settings.DUMMY_OPTION, 42)

    @override_settings(DUMMY_OPTION=SETTING_DELETED)
    def test_delete_dummy_option(self):
        """
        Can delete settings at the method level.
        """
        self.assertRaises(AttributeError, getattr, settings, 'DUMMY_OPTION')

    def test_dummy_option_exists_after_method_level_delete(self):
        """
        Make sure the option returns after deleting it at the method level.
        """
        self.assertEqual(settings.DUMMY_OPTION, 42)

class TestGlobalSettingsUnaffected(TestCase):
    @override_settings(DUMMY_OPTION=42)
    def test_global_settings_are_unaffected(self):
        """
        Ensure global settings aren't touched.

        We don't want the passed options to be the *only* settings
        set.  We check here for USE_ETAGS, defined in
        django.conf.global_settings and untouched by override_settings.
        """
        self.assertEqual(settings.DUMMY_OPTION, 42)
        self.assertTrue('USE_ETAGS' in dir(settings))
