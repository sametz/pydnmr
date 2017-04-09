"""
Cobbling together the skeleton for the next GUI version that will use a 
QStackedWidget to display various models
"""

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QStackedWidget,
                             QToolBar, QWidget, QLabel, QGridLayout,
                             QGroupBox, QRadioButton, QDockWidget, QPushButton,
                             QVBoxLayout, QListWidget, QButtonGroup)
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
        buttonbar.addWidget(self.modelButtonGroup2())
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

    def modelButtonGroup2(self):
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
        # buttonboxlayout = QVBoxLayout()


        #print(ButtonGroup.button(0).text())
        self.ButtonGroup.buttonClicked[int].connect(self.switchdisplay)
        ModelsLayout.addWidget(twosingletbutton)
        ModelsLayout.addWidget(abbutton)
        ModelsWidget.setLayout(ModelsLayout)

        return ModelsWidget

    def modelButtonGroup3(self):

        buttonwidget = QWidget()
        layout = QVBoxLayout()

        self.buttongroup = QButtonGroup()
        #self.buttongroup.setExclusive(True)
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QRadioButton("Button 1")
        self.buttongroup.addButton(button, 1)
        layout.addWidget(button)
        button.setChecked(True)

        button = QRadioButton("Button 2")
        self.buttongroup.addButton(button, 2)
        layout.addWidget(button)

        button = QRadioButton("Button 3")
        self.buttongroup.addButton(button, 3)
        layout.addWidget(button)

        buttonwidget.setLayout(layout)

        return buttonwidget

    def modelButtonGroup4(self):

        ModelsWidget = QWidget()
        ModelsLayout = QVBoxLayout()
        self.buttongroup = QButtonGroup()

        twosingletbutton = QRadioButton('Two uncoupled spin-1/2 nuclei')
        twosingletbutton.setChecked(True)
        self.buttongroup.addButton(twosingletbutton, 0)
        abbutton = QRadioButton('Two coupled spin-1/2 nuclei ("AB quartet)')
        self.buttongroup.addButton(abbutton, 1)
        # buttonboxlayout = QVBoxLayout()


        #print(ButtonGroup.button(0).text())
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
        ModelsLayout.addWidget(twosingletbutton)
        ModelsLayout.addWidget(abbutton)
        ModelsWidget.setLayout(ModelsLayout)

        return ModelsWidget

    def on_button_clicked(self, buttonid):
        print(buttonid)
        button = self.buttongroup.button(buttonid)
        print("%s was clicked!" % (button.text()))

    def switchdisplay(self, id):
        print('button %d has been pressed' % id)
        self.stackedWidget.setCurrentIndex(id)

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
