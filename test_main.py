import sys
import pytest
from PyQt5.QtWidgets import QApplication, QDoubleSpinBox, QLabel, \
    QGridLayout, QWidget
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

# Uncomment to test on mock:
import mock as main

# Uncomment to test on real code:
# import main
app = QApplication(sys.argv)

class TestMainGUi:

    def setup(self):
        self.ui = main.dnmrGui()

    def test_title(self):
        """The user launches the app and sees that it is named 'pyDNMR'"""
        app_title = self.ui.windowTitle()
        assert app_title == 'pyDNMR'

    def test_two_singlet_all_widgets_exist(self):
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
        va_box_fetch = self.ui.findChild(QDoubleSpinBox, 'va')
        print(va_box_fetch.parent().parent().objectName())
        found_widget = self.ui.centralWidget().layout().itemAtPosition(0, 0)
        print(found_widget.widget().text())
        assert found_widget.widget().text() == 'Va'
        #assert found_widget.objectName == 'va'
        #assert va_box_fetch.objectName() == 'va'

        #assert 1 == 2  # TODO: Write more tests!
        # # print(self.ui.layout().itemAt(0).text)
        # va_box_fetch = self.ui.findChild(QDoubleSpinBox, 'va')
        # assert va_box_fetch.objectName() == 'va'
        # # assert self.ui.layout().itemAt(0) is not None

    def test_alternate_widget_access(self):
        """Just hacking away trying to find a more terse widget reference"""
        main_layout = self.ui.findChild(QGridLayout, 'centrallayout')
        found_widget = main_layout.itemAtPosition(0, 0)
        print('Widget at coordinate 0, 0 is', type(found_widget))
        print('This widget contains widget ', type(found_widget.widget()))
        print('Its text is', found_widget.widget().text())
        assert found_widget.widget().text() == 'Va'
        found_widget2 = main_layout.itemAtPosition(0,0).widget()
        print(type(found_widget2), found_widget2.objectName(),
              found_widget2.text())

    def test_find_central_widget(self):
        found_centralwidget = self.ui.findChild(QWidget, 'centralwidget')
        print('Found centralwidget with parent', found_centralwidget.parent(),
              found_centralwidget.parent().objectName())

    def test_find_central_layout(self):

        found_layout = self.ui.findChild(QGridLayout, 'centrallayout')
        if found_layout:
            print('Found layout named', found_layout.objectName())
            print('Found layout has parent:', found_layout.parent(),
                  found_layout.parent().objectName())
        else:
            found_layout = self.ui.centralWidget().layout()
            print('Did not find QGridLayout child named "centrallayout"')
            print('Found layout named', found_layout.objectName())
            print('Found layout has parent:', found_layout.parent(),
                  found_layout.parent().objectName())

    def test_child_parent_map(self):
        va_widget_fetch = self.ui.findChild(QDoubleSpinBox, 'va')
        current_widget = va_widget_fetch
        end = False
        while not end:
            try:
                print('Widget ', current_widget.objectName(), ' has parent ',
                      current_widget.parent().objectName())
                current_widget = current_widget.parent()
            except:
                print('The parent of', current_widget.objectName(),
                      'is of type', type(current_widget.parent()))
                print('No more parents.')
                end = True

    def teardown(self):
        pass