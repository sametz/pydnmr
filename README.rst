pyDNMR v0.2.0 (alpha)
*********************

.. image:: docs/source/pydnmrimg.png

`Documentation (.pdf)`_.

.. _Documentation (.pdf): docs/build/latex/pyDNMR.pdf
pyDNMR simulates dynamic nuclear magnetic resonance (DNMR) spectra. A graphical user interface provides inputs for simulation parameters (frequencies, rate constants, line widths, and the population of various states), and displays the resulting spectrum.

The current version of pyDNMR only includes the simulation for two uncoupled spin-1/2 nuclei undergoing exchange. The short-term goal of this project is to include the simulation for two coupled nuclei as well, and to create platform-specific executable files ("apps") for educational use. For example, the rate constant for nuclear exchange can be adjusted up and down to demonstrate coalescence of signals.

The longer-term goal of this project is to add simulations for more complex systems, and to provide additional tools (e.g. importation of NMR spectra, and matching experimental to simulated lineshapes) that would result in an application suitable for researchers as well as educators.

A secondary purpose of this project is to provide a test case for the author to learn how to properly test, package, and distribute software. Which leads to:

----

Installation and Use
====================

This is a work in progress. In the main branch, the main application (main.py)
and its dependencies in the pydnmr subfolder should provide a basic,
functional application. Everything else, including setup.py, should not be
trusted.

The brave and curious can copy main.py plus the pydnmr/pydnmr subfolder, and
run the program from the command line:

    ``python main.py``

----

TODO:
=====


Steps to a Version 1 release:

* Check PEP8/PEP257 compliance for code style

* Check that setup.py and requirements.txt allow another user to install the software.

* Use tox to test if pydnmr works with other Python verstions etc.

* Freeze the app, preferably as a 1-file executable, for OSX/Win/Unix.

See the CHANGELOG for the anticipated changes required to progress from alpha to beta to pre-release to Version 1.0.0.

----

Feedback
========
Disclaimer: the author is neither an NMR spectroscopist, nor a software engineer. I'm figuring this out as I go along. I welcome feedback on the project. If you think the simulation or the code could be improved upon, feel free to leave an issue on GitHub, or contact me by email (see setup.py for my current address).

----

Acknowledgements
================
This project is inspired by Hans Reich's WINDNMR application. I thank him for our conversations, and his sharing of WINDNMR's Visual Basic 6 code.
