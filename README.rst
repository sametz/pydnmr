pyDNMR (pre-alpha)
******************

pyDNMR simulates dynamic nuclear magnetic resonance (DNMR) spectra. A graphical user interface provides inputs for simulation parameters (frequencies, rate constants, line widths, and the population of various states), and displays the resulting spectrum.

The short-term goal of this project is to include the simulation for two coupled nuclei as well, and create platform-specific executable files ("apps") for educational use. For example, the rate constant for nuclear exchange can be adjusted up and down to show coalescence of signals.

The longer-term goal of this project is to add simulations for more complex systems, and to provide additional tools (e.g. matching experimental and simulated lineshapes) that would result in an application suitable for researchers as well as educators.

A secondary purpose of this project is to provide a test case for the author to learn how to properly test, package, and distribute software. Which leads to:

----

Installation and Use
====================

Everything outside the pydnmr/pydnmr folder is a work in progress, including setup.py and tests, and should not be trusted.

The brave and curious can copy the contents of the pydnmr/pydnmr folder, and run the program from the command line:

    ``python main.py``

----

Feedback
========
Disclaimer: the author is neither an NMR spectroscopist, nor a software engineer. I'm figuring this out as I go along. I welcome feedback on the project. If you think the simulation or the code could be improved upon, feel free to leave an issue on GitHub, or contact me by email (see setup.py for my current address).