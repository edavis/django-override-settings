Development
-----------
* Use mock to provide fake django.conf.settings object
* Register with Travis CI
* Move tests outside of package
* Use tox to test various Python and Django versions
* Add tests for with/without apps when used as context managers
* Test a few different permutations of SETTING_DELETED

Version 1.2
-----------
* Much more robust handling of SETTING_DELETED

Version 1.1.1
-------------
* When decorating TestCases, display the original name in output
* Small typo fix in README
* Add test to make sure global settings are unaffected

Version 1.1
-----------
* Initial release
