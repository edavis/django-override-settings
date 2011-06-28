from distutils.core import setup

setup(
    name="django-override-settings",
    version="1.0.0",
    description="Allow settings to be overridden in Django tests",
    long_description=open('README.rst').read(),
    author="Jannis Leidel", author_email="jezdez@enn.io",
    maintainer="Eric Davis", maintainer_email="ed@npri.org",
    url="http://github.com/edavis/django-override-settings/",
    packages=['override_settings'],
    license='BSD',
)
