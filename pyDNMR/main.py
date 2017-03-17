# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from nmrplot import dnmrplot_2spin


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 531)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_2.addWidget(self.doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout_4.addWidget(self.doubleSpinBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.verticalLayout_5.addWidget(self.doubleSpinBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.verticalLayout_6.addWidget(self.doubleSpinBox_5)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.verticalLayout_7.addWidget(self.doubleSpinBox_6)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.verticalLayout_8.addWidget(self.doubleSpinBox_7)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.verticalLayout_9.addWidget(self.doubleSpinBox_8)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.graphicsView = PlotWidget(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 831, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.graphicsView.plot(*twoSingletSpectrum().call_model())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #twoSingletSpectrum()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Va"))
        self.label_2.setText(_translate("MainWindow", "Vb"))
        self.label_3.setText(_translate("MainWindow", "kab + kba"))
        self.label_4.setText(_translate("MainWindow", "Wa"))
        self.label_5.setText(_translate("MainWindow", "Wb"))
        self.label_6.setText(_translate("MainWindow", "%a"))
        self.label_7.setText(_translate("MainWindow", "Right-Hz"))
        self.label_8.setText(_translate("MainWindow", "WdthHz"))


class twoSingletSpectrum:
    """Creates spectrum data that can be used by pyqtGraph"""

    def __init__(self):
        reichdefault = (165.00, 135.00, 1.50, 0.50, 0.50, 50.00)
        self._Va = reichdefault[0]
        self._Vb = reichdefault[1]
        self._ka = reichdefault[2]
        self._Wa = reichdefault[3]
        self._Wb = reichdefault[4]
        self._pa = reichdefault[5] / 100
        #self.update_graph()

    def update_graph(self):
        #Ui_MainWindow.graphicsView.plot(*self.call_model())
        print(type(Ui_MainWindow.graphicsView))

    def call_model(self):
        x, y = dnmrplot_2spin(self._Va, self._Vb, self._ka, self._Wa,
                              self._Wb, self._pa)
        return x, y


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

