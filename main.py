"""
The main GUI application to be run from the command line.
"""

import sys
from collections import namedtuple

from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel, QDoubleSpinBox,
                             QApplication, QMainWindow)
from pyqtgraph import PlotWidget
# noinspection PyUnresolvedReferences
from pydnmr.dnmrplot import dnmrplot_2spin

# If testing TwoSinglets class, uncomment the next line:
# from dnmrmath import TwoSinglets

# Define the different types of input widgets that may be required.
# Currently all inputs are QDoubleSpinBox.
# Keys are for use with a dict that is sent to model as **kwargs.
# Strings are for labels.
# Value is for the inital QDoubleSpinBox default.
# Range is the range of values for the QDoubleSpinBox.
# RANGE MUST BE SET BEFORE VALUE

# Widget presets:
var = namedtuple('var', ['key', 'string', 'value', 'range'])
va = var(key='va', string='Va', value=165.00, range=(0.00, 10000.00))
vb = var(key='vb', string='Vb', value=135.00, range=(0.00, 10000.00))
k = var(key='k', string='k', value=1.50, range=(0.01, 1000.00))
wa = var(key='wa', string='Wa', value=0.50, range=(0.00, 100.00))
wb = var(key='wb', string='Wb', value=0.50, range=(0.00, 100.00))
percent_a = var(key='percent_a', string='%a', value=50.00, range=(0.00, 100.00))

# Each type of calculation will have its own ordering of input widgets:
twospin_vars = (va, vb, k, wa, wb, percent_a)

# further widget collections woudl appear hear for future calculation models


class dnmrGui(QMainWindow):
    """
    Create the GUI for the application.

    Currently the app features a single simulation model (two uncoupled
    spins), and so a single main window. TODO: as models are added, create a
    toggle between GUI windows tailored to each simulation (e.g. appropriate
    widgets for data entry)
    """

    def __init__(self, parent=None):

        super(dnmrGui, self).__init__(parent)

        self.simulation_vars = {}  # stores kwargs that model is called with

        self.setupUi()

    # TODO: determine why it's common to separate the following from __init__
    def setupUi(self):
        """
        Set up the GUI with the default moded, default variables,
        and simulated lineshape.
        """

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

            centralLayout.addWidget(wlabel, 0, i)
            centralLayout.addWidget(wbox, 1, i)

            # Using the lambda expression below allows extra information to
            # be passed to the self.update slot, allowing the delegator to
            # see who sent the signal, update the dictionary of model inputs,
            # call the model for a simulation result, and plot it. See:
            # https://mfitzp.io/article/transmit-extra-data-with-signals-in-pyqt/

            # noinspection PyUnresolvedReferences
            wbox.valueChanged.connect(
                lambda val, key=widget.key: self.update(key, val))

        graphicsView = PlotWidget()
        centralLayout.addWidget(graphicsView, 2, 0, 1, len(twospin_vars))
        # lets the graph span the entire width of the window, no matter how
        # many input widgets appear above

        centralWidget.setLayout(centralLayout)

        self.plotdata = graphicsView.plot()
        self.plotdata.getViewBox().invertX(True)  # Reverse x axis "NMR style"
        self.plotdata.setData(*self.call_model())

        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('pyDNMR')
        self.statusBar().showMessage('Ready')

    def call_model(self):
        """
        Send the dictionary as **kwargs to the model
        :return: a spectrum, consisting of a tuple of x and y coordinate arrays
        """
        x, y = dnmrplot_2spin(**self.simulation_vars)
        return x, y

    def update(self, key, val):
        """
        Detect a change in numerical input; record the change in
        the dictionary of widget values; call the model to get an updated
        spectrum; and plot the spectrum.
        :param key: the dictionary key for the variable associated with the
        signalling widget
        :param val: the current value of the signalling widget
        """
        self.simulation_vars[key] = val

        # Choose one of the following. TODO: speedtests to find fastest routine
        self.plotdata.setData(*self.call_model())  # original routine

        # OR:

        # spectrum = TwoSinglets(**self.simulation_vars).spectrum()
        # self.plotdata.setData(*spectrum)  # using new TwoSinglets class

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = dnmrGui()
    ui.show()
    sys.exit(app.exec_())
