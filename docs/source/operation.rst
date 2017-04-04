Using pyDNMR
============

.. image:: appwindow.*
   :width: 6.5 in

Entering Parameters
-------------------

Numerical values for :math:`\nu_A , \nu_B, k_A, W_A,
W_B`, and % A can be entered into the fields at the top of the application
window. The calculations assume units of Hz or s\ :superscript:`-1` for the
first five. The final entry is the population of site A expressed as a
percentage (rather than as the fraction (:math:`p_A`) used in the previous
section's formulas).

Mouse Controls
--------------

Clicking on the up/down arrows, or scrolling with the mouse wheel
while the field's contents are active, raises/lowers the values inside in
increments of 1.

Inside the plot of the spectrum:

* Left click and drag moves the plot.

* Scroll up/down zooms in/out.

* Right click and drag expands/contracts the spectrum horizontally/vertically.

* Right click currently opens up menus of options that have not been fully tested yet. These options are built into the third-party pyqtgraph library that pyDNMR imports.