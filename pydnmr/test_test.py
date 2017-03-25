"""Purpose: to see if any successful test of a module is possible."""

from .dnmrplot import dnmrplot_2spin


def test_if_anything_can_pass():
    assert True == True

# if __name__ == '__main__':
#     import plottools as pt
#
#     WINDNMR_DEFAULTS = (165.00, 135.00, 1.50, 0.50, 0.50, 50.00)
#     spectrum = dnmrplot_2spin(*WINDNMR_DEFAULTS)
#     pt.popplot(*spectrum)
