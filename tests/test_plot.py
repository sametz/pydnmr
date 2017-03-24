# Currently not functional. Tried to use the path modification from The
# Hitchhiker's Guide to Python to get imports within test folder to work,
# but no dice. This has been a problem with other projects.
# TODO: find why tests in this folder can'timport project modules

# PyCharm keeps refering to this file as 'SimplePlot', the name of the
# file it was copied from?!

# noinspection PyUnresolvedReferences

import pytest
from .context import pydnmr

def test_dnmrplot_2spin_type():

    WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
    x, y = pydnmr.dnmrplot.dnmrplot_2spin(*WINDNMR_DEFAULT)
    assert type(x) == 'list'  # should fail b/c it's a numpy array


# if __name__ == '__main__':
#
#     import pyqtgraph as pg
#     WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
#     x, y = pydnmr.nmrplot.dnmrplot_2spin(*WINDNMR_DEFAULT)
#     plt = pg.plot(x, y)
#     plt.show()
if __name__ == '__main__':
    # for key in pydnmr.__dict__:
    #     print(key, pydnmr.__dict__[key])
    pydnmr.dnmrplot()