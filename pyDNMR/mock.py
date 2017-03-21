"""
There were problems with taking the initial main.py with machine-generated
GUI and refactoring for clarity. This module is a quick and dirty mock-up of
a main window, that will have GUI elements added to it gradually.
"""

import sys
from collections import namedtuple

# Import widgets separately for simpler names
from PyQt5 import QtCore  # , QtWidgets
from PyQt5.QtWidgets import (QWidget, QGridLayout, QHBoxLayout, QVBoxLayout,
                            QLabel, QDoubleSpinBox, QMenuBar, QToolBar,
                            QStatusBar, QApplication, QMainWindow)
from pyqtgraph import PlotWidget
from nmrplot import dnmrplot_2spin

var = namedtuple('var', ['key', 'string', 'value', 'range'])
Va = var(key='Va', string='Va', value=165.00, range=(0.00, 10000.00))
Vb = var(key='Vb', string='Vb', value=135.00, range=(0.00, 10000.00))
k = var(key='k', string='kab + kba', value=1.50, range=(0.00, 1000.00))
Wa = var(key='Wa', string='Wa', value=0.50, range=(0.00, 100.00))
Wb = var(key='Wb', string='Wb', value=0.50, range=(0.00, 100.00))
percent_a = var(key='percent_a', string='%a', value=50.00, range=(0.00, 100.00))
twospin_vars = (Va, Vb, k, Wa, Wb, percent_a)


class modelFrame(QHBoxLayout):
    """
    A horizontal layout designed to hold a series of child widgets that provide
    inputs for a model, detects when any of the children are updated, pings the
    model for the simulation data, and tells  the graphics window to plot
    the data.
    """

    def __init__(self, parent=None):
        super(modelFrame, self).__init__(parent)

    def onChildUpdate(self):
        pass


def boxer(label, value):
    return label, value

def va_box():
    va_layout = QVBoxLayout()
    va_layout.setContentsMargins(11, 11, 11, 11)
    va_layout.setSpacing(6)
    va_layout.setObjectName("va_layout")
    va_label = QLabel("Va")
    va_label.setObjectName("va_label")
    va_layout.addWidget(va_label)
    va_box = QDoubleSpinBox()
    va_box.setObjectName("va_box")
    va_layout.addWidget(va_box)

    return va_layout



class dnmrGui(QMainWindow):

    def __init__(self, parent=None):
        super(dnmrGui, self).__init__(parent)

        self.widget_list = ['Va', 'Vb', 'k', 'Wa', 'Wb']
        self.data = {'Va': (165.00, (0.00, 10000.00)),
                'Vb': (135.00, (0.00, 10000.00)),
                'k': (1.50, (0.00, 1000.00)),
                'Wa': (0.50, (0.00, 100.00)),
                'Wb': (0.50, (0.00, 100.00))}


        self.setupUi()

    def setupUi(self):

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralLayout = QGridLayout()

        # for i, widget in enumerate(self.widget_list):
        #     wlabel = QLabel(widget)
        #     wbox = QDoubleSpinBox()
        #
        #     lo, hi = self.data[widget][1]
        #     wbox.setRange(lo, hi)
        #     wbox.setValue(self.data[widget][0])
        #
        #     centralLayout.addWidget(wlabel, 0, i)
        #     centralLayout.addWidget(wbox, 1, i)

        for i, widget in enumerate(twospin_vars):
            wlabel = QLabel(widget.string)
            wbox = QDoubleSpinBox()
            wbox.setRange(*widget.range)
            wbox.setValue(widget.value)
            centralLayout.addWidget(wlabel, 0, i)
            centralLayout.addWidget(wbox, 1, i)
            wbox.valueChanged['double'].connect(lambda val,
                                                key=widget.key:
                                                self.update_graph(key, val))

        # modelBar = modelFrame()
        # modelBar.addLayout(va_box())
        thing1 = QLabel('Thing 1')
        thing2 = QLabel('Thing 2')
        # modelBar.addWidget(thing1)
        # modelBar.addWidget(thing2)

        graphicsView = PlotWidget()

        #centralLayout.addLayout(modelBar, 0, 0, 1, 1)
        # centralLayout.addWidget(thing1, 0, 0, 1, 1)
        # centralLayout.addWidget(thing2, 0, 1, 1, 1)
        centralLayout.addWidget(graphicsView, 2, 0, 1, len(twospin_vars))
        centralWidget.setLayout(centralLayout)

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Mock')
        self.statusBar().showMessage('Ready')

    def update_graph(self, key, val):

        source = self.sender()
        if key:
            print(key, val, source.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = dnmrGui()
    ui.show()
    sys.exit(app.exec_())