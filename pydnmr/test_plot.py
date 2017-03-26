import numpy as np
from . import testdata
from .dnmrplot import dnmrplot_2spin


def test_dnmrplot_2spin_slowexchange():

    WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 50.00)
    x, y = dnmrplot_2spin(*WINDNMR_DEFAULT)
    accepted_x, accepted_y = testdata.TWOSPIN_SLOW
    np.testing.assert_array_almost_equal(x, accepted_x)
    np.testing.assert_array_almost_equal(y, accepted_y)


def test_dnmrplot_2spin_coalesce():

    WINDNMR_DEFAULT = (165.00, 135.00, 65.9, 0.50, 0.50, 50.00)
    x, y = dnmrplot_2spin(*WINDNMR_DEFAULT)
    accepted_x, accepted_y = testdata.TWOSPIN_COALESCE
    np.testing.assert_array_almost_equal(x, accepted_x)
    np.testing.assert_array_almost_equal(y, accepted_y)


def test_dnmrplot_2spin_fastexchange():

    WINDNMR_DEFAULT = (165.00, 135.00, 1000.00, 0.50, 0.50, 50.00)
    x, y = dnmrplot_2spin(*WINDNMR_DEFAULT)
    accepted_x, accepted_y = testdata.TWOSPIN_FAST
    np.testing.assert_array_almost_equal(x, accepted_x)
    np.testing.assert_array_almost_equal(y, accepted_y)
# if __name__ == "__main__":
#     import plottools as pt
#
#     WINDNMR_DEFAULTS = (165.00, 135.00, 1.50, 0.50, 0.50, 50.00)
#     spectrum = dnmrplot_2spin(*WINDNMR_DEFAULTS)
#     pt.popplot(*spectrum)

