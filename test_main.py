import sys
import pytest
from PyQt5.QtWidgets import QApplication, QDoubleSpinBox, QLabel
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

import mock as main

app = QApplication(sys.argv)

class TestMainGUi:

    def setup(self):
        self.ui = main.dnmrGui()

    def test_title(self):
        """The user launches the app and sees that it is named 'pyDNMR'"""
        app_title = self.ui.windowTitle()
        assert app_title == 'pyDNMR'

    def test_two_siglet_all_widgets_exist(self):
        """The user sees 5 labels and 5 'double spin box' numerical entries 
        corresponding to the 5 inputs needed for the simulation.
        """

        for widget in main.twospin_vars:
            found_box = self.ui.findChild(QDoubleSpinBox, widget.key)
            assert found_box.value() == widget.value
            found_label = self.ui.findChild(QLabel, widget.key + '_label')
            assert found_label.text() == widget.string

    def test_two_singlet_grid_layout(self):
        """The user sees that the top of the window is a 2 x 5 grid of 
        numerical entries (bottom row) with corresponding labels (top row)"""

        assert 1 == 2  # TODO: Write more tests!
        # # print(self.ui.layout().itemAt(0).text)
        # va_box_fetch = self.ui.findChild(QDoubleSpinBox, 'va')
        # assert va_box_fetch.objectName() == 'va'
        # # assert self.ui.layout().itemAt(0) is not None

    def teardown(self):
        pass