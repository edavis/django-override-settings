========================
django-override-settings
========================

django-override-settings provides an easy way to override settings in
Django tests.

The ``override_settings`` class can be used as either a class or
method decorator or as a context manager to temporarily override the
values of settings.  After each test case has finished (when using it
as a decorator) or after the context manager has exited, it resets the
values in ``django.conf.settings`` to what they were before.  This prevents
side-effects from creeping in and lets each test case run in its own
sandbox.

This package also provides two convenience functions (``with_apps``
and ``without_apps``) to modify just ``INSTALLED_APPS`` as well as a
special object (``SETTING_DELETED``) to run tests without a given
setting defined.

The functionality in this package will eventually be superseded when
Django 1.4 is released as it will come with a built-in
``override_settings``.  But for those maintaining pre-1.4 codebases,
hopefully this package comes in handy.

Installation
------------

We're on PyPI_::

    pip install django-override-settings

.. _PyPI: http://pypi.python.org/pypi/django-override-settings

Usage
-----

If you have a bunch of tests that require a given setting, you can
decorate the class and each test case will use that value.  For
example::

    from django.conf import settings
    from django.test import TestCase
    from override_settings import override_settings

    @override_settings(FOO="abc")
    class TestFoo(TestCase):
        def test_foo(self):
            self.assertEqual(settings.FOO, "abc")

Or you can decorate a single test case and have it only apply on that
method::

    @override_settings(BAR="123")
    class TestBar(TestCase):

        @override_settings(BAR="abc")
        def test_bar(self):
            self.assertEqual(settings.BAR, "abc")

        def test_bar_no_decoration(self):
            self.assertEqual(settings.BAR, "123")

You can also use it as a context manager::

    class TestBar(TestCase):
        @override_settings(BAR="123")
        def test_bar(self):
            self.assertEqual(settings.BAR, "123")

            with override_settings(BAR="abc")
                self.assertEqual(settings.BAR, "abc")

            self.assertEqual(settings.BAR, "123")

To modify just ``INSTALLED_APPS``, use ``with_apps`` or
``without_apps``::

    from override_settings import with_apps, without_apps

    class TestAppModifiers(TestCase):
        @with_apps('django.contrib.humanize')
        def test_humanize(self):
            # ...

        @without_apps('django.contrib.sites')
        def test_no_sites(self):
            # ...

To run tests without a setting, use ``SETTING_DELETED``::

    from override_settings import override_settings, SETTING_DELETED

    class TestMissingSetting(TestCase):
        @override_settings(CUSTOM_OPTION=SETTING_DELETED)
        def test_delete_custom_option(self):
            """
            Useful to make sure a missing setting raises an Exception.
            """
            self.assertRaises(AttributeError, getattr, settings, 'CUSTOM_OPTION')

Requirements
------------

- Django >= 1.2

Thanks
------

- `Jannis Leidel`_ for both the `original snippet`_ and his work updating it
  to work when decorating TestCases as part of `Django proper`_.

- `Joost Cassee`_ for the idea of ``SETTING_DELETED`` as well as
  ``with_apps`` and ``without_apps`` as part of his django-analytical_
  project.

.. _Jannis Leidel: https://github.com/jezdez
.. _original snippet: http://djangosnippets.org/snippets/2437/
.. _Django proper: https://code.djangoproject.com/browser/django/trunk/django/test/utils.py
.. _Joost Cassee: https://github.com/jcassee
.. _django-analytical: https://github.com/jcassee/django-analytical

Contact
-------

If you notice any bugs, please `open a ticket`_.

.. _open a ticket: https://github.com/edavis/django-override-settings/issues
