from django.test import TestCase
from django.conf import settings
from override_settings import override_settings

# This is just a smoke test to make sure actually using
# override_settings in django TestCases still works.
#
# We're just testing the bare minimum.

class SimpleTest(TestCase):
    @override_settings(FOO="abc")
    def test_method_decorator(self):
        self.assertEqual(settings.FOO, "abc")

    def test_context_manager(self):
        self.assertRaises(AttributeError, getattr, settings, "FOO2")
        with override_settings(FOO2="abc"):
            self.assertEqual(settings.FOO2, "abc")
        self.assertRaises(AttributeError, getattr, settings, "FOO2")

@override_settings(FOO3="abc")
class SimpleTestClassOverride(TestCase):
    def test_exists(self):
        self.assertEqual(settings.FOO3, "abc")

    def test_exists(self):
        self.assertEqual(settings.FOO3, "abc")
