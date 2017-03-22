"""
There were problems with taking the initial main.py with machine-generated
GUI and refactoring for clarity. This module is a quick and dirty mock-up of
a main window, that will have GUI elements added to it gradually.
"""

import sys
from collections import namedtuple

from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel, QDoubleSpinBox,
                             QApplication, QMainWindow)
from pyqtgraph import PlotWidget
from nmrplot import dnmrplot_2spin

# Define the different types of input widgets that may be required.
# Currently all inputs are QDoubleSpinBox.
# Keys are for use with a dict that is sent to model as **kwargs.
# Strings are for labels.
# Value is for the inital QDoubleSpinBox default.
# Range is the range of values for the QDoubleSpinBox.
# RANGE MUST BE SET BEFORE VALUE

var = namedtuple('var', ['key', 'string', 'value', 'range'])
Va = var(key='Va', string='Va', value=165.00, range=(0.00, 10000.00))
Vb = var(key='Vb', string='Vb', value=135.00, range=(0.00, 10000.00))
k = var(key='k', string='kab + kba', value=1.50, range=(0.01, 1000.00))
Wa = var(key='Wa', string='Wa', value=0.50, range=(0.00, 100.00))
Wb = var(key='Wb', string='Wb', value=0.50, range=(0.00, 100.00))
percent_a = var(key='percent_a', string='%a', value=50.00, range=(0.00, 100.00))

# Each type of calculation has its own ordering of input widgets:
twospin_vars = (Va, Vb, k, Wa, Wb, percent_a)

# further widget collections woudl appear hear for future calculation models


class dnmrGui(QMainWindow):
    """
    Currently the app features a single model (two uncoupled spins) to
    simulate, and so a single main window. TODO: as models are added, create a
    toggle
    between GUI setups.
    """

    def __init__(self, parent=None):

        super(dnmrGui, self).__init__(parent)

        self.simulation_vars = {}  # stores kwargs that model is called with

        self.setupUi()

    def setupUi(self):

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralLayout = QGridLayout()
        # More complex layouts can be considered in future, e.g. a horizontal
        #  layout containing a serious of vertical layouts containing labels
        # and spinboxes.

        for i, widget in enumerate(twospin_vars):
            # The namedtuple construct facilitates widget generation:
            wlabel = QLabel(widget.string)
            wbox = QDoubleSpinBox()
            wbox.setRange(*widget.range)  # SET RANGE BEFORE VALUE
            wbox.setValue(widget.value)

            # populate the dictionary with initial simulation variables
            self.simulation_vars[widget.key] = widget.value

            # Choosing a grid layout simplifies construction of a horizontal
            # array of widgets:
            centralLayout.addWidget(wlabel, 0, i)
            centralLayout.addWidget(wbox, 1, i)

            # Using the lambda expression below allows extra information to
            # be passed to the self.update slot, allowing the delegator to
            # see who sent the signal, update the dictionary of model inputs,
            # call the model for a simulation result, and plot it.
            wbox.valueChanged.connect(
                lambda val, key=widget.key: self.update(key, val))

        # create the pyqtGraph widget for graphical output of the model's
        # spectrum
        graphicsView = PlotWidget()
        centralLayout.addWidget(graphicsView, 2, 0, 1, len(twospin_vars))
        # lets the graph span the entire width of the window, no matter how
        # many input widgets appear above

        centralWidget.setLayout(centralLayout)

        self.plotdata = graphicsView.plot()
        self.plotdata.setData(*self.call_model())

        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('Mock')
        self.statusBar().showMessage('Ready')

    def call_model(self):
        """
        Sends the dictionary as **kwargs to the mode
        :return: a spectrum of x and y coordinate arrays
        """
        x, y = dnmrplot_2spin(**self.simulation_vars)
        return x, y

    def update(self, key, val):
        """
        Slot detects change to numerical inputs; records the change in
        simulations_vars; calls the model to get an updated spectrum; and
        plots the spectrum.
        :param key: the key associated with the variable, forwarded by the
        signaling widget
        :param val: the current value of the signalling widget
        """
        self.simulation_vars[key] = val
        self.plotdata.setData(*self.call_model())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = dnmrGui()
    ui.show()
    sys.exit(app.exec_())
