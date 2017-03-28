import sys
import pytest
from PyQt5.QtWidgets import QApplication, QDoubleSpinBox, QLabel, \
    QGridLayout, QWidget
from pyqtgraph import PlotWidget
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

# Uncomment to test on mock:
# import mock as main
from pydnmr.testdata import TWOSPIN_SLOW

# Uncomment to test on real code:
import main
app = QApplication(sys.argv)

class TestMainGUi:

    def setup(self):
        self.ui = main.dnmrGui()

        boxlist = [widget.key for widget in main.twospin_vars]
        labellist = [box + '_label' for box in boxlist]
        widgetlist = boxlist + labellist

        # findChild can use tuples of object types, but my first pass at
        # using it failed (returned 4 copies of wb and 4 copies of k).
        # assembling piecewise:
        boxdict = {widget: self.ui.findChild(QDoubleSpinBox, widget)
                      for widget in boxlist}
        labeldict = {widget: self.ui.findChild(QLabel, widget)
                   for widget in labellist}
        self.widgetdict = {**boxdict, **labeldict}
        print('box list:', boxlist)
        print('box dict:', boxdict)
        print('label list:', labellist)
        print('label dict:', labeldict)
        print('widget list:', widgetlist)
        print('widget dict:', self.widgetdict)
    # def test_childAt(self):
    #     fetch = self.ui.centralWidget().
    #     fetchlist = self.ui.children()
    #     print(fetchlist)
    #     print("Fetched", fetch, 'object with name', fetch.objectName())
    #     assert fetch.objectName() == 'va_label'
    #     assert fetch.text() == 'Va'

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
        """The user sees that the widgets are in a 2 x 5 grid of 
        numerical entries (bottom row) with corresponding labels (top row). 
        The labels have the correct text, and the numerical entries are 
        correct for the default system.
        """
        layout = self.ui.findChild(QGridLayout, 'centrallayout')
        widgetlist = main.twospin_vars
        for i, widget in enumerate(widgetlist):
            label_fetch = layout.itemAtPosition(0, i).widget()
            box_fetch = layout.itemAtPosition(1, i).widget()
            assert label_fetch.text() == widget.string
            assert box_fetch.value() == widget.value

    def test_graph_spans_bottom_of_frame(self):
        """The user sees a graph object below the entry widgets, filling the 
        bottom of the frame. Its data matches that of the default system.
        """
        # TODO: learn how to assert a widget is a certain class
        # Test doesnt' test for correct graph widget, just contents

        layout = self.ui.findChild(QGridLayout, 'centrallayout')
        widget_2_0 = layout.itemAtPosition(2, 0).widget()
        data = widget_2_0.listDataItems()

        # Can't figure out how to find out what the graph data is, to compare
        #  to an accepted set. For now, let's try to assure that the data
        # returned from all 6 cells of bottom row are the same.
        # TODO: learn how to retrieve data from pyqtgraph plot
        for i in range(1, 6):
            # using 'is' instead of '==' in next line didn't quite work
            assert data == layout.itemAtPosition(2, i).widget().listDataItems()

        # test that 7th column is empty
        for j in range(3):
            try:
                found_widget = layout.itemAtPosition(j, 5).widget()
                assert not found_widget
            except:
                print(found_widget)

    def test_twiddle_buttons(self):
        """The user changed values in all of the numerical entries up and 
        down, and the program didn't crash."""
        assert self.widgetdict['va'].objectName() == 'va'
        assert self.widgetdict['va_label'].text() == 'Va'


        assert 1 == 2  # TODO: Finish test!

    # tests below were used as part of debugging, but retained because they
    # may detect a drastic change to the GUI

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