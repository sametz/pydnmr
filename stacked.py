"""
Cobbling together the skeleton for the next GUI version that will use a 
QStackedWidget to display various models
"""

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QStackedWidget,
                             QToolBar, QWidget, QLabel, QGridLayout,
                             QGroupBox, QRadioButton, QDockWidget,
                             QVBoxLayout, QListWidget)
from PyQt5.QtCore import Qt


class dnmrGui(QMainWindow):

    def __init__(self, parent=None):

        super(dnmrGui, self).__init__(parent)

        self.setObjectName('toplevel')

        self.setupUi()

    def setupUi(self):

        self.setupCentral()
        #self.setupDock()
        self.setupButtonToolBar()

    def setupCentral(self):

        stackedWidget = QStackedWidget()
        stackedWidget.setObjectName('centralwidget')
        self.setCentralWidget(stackedWidget)

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

        stackedWidget.addWidget(twosinglet)
        stackedWidget.addWidget(ab)

    def setupDock(self):
        leftdock = QDockWidget("leftdock", self)
        leftdock.setObjectName('leftdockwidget')

        # buttonbox = QGroupBox("Model")
        # twosingletbutton = QRadioButton('Two uncoupled spin-1/2 nuclei')
        # twosingletbutton.setChecked(True)
        # abbutton = QRadioButton('Two coupled spin-1/2 nuclei ("AB quartet)')
        # buttonboxlayout = QVBoxLayout()
        # buttonboxlayout.addWidget(twosingletbutton)
        # buttonboxlayout.addWidget(abbutton)
        # buttonboxlayout.addStretch(1)
        # buttonbox.setLayout(buttonboxlayout)

        # leftdocklayout.addWidget(buttonbox)
        # leftdock.setLayout(leftdocklayout)

        leftdock.setWidget(self.modelButtonGroup())
        self.addDockWidget(Qt.LeftDockWidgetArea, leftdock)

    def setupButtonToolBar(self):

        buttonbar = QToolBar()
        buttonbar.setObjectName('buttonbar')
        buttonbar.addWidget(self.modelButtonGroup())
        self.addToolBar(buttonbar)

    def modelButtonGroup(self):
        buttonbox = QGroupBox("Model")
        twosingletbutton = QRadioButton('Two uncoupled spin-1/2 nuclei')
        twosingletbutton.setChecked(True)
        abbutton = QRadioButton('Two coupled spin-1/2 nuclei ("AB quartet)')
        buttonboxlayout = QVBoxLayout()
        buttonboxlayout.addWidget(twosingletbutton)
        buttonboxlayout.addWidget(abbutton)
        buttonboxlayout.addStretch(1)
        buttonbox.setLayout(buttonboxlayout)

        return buttonbox


    def setupUiOld(self):

        stackedWidget = QStackedWidget()
        stackedWidget.setObjectName('centralwidget')
        self.setCentralWidget(stackedWidget)

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

        stackedWidget.addWidget(twosinglet)
        stackedWidget.addWidget(ab)


        leftdock = QDockWidget()
        leftdocklayout = QVBoxLayout()

        leftdocklayout.addWidget(self.createFirstExclusiveGroup())

        #buttongroup = QGroupBox()

        twosingletbutton = QRadioButton('Two uncoupled spin-1/2 nuclei')
        twosingletbutton.setChecked(True)
        abbutton = QRadioButton('Two coupled spin-1/2 nuclei ("AB quartet)')

        # leftdocklayout.addWidget(twosingletbutton)
        # leftdocklayout.addWidget(abbutton)

        #buttongroup.setLayout(leftdocklayout)

        leftdock.setLayout(leftdocklayout)

        #buttonbar = QToolBar()

        self.addDockWidget(Qt.LeftDockWidgetArea, leftdock)

        #buttonbar = QToolBar()
        #buttonbar.setLayout(leftdocklayout)

        #buttonbar.addWidget(buttongroup)

        #self.addToolBar(buttonbar)

        #buttonbar.addWidget(QLabel('button bar'))
        #buttonbar.addWidget()

    def createFirstExclusiveGroup(self):
        groupBox = QGroupBox("Exclusive Radio Buttons")

        radio1 = QRadioButton("&Radio button 1")
        radio2 = QRadioButton("R&adio button 2")
        radio3 = QRadioButton("Ra&dio button 3")

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = dnmrGui()
    ui.show()
    sys.exit(app.exec_())
