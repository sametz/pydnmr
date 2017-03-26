"""
dnmrplot provides interfaces with the dnmrmath model that return simulation
data in a format suitable for plotting.
"""

import numpy as np

# Uncomment ', TwoSinglets' if testing that optional function
# noinspection PyUnresolvedReferences
from .dnmrmath import dnmr_AB, d2s_func  # , TwoSinglets


def dnmrplot_2spin(va, vb, k, wa, wb, percent_a):
    """
    Creates the spectrum data using the function nmrmath.two_spin.
    Currently assumes va > vb.
    Returns: tuple of arrays for x and y coordinates
    """

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


def dnmrplot_AB(v1, v2, J, k, w):
    """
    plots the function nmrmath.dnmr_AB.
    Currently assumes va > vb
    """

    l_limit = v2 - 50
    r_limit = v1 + 50
    x = np.linspace(l_limit, r_limit, 800)
    y = dnmr_AB(x, v1, v2, J, k, w)
    return x, y


if __name__ == '__main__':
    import plottools as pt

    WINDNMR_DEFAULTS = (165.00, 135.00, 1.50, 0.50, 0.50, 50.00)
    spectrum = dnmrplot_2spin(*WINDNMR_DEFAULTS)
    pt.popplot(*spectrum)
