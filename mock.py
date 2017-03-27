"""Mock of main GUI for developing test_main GUI tests"""

import sys
from collections import namedtuple

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                             QLabel, QDoubleSpinBox)

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
wa = var(key='wa', string='Wa', value=0.50, range=(0.01, 100.00))
wb = var(key='wb', string='Wb', value=0.50, range=(0.01, 100.00))
percent_a = var(key='percent_a', string='%a', value=50.00, range=(0.00, 100.00))

# Each type of calculation will have its own ordering of input widgets:
twospin_vars = (va, vb, k, wa, wb, percent_a)

# further widget collections woudl appear hear for future calculation models


class dnmrGui(QMainWindow):
    def __init__(self, parent=None):
        super(dnmrGui, self).__init__(parent)

        self.simulation_vars = {}  # stores kwargs that model is called with
        self.setObjectName('toplevel')
        self.setupUi()

    def setupUi(self):
        """
                Set up the GUI with the default moded, default variables,
                and simulated lineshape.
                """

        centralWidget = QWidget()
        centralWidget.setObjectName('centralwidget')
        self.setCentralWidget(centralWidget)

        centralLayout = QGridLayout()
        self.setObjectName('centrallayout')
        # More complex layouts can be considered in future, e.g. a horizontal
        #  layout containing a serious of vertical layouts containing labels
        # and spinboxes.

        for i, widget in enumerate(twospin_vars):
            # The namedtuple construct facilitates widget generation:
            wlabel = QLabel(widget.string)
            wlabel.setObjectName(widget.key + '_label')
            wbox = QDoubleSpinBox()
            wbox.setObjectName(widget.key)
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

        centralWidget.setLayout(centralLayout)

        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('pyDNMR')

        # va_box_fetch = self.findChild(QDoubleSpinBox, 'va')
        # print("I found: ", va_box_fetch.objectName())
        # print('Its parent is: ', va_box_fetch.parent().objectName())
        # va_cw_fetch = self.findChild(QWidget, 'centralwidget')
        # print('I found: ', va_cw_fetch.objectName())
        # print('Its parent is: ', va_cw_fetch.parent().objectName())
        # print('Its type is: ', type(va_cw_fetch.parent()))
        # print('Is this the same as "self"?', va_cw_fetch.parent() is self)


        def update(self, key, val):
            pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = dnmrGui()
    ui.show()
    sys.exit(app.exec_())
