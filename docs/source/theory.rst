Theory
======

The current version of pyDNMR simulates the case of two-site exchange for
uncoupled spin-1/2 nuclei. Other simple systems that do not require a quantum-mechanical treatment will be introduced after a stable Version 1 distribution is finished.

Sandström [#f1]_ shows how a formula for calculating the intensity
(:math:`\textrm{v}`) at frequency :math:`\nu` can be derived from the Bloch
equations. [#f2]_ The formula:

.. math::
    \textrm{v} = -C_0\frac{\bigg\{P\bigg[1+\tau\Big(\dfrac{p_B}{T_{2A}}+\dfrac{p_B}{T_{2B}}\Big)\bigg]+Q R\bigg\}}{P^2+R^2}

requires the calculation of paramaters P, Q, and R:

.. math::

    &P=\tau\bigg[\frac{1}{T_{2A} \cdot T_{2B}}-4\pi^2\Delta\nu^2+\pi^2(\delta\nu)^2\bigg]+\frac{p_A}{T_{2A}}+\frac{p_B}{T_{2B}}\\
    &Q=\tau[2\pi\Delta\nu-\pi\delta\nu(p_A-p_B)]\\
    &R=2\pi\Delta\nu\bigg[1+\tau\Big(\frac{1}{T_{2A}}+\frac{1}{T_{2B}}\Big)\bigg]+\pi\delta\nu\tau\Big(\frac{1}{T_{2B}}-\frac{1}{T_{2A}}\Big)
    +\pi\delta\nu(p_A-p_B)

These in turn require calculations for :math:`\tau , \delta \nu \mbox{, and }
\Delta \nu`, as well as determining the transverse relaxation times
:math:`T_2`.

Calculating :math:`\tau` requires knowing the fractional populations of
nuclei in each state (:math:`p_{A/B}`), and one of the rate constants :math:`k` for an exchange process.

.. math::

    \tau=\frac{p_A}{k_B}=\frac{p_B}{k_A}

where :math:`p_A+p_B=1 \mbox{, and } \frac{d[A]}{dt}=-k_A[A]`.

:math:`\delta \nu` is the difference in frequencies for nuclei at site A versus site B, at the slow exchange limit:

.. math::
    \delta \nu = \nu_A-\nu_B

and :math:`\Delta \nu` is the difference between the average of (i.e.
midpoint between) :math:`\nu_A` and :math:`\nu_B`, and the frequency
:math:`\nu` along the spectrum that the signal intensity :math:`\textrm{v}` is being
calculated at.

.. math::
    \Delta \nu = 0.5(\nu_A+\nu_B)-\nu

Although the :math:`T_2` s for the nuclei at sites A and B could be determined experimentally, in practice they are usually estimated from the width of the peaks at half height, at the slow exchange limit (:math:`W_{0A/B}`).

.. math::
    T_{2A}=\dfrac{1}{\pi W_{0A}}\mbox{; } T_{2B}=\dfrac{1}{\pi W_{0B}}


So, the experimental parameters required to simulate a lineshape are:

* :math:`\nu_A` and :math:`\nu_B` at the slow-exchange limit
* linewidths :math:`W_{0A}` and :math:`W_{0B}` at the slow-exchange limit
* the population :math:`p_A` of one of the sites, and
* the rate constant :math:`k_A` for the rate of exchange from site A to site B

.. rubric:: Footnotes
.. [#f1] Sandström, J. *Dynamic NMR Spectroscopy;* Academic Press: New York, 1982.

.. [#f2] The use of :math:`\textrm{v}` for intensity is retained from Sandström, despite its resemblance to :math:`\nu` . The simulated lineshape will be a plot of :math:`\textrm{v}` vs. :math:`\nu` !