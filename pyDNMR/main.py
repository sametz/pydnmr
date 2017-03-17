# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_named.ui'
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
        self.appGridLayout = QtWidgets.QGridLayout()
        self.appGridLayout.setContentsMargins(11, 11, 11, 11)
        self.appGridLayout.setSpacing(6)
        self.appGridLayout.setObjectName("appGridLayout")
        self.widgets_layout = QtWidgets.QHBoxLayout()
        self.widgets_layout.setContentsMargins(11, 11, 11, 11)
        self.widgets_layout.setSpacing(6)
        self.widgets_layout.setObjectName("widgets_layout")
        self.va_layout = QtWidgets.QVBoxLayout()
        self.va_layout.setContentsMargins(11, 11, 11, 11)
        self.va_layout.setSpacing(6)
        self.va_layout.setObjectName("va_layout")
        self.va_label = QtWidgets.QLabel(self.centralWidget)
        self.va_label.setObjectName("va_label")
        self.va_layout.addWidget(self.va_label)
        self.va_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.va_box.setObjectName("va_box")
        self.va_layout.addWidget(self.va_box)
        self.widgets_layout.addLayout(self.va_layout)
        self.vb_layout = QtWidgets.QVBoxLayout()
        self.vb_layout.setContentsMargins(11, 11, 11, 11)
        self.vb_layout.setSpacing(6)
        self.vb_layout.setObjectName("vb_layout")
        self.vb_label = QtWidgets.QLabel(self.centralWidget)
        self.vb_label.setObjectName("vb_label")
        self.vb_layout.addWidget(self.vb_label)
        self.vb_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.vb_box.setObjectName("vb_box")
        self.vb_layout.addWidget(self.vb_box)
        self.widgets_layout.addLayout(self.vb_layout)
        self.k_layout = QtWidgets.QVBoxLayout()
        self.k_layout.setContentsMargins(11, 11, 11, 11)
        self.k_layout.setSpacing(6)
        self.k_layout.setObjectName("k_layout")
        self.k_label = QtWidgets.QLabel(self.centralWidget)
        self.k_label.setObjectName("k_label")
        self.k_layout.addWidget(self.k_label)
        self.k_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.k_box.setObjectName("k_box")
        self.k_layout.addWidget(self.k_box)
        self.widgets_layout.addLayout(self.k_layout)
        self.wa_layout = QtWidgets.QVBoxLayout()
        self.wa_layout.setContentsMargins(11, 11, 11, 11)
        self.wa_layout.setSpacing(6)
        self.wa_layout.setObjectName("wa_layout")
        self.wa_label = QtWidgets.QLabel(self.centralWidget)
        self.wa_label.setObjectName("wa_label")
        self.wa_layout.addWidget(self.wa_label)
        self.wa_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.wa_box.setObjectName("wa_box")
        self.wa_layout.addWidget(self.wa_box)
        self.widgets_layout.addLayout(self.wa_layout)
        self.wb_layout = QtWidgets.QVBoxLayout()
        self.wb_layout.setContentsMargins(11, 11, 11, 11)
        self.wb_layout.setSpacing(6)
        self.wb_layout.setObjectName("wb_layout")
        self.wb_label = QtWidgets.QLabel(self.centralWidget)
        self.wb_label.setObjectName("wb_label")
        self.wb_layout.addWidget(self.wb_label)
        self.wb_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.wb_box.setObjectName("wb_box")
        self.wb_layout.addWidget(self.wb_box)
        self.widgets_layout.addLayout(self.wb_layout)
        self.percent_a_layout = QtWidgets.QVBoxLayout()
        self.percent_a_layout.setContentsMargins(11, 11, 11, 11)
        self.percent_a_layout.setSpacing(6)
        self.percent_a_layout.setObjectName("percent_a_layout")
        self.percent_a_label = QtWidgets.QLabel(self.centralWidget)
        self.percent_a_label.setObjectName("percent_a_label")
        self.percent_a_layout.addWidget(self.percent_a_label)
        self.percent_a_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.percent_a_box.setObjectName("percent_a_box")
        self.percent_a_layout.addWidget(self.percent_a_box)
        self.widgets_layout.addLayout(self.percent_a_layout)
        self.rightHz_layout = QtWidgets.QVBoxLayout()
        self.rightHz_layout.setContentsMargins(11, 11, 11, 11)
        self.rightHz_layout.setSpacing(6)
        self.rightHz_layout.setObjectName("rightHz_layout")
        self.righthz_label = QtWidgets.QLabel(self.centralWidget)
        self.righthz_label.setObjectName("righthz_label")
        self.rightHz_layout.addWidget(self.righthz_label)
        self.righthz_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.righthz_box.setObjectName("righthz_box")
        self.rightHz_layout.addWidget(self.righthz_box)
        self.widgets_layout.addLayout(self.rightHz_layout)
        self.wdthHz_layout = QtWidgets.QVBoxLayout()
        self.wdthHz_layout.setContentsMargins(11, 11, 11, 11)
        self.wdthHz_layout.setSpacing(6)
        self.wdthHz_layout.setObjectName("wdthHz_layout")
        self.wdthHz_label = QtWidgets.QLabel(self.centralWidget)
        self.wdthHz_label.setObjectName("wdthHz_label")
        self.wdthHz_layout.addWidget(self.wdthHz_label)
        self.wdthHz_box = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.wdthHz_box.setObjectName("wdthHz_box")
        self.wdthHz_layout.addWidget(self.wdthHz_box)
        self.widgets_layout.addLayout(self.wdthHz_layout)
        self.appGridLayout.addLayout(self.widgets_layout, 0, 0, 1, 1)
        self.graphicsView = PlotWidget(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.appGridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.appGridLayout, 0, 0, 1, 1)
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
        for widget in (self.va_box,
                       self.vb_box,
                       self.k_box,
                       self.wa_box,
                       self.wb_box,
                       self.percent_a_box):
            widget.valueChanged['double'].connect(self.update_graph)

        self.plotdata = self.graphicsView.plot()
        self.update_graph()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.va_label.setText(_translate("MainWindow", "Va"))
        self.va_box.setRange(0.00, 10000.00)
        self.va_box.setValue(165.00)
        self.vb_label.setText(_translate("MainWindow", "Vb"))
        self.vb_box.setRange(0.00, 10000.00)
        self.vb_box.setValue(135.00)
        self.k_label.setText(_translate("MainWindow", "kab + kba"))
        self.k_box.setValue(1.50)
        self.k_box.setRange(0.00, 1000.00)
        self.wa_label.setText(_translate("MainWindow", "Wa"))
        self.wa_box.setValue(0.50)
        self.wb_label.setText(_translate("MainWindow", "Wb"))
        self.wb_box.setValue(0.50)
        self.percent_a_label.setText(_translate("MainWindow", "%a"))
        self.percent_a_box.setValue(50.00)
        self.righthz_label.setText(_translate("MainWindow", "Right-Hz"))
        self.wdthHz_label.setText(_translate("MainWindow", "WdthHz"))

    def call_model(self):
        model_input = (self.va_box.value(),
                       self.vb_box.value(),
                       self.k_box.value(),
                       self.wa_box.value(),
                       self.wb_box.value(),
                       self.percent_a_box.value() / 100.0)
        x, y = dnmrplot_2spin(*model_input)
        return x, y

    def update_graph(self):
        self.plotdata.setData(*self.call_model())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

