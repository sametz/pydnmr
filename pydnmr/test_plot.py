# TODO: create meaningful tests that pass

from .dnmrplot import dnmrplot_2spin


def test_dnmrplot_2spin_type():

    WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
    x, y = dnmrplot_2spin(*WINDNMR_DEFAULT)
    print('x ', type(x), "y", type(y))
    assert type(x) == "<class 'numpy.ndarray'>"
    assert type(y) == "<class 'numpy.ndarray'>"


if __name__ == "__main__":
    import plottools as pt

    WINDNMR_DEFAULTS = (165.00, 135.00, 1.50, 0.50, 0.50, 50.00)
    spectrum = dnmrplot_2spin(*WINDNMR_DEFAULTS)
    pt.popplot(*spectrum)

