"""A placeholder to remind how imports for tests within the test folder must 
work."""
from pydnmr import dnmrplot

def test_testing_from_inside_test_folder():

    WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
    x, y = dnmrplot.dnmrplot_2spin(*WINDNMR_DEFAULT)
    print('x ', type(x), "y", type(y))
    assert type(x) == type(y)
