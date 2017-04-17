"""
Cobbling together the skeleton for the next GUI version that will use a 
QStackedWidget to display various models
"""

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QStackedWidget,
                             QToolBar, QWidget, QLabel, QGridLayout,
                             QRadioButton, QVBoxLayout, QButtonGroup)
from PyQt5.QtCore import Qt


class dnmrGui(QMainWindow):

    def __init__(self, parent=None):

        super(dnmrGui, self).__init__(parent)

        self.setObjectName('toplevel')

        self.setupUi()

    def setupUi(self):

        self.setupCentral()
        self.setupButtonToolBar()
        self.stackedWidget.setCurrentIndex(0)

    def setupCentral(self):

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setObjectName('centralwidget')
        self.setCentralWidget(self.stackedWidget)

        twosinglet = QWidget()
        twosinglet.setObjectName('twosinglet')
        twosingletlayout = QGridLayout()
        twosingletlayout.setObjectName('twosingletlayout')
        twosingletlayout.addWidget(QLabel('two singlets'))

        ab = QWidget()
        ab.setObjectName('ab')
        ablayout = QGridLayout()
        ablayout.setObjectName('ab layout')
        ablayout.addWidget(QLabel('AB layout'))

        twosinglet.setLayout(twosingletlayout)
        ab.setLayout(ablayout)

        self.stackedWidget.addWidget(twosinglet)
        self.stackedWidget.addWidget(ab)

    def setupButtonToolBar(self):

        buttonbar = QToolBar()
        buttonbar.setObjectName('buttonbar')
        buttonbar.addWidget(self.modelButtonGroup())
        self.addToolBar(Qt.LeftToolBarArea, buttonbar)

    def modelButtonGroup(self):
        """
        A widget of radio buttons that will determine which QStackedWidget is
        displayed.
        """

        # It seems that in order for the buttonClicked signal to work,
        # self.ButtonGroup and not ButtonGroup is necessary. Does not work
        # with out 'self.' prefix!!!

        ModelsWidget = QWidget()
        ModelsLayout = QVBoxLayout()
        self.ButtonGroup = QButtonGroup()

        twosingletbutton = QRadioButton('Two uncoupled spin-1/2 nuclei')
        twosingletbutton.setChecked(True)
        self.ButtonGroup.addButton(twosingletbutton, 0)

        abbutton = QRadioButton('Two coupled spin-1/2 nuclei ("AB quartet)')
        self.ButtonGroup.addButton(abbutton, 1)

        self.ButtonGroup.buttonClicked[int].connect(self.switchdisplay)

        ModelsLayout.addWidget(twosingletbutton)
        ModelsLayout.addWidget(abbutton)
        ModelsWidget.setLayout(ModelsLayout)

        return ModelsWidget

    def switchdisplay(self, id):
        print('button %d has been pressed' % id)
        self.stackedWidget.setCurrentIndex(id)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = dnmrGui()
    ui.show()
    sys.exit(app.exec_())
