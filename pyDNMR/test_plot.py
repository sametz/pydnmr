
from PyQt5 import QtGui
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
from nmrplot import dnmrplot_2spin
#plt = pg.plot(np.random.normal(size=100), title="Simplest possible plotting
# example")
reichdefault = (165.00, 135.00, 1.50, 0.50, 0.50, 0.5000)
x, y = dnmrplot_2spin(*reichdefault)
plt = pg.plot(x, y)
plt.show()
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()