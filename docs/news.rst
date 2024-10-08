News
====

Version 0.8.1 (in development)
------------------------------

* Python 3.10, 3.11, 3.12, 3.13.

* CI(GHActions): Install all Python and PyPy versions from ``conda-forge``.

* CI(GHActions): Switch to ``setup-miniconda``.

* Tests: Use ``pytest.fixture``.

Version 0.8.0 (2021-09-24)
--------------------------

* Python 3.8, Python 3.9.

* GitHub Actions.

* Stop testing at Travis CI.

* Stop testing at AppVeyor.

Version 0.7.0 (2019-02-01)
--------------------------

* Python 3.7.

* Drop support for Python 3.3.

Version 0.6.1 (2017-12-15)
--------------------------

* Fix rm.py: do not ask to remove read-only files when -f is active.

Version 0.6.0 (2017-12-13)
--------------------------

* rm.py ask interactively to remove read-only files or directories.

* Add options -s --silent --quiet for cmp.py.

* Add option -f for rm.py.

* PyPy.

Version 0.5.0 (2017-07-09)
--------------------------

* Add option -r for rm.py.

* Use remove-old-files.py to cleanup pip cache.

Version 0.4.0 (2017-06-04)
--------------------------

* Add package 'ppu'.

* Add module ppu/find_executable.py.

* Add script which.py.

Version 0.3.2 (2017-05-01)
--------------------------

* Convert README to reST.

Version 0.3.1 (2017-04-30)
--------------------------

* Fix release: build scripts with '/usr/bin/env python'

Version 0.3.0 (2017-04-30)
--------------------------

* Move cmp.py, remove-old-files.py and rm.py to scripts directory.

* Release at PyPI.

Version 0.2.0 (2017-04-30)
--------------------------

* Add cmp.py and rm.py.

* Test at Travis and AppVeyor.

* Use subprocess.call() instead of os.system().

0.1.0 (2017-04-16)
------------------

* Remove empty directories.

* Add installation instructions.

0.0.1 (2017-04-16)
------------------

* Initial release.
