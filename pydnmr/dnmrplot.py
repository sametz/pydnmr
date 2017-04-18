"""
dnmrplot provides interfaces with the dnmrmath model that return simulation
data in a format suitable for plotting.
"""

import numpy as np

from .dnmrmath import dnmr_AB, d2s_func  # , TwoSinglets

# TODO: dnmrplot prefix is redundant. Consider refactor.


def dnmrplot_2spin(va, vb, k, wa, wb, percent_a):
    """
    Creates the spectrum data using the function nmrmath.d2s_func.
    :param va: The frequency of nucleus 'a' at the slow exchange limit
    :param vb: The frequency of nucleus 'b' at the slow exchange limit
    :param k: The rate of nuclear exchange
    :param wa: The width at half heigh of the signal for nucleus a (at the slow
    exchange limit).
    :param wb: The width at half heigh of the signal for nucleus b (at the slow
    exchange limit).
    :param percent_a: The fraction of the population in state a (vs. state b)
    :return: a tuple of numpy arrays for frequencies (x coordinate) and 
    corresponding intensities (y coordinate). Hard-coded for 800 data points 
    and a frequency range from vb-50 to va+50.
    """

    if vb > va:
        va, vb = vb, va
        wa, wb = wb, wa
        percent_a = 100 - percent_a
    l_limit = vb - 50
    r_limit = va + 50
    x = np.linspace(l_limit, r_limit, 800)
    # y = two_spin(x, va, vb, k, wa, wb, percent_a)

    # OR:

    dfunc = d2s_func(va, vb, k, wa, wb, percent_a / 100)
    y = dfunc(x)

    # OR:
    # y = reich(x, va, vb, k, wa, wb, percent_a)

    return x, y


def dnmrplot_AB(va, vb, j_ab, k_ab, wa):
    """
    Creates the spectrum data using the function nmrmath.dnmr_AB.
    :param va: The frequency of nucleus 'a' at the slow exchange limit
    :param vb: The frequency of nucleus 'b' at the slow exchange limit
    :param j_ab: The coupling constant between nuclei a and b
    :param k_ab: The rate of two-site exchange of nuclei a and b
    :param wa: The line width at the slow exchange limit
    :return: a tuple of numpy arrays for frequencies (x coordinate) and 
    corresponding intensities (y coordinate). Hard-coded for 800 data points 
    and a frequency range from vb-50 to va+50.
    """

    if vb > va:
        va, vb = vb, va  # dnmr_AB requires va > vb

    l_limit = vb - 50
    r_limit = va + 50
    x = np.linspace(l_limit, r_limit, 800)
    y = dnmr_AB(x, va, vb, j_ab, k_ab, wa)
    return x, y


# if __name__ == '__main__':
#     import plottools as pt
#
#     WINDNMR_DEFAULTS = (165.00, 135.00, 1.50, 0.50, 0.50, 50.00)
#     spectrum = dnmrplot_2spin(*WINDNMR_DEFAULTS)
#     pt.popplot(*spectrum)
