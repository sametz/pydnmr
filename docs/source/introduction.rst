Introduction to pyDNMR v0.2.0 (alpha)
=====================================


pyDNMR simulates dynamic nuclear magnetic resonance (DNMR) spectra. A graphical user interface provides inputs for simulation parameters (frequencies, rate constants, line widths, and the population of various states), and displays the resulting spectrum.

The current version of pyDNMR only includes the simulation for two uncoupled spin-1/2 nuclei undergoing exchange. The short-term goal of this project is to include the simulation for two coupled nuclei as well, and to create platform-specific executable files ("apps") for educational use. For example, the rate constant for nuclear exchange can be adjusted up and down to demonstrate coalescence of signals.

The longer-term goal of this project is to add simulations for more complex systems, and to provide additional tools (e.g. importation of NMR spectra, and matching experimental to simulated lineshapes) that would result in an application suitable for researchers as well as educators.

A secondary purpose of this project is to provide a test case for the author to learn how to properly test, package, and distribute software.