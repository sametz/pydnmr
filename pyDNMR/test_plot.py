# TODO: turn into a proper unit test or discard
# PyCharm keeps refering to this file as 'SimplePlot', the name of the
# file it was copied from?!

# noinspection PyUnresolvedReferences
from PyQt5 import QtGui
import pyqtgraph as pg
from nmrplot import dnmrplot_2spin

WINDNMR_DEFAULT = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
x, y = dnmrplot_2spin(*WINDNMR_DEFAULT)
plt = pg.plot(x, y)
plt.show()


if __name__ == '__main__':
    pg.QtGui.QApplication.exec_()
