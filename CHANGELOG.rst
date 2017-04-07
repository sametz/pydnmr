##########
Change Log
##########

All notable changes to this project will be documented in this file.

The format is inspired by `Keep a Changelog <http://keepachangelog.com/en/0.3.0/>`_ and tries to adhere to `Semantic Versioning <http://semver.org>`_
. The author interprets the terms below as follows:

* **pre-alpha status**: the app runs, but there is no formal unit or functional testing.


* **alpha status**: pre-alpha, plus implementation of unit and functional tests.


* **beta status**: alpha, plus documentation, implementation of all anticipated Version 1.0.0 features, and setup routines.


* **release candidate status**: beta, plus standalone executable(s).


* **Version 1.0.0 release**: a minimal app suitable for educational use and not requiring execution from the command line interface.


0.4.0 - 2017-04-04 (alpha)
--------------------------

Added
^^^^^

* Specific versions for the dependencies in requirements.txt

* Instructions on installing the software as stand-alone apps and as executable python code.

* Tox tests

* toxlog.txt is a diary of steps that were required to get tox tests to work.

Removed
^^^^^^^

* setup.py -- this app should not be "pip installed" like a library.

* mock.py no longer required for GUI testing. References to it removed from test_main.py.

0.3.0 - 2017-04-04 (alpha)
--------------------------

Added
^^^^^

* Stand-alone executable files (no Python required) included for Windows and Mac OS X

* Documentation implemented with Sphinx. Link to Sphinx-generated documentation (PDF) added to README.rst.

* Screenshots added to documentation and README.rst.

* freezelog.txt is a diary of the steps that were required to get PyInstaller to work.

Changed
^^^^^^^

* GUI appearance and widget labels

* Acceleration added to numerical entries' increment/decrement functionality


0.2.0 - 2017-03-29 (alpha release)
----------------------------------

Added
^^^^^
* Functional tests for all core files (main.py, dnmrmath.py, dnmrplot.py). Output for dnmrmath/dnmrplot were compared to simulations from the chemical literature, and output from Hans Reich's WINDNMR program, and then saved as tests/testdata.py. Test suites will refer to this file, or future equivalents, to test the current application's output vs. accepted results.

* A mock.py file was added for use with functional tests. This file should be functionally equivalent to main.py, and is scheduled for deletion prior to Version 1.0.0.

Changed
^^^^^^^
* The main app, main.py, was moved to the top level of the pydnmr directory. Required modules dnmrmath and dnmrplot remain in the pydnmr/pydnmr subdirectory. Tests and test-related files were moved to the pydnmr/tests directory.

* Linewidths Wa and Wb have a minimum value of 0.01 set in the GUI to prevent divide-by-zero errors (this same limitation for k was already implemented in the pre-alpha).

* The method used to calculate the lineshape was changed (to dnmrmath.d2s_func), which should provide a modest speed boost (rigorous testing and of alternative math methods and speed optimization is still required).

Bug Fixes
^^^^^^^^^
* The frequencies do not have to be in a particular order to produce an accurate plot, or to set the width of the spectral window. Previously, Va had to be greater than Vb.

* A potential bug with the currently preferred calculation method in dnmrmath (d2s_func) was squashed before it could cause problems.


0.1.0 - 2017-03-23 (pre-alpha release)
--------------------------------------

Initial Commit
