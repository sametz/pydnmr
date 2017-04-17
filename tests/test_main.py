import sys

from PyQt5.QtWidgets import (QApplication, QDoubleSpinBox, QLabel, QGridLayout,
                             QWidget, QToolBar, QStackedWidget, QVBoxLayout,
                             QRadioButton, QSpacerItem)
from PyQt5.QtCore import Qt

#import main
import ab as main

app = QApplication(sys.argv)


class TestDefaultGUi:

    def setup(self):
        self.ui = main.DnmrGui()

        self.activeView = self.ui.stackedWidget.currentWidget()
        # create lists of names for required widgets
        self.doublespinboxlist = [widget.key for widget in main.twosinglets_vars]
        labellist = [box + '_label' for box in self.doublespinboxlist]
        widgetlist = self.doublespinboxlist + labellist

        # Dictionaries match widget names to widget objects.
        # findChild can use tuples of object types, but my first pass at
        # using it failed (returned 4 copies of wb and 4 copies of k).
        # assembling piecewise:
        boxdict = {widget: self.ui.findChild(QDoubleSpinBox, widget)
                   for widget in self.doublespinboxlist}
        labeldict = {widget: self.ui.findChild(QLabel, widget)
                     for widget in labellist}
        self.widgetdict = {**boxdict, **labeldict}
        print('box list:', self.doublespinboxlist)
        print('box dict:', boxdict)
        print('label list:', labellist)
        print('label dict:', labeldict)
        print('widget list:', widgetlist)
        print('widget dict:', self.widgetdict)

    def test_title(self):
        """The user launches the app and sees that it is named 'pyDNMR'"""
        appTitle = self.ui.windowTitle()
        assert appTitle == 'pyDNMR'

    def test_find_active_view(self):
        """The user sees that the default main window is designed for the 
        simulation of two singlets."""
        assert self.activeView.objectName() == 'twosingletswidget'

    def test_two_singlets_all_widgets_exist(self):
        """The user sees 5 labels and 5 'double spin box' numerical entries 
        corresponding to the 5 inputs needed for the two singlets simulation.
        """

        for required_widget in main.twosinglets_vars:
            widgetBox = self.activeView.findChild(QDoubleSpinBox,
                                                  required_widget.key)
            assert widgetBox.value() == required_widget.value
            widgetLabel = self.activeView.findChild(
                QLabel, required_widget.key + '_label')
            assert widgetLabel.text() == required_widget.string

    def test_two_singlets_grid_layout(self):
        """The user sees that the widgets are in a 2 x 5 grid of 
        numerical entries (bottom row) with corresponding labels (top row). 
        The labels have the correct text, and the numerical entries are 
        correct for the default system.
        """
        layout = self.ui.findChild(QGridLayout, 'twosingletslayout')
        widgetlist = main.twosinglets_vars
        for i, widget in enumerate(widgetlist):
            widgetLabel = layout.itemAtPosition(0, i).widget()
            widgetBox = layout.itemAtPosition(1, i).widget()
            assert widgetLabel.text() == widget.string
            assert widgetBox.value() == widget.value

    def test_graph_spans_bottom_of_frame(self):
        """The user sees a graph object below the entry widgets, filling the 
        bottom of the frame. Its data matches that of the default system.
        """
        # TODO: learn how to assert a widget is a certain class
        # TODO: split into multiple tests
        # Test doesnt' test for correct graph widget, just contents

        layout = self.ui.findChild(QGridLayout, 'twosingletslayout')
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
            except Exception:
                print("Unexpected widgets found in column 7")

    def test_status_bar_ready(self):
        """The user sees a 'Ready' status indicator at the bottom of the app 
        window.
        """
        statusbarText = self.ui.statusBar().currentMessage()
        assert statusbarText == 'Ready'

    def test_twiddle_buttons(self):
        """The user changed values in all of the numerical entries up and 
        down, and the program didn't crash.
        """

        for key in self.doublespinboxlist:
            widget = self.widgetdict[key]
            widget.setValue(widget.value() + 10)
            widget.setValue(widget.value() - 20)
            widget.setValue(widget.value() + 10)

        for widget in main.twosinglets_vars:
            if widget.value > 10:
                assert self.widgetdict[widget.key].value() == widget.value
            else:
                assert self.widgetdict[widget.key].value() == 10.01
                # k and wa/b widgets should not go below 0.01

    # tests below were used as part of debugging, but retained because they
    # may detect a drastic change to the GUI

    def test_find_stackedwidget(self):
        foundStackedWidget = self.ui.findChild(QStackedWidget, 'stackedwidget')
        print('Found stackedwidget with parent',
              foundStackedWidget.parent(),
              foundStackedWidget.parent().objectName())

    def test_find_two_singlets_widget(self):
        foundTwoSingletWidget = self.ui.findChild(QWidget, 'twosingletswidget')
        print(type(foundTwoSingletWidget))
        print('Found twosingletwidget with parent',
              foundTwoSingletWidget.parent(),
              foundTwoSingletWidget.parent().objectName())

    def test_find_two_singlets_layout(self):

        foundLayout = self.ui.findChild(QGridLayout, 'twosingletslayout')
        if foundLayout:
            print('Found layout named', foundLayout.objectName())
            print('Found layout has parent:', foundLayout.parent(),
                  foundLayout.parent().objectName())
        else:
            foundLayout = self.ui.centralWidget().layout()
            print('Did not find QGridLayout child named "twosingletlayout"')
            print('Found layout named', foundLayout.objectName())
            print('Found layout has parent:', foundLayout.parent(),
                  foundLayout.parent().objectName())

    def test_find_AB_widget(self):
        foundABWidget = self.ui.findChild(QWidget, 'abwidget')
        print(type(foundABWidget))
        print('Found ABwidget with parent',
              foundABWidget.parent(),
              foundABWidget.parent().objectName())

    def test_child_parent_map(self):
        foundVaBox = self.ui.findChild(QDoubleSpinBox, 'va')
        current_widget = foundVaBox
        end = False
        while not end:
            try:
                print('Widget ', current_widget.objectName(), ' has parent ',
                      current_widget.parent().objectName())
                current_widget = current_widget.parent()
            except Exception:
                print('The parent of', current_widget.objectName(),
                      'is of type', type(current_widget.parent()))
                print('No more parents.')
                end = True

    def teardown(self):
        pass


class TestViewSwitch:

    def setup(self):
        self.ui = main.DnmrGui()
        self.getToolbar = self.ui.findChild(QToolBar, 'lefttoolbar')

    def test_left_toolbar_exists(self):
        """The user sees that there is a bar to the left of the main window.
        """
        assert self.ui.toolBarArea(self.getToolbar) == Qt.LeftToolBarArea

    def test_left_toolbar_has_layout(self):
        """The user sees that the toolbar has a vertical layout."""
        assert self.getToolbar.findChild(QVBoxLayout, 'modelslayout')

    def test_find_model_selection(self):
        """The user sees a menu of radio buttons with a label saying 
        'Select Model:'
        """

        foundModelsWidget = self.getToolbar.findChild(QWidget, 'modelswidget')
        for child in foundModelsWidget.children():
            print(type(child))
            if isinstance(child, QLabel):
                print('QLabel', child.text())
                assert child.text() == 'Select Model:'
            elif isinstance(child, QRadioButton):
                print('QRadioButton', child.text())
            else:
                print('Also found widget of type: ', type(child))

    def test_toolbar_layout(self):
        """The user sees, centered vertically in the toolbar, a label 
        instructing them to select a model, followed by a radio button to 
        select the two singlet model followed by a radio button to select the 
        AB model.
        """
        layout = self.getToolbar.findChild(QVBoxLayout, 'modelslayout')
        assert layout.count() == 5
        assert (isinstance(layout.itemAt(0), QSpacerItem) and
                (isinstance(layout.itemAt(4), QSpacerItem)))
        assert layout.itemAt(1).widget().text() == 'Select Model:'
        assert layout.itemAt(2).widget().text() == \
               'Two uncoupled spin-1/2 nuclei'
        assert layout.itemAt(3).widget().text() == \
               'Two coupled spin-1/2 nuclei\n ("AB quartet)'

    def test_view_switch(self):
        """The user clicks on the radio button for the AB model, and sees that 
        the view has changed to that for the AB model.
        """
        initialView = self.ui.stackedWidget.currentWidget()
        abButton = self.getToolbar.findChild(QRadioButton, 'abbutton')
        abButton.click()
        finalView = self.ui.stackedWidget.currentWidget()
        assert initialView is not finalView
        assert finalView.objectName() == 'abwidget'

    # function below was used for debugging, and retained because it may detect
    # a drastic change in GUI structure
    def test_child_parent_map(self):
        foundModelsLayout = self.getToolbar.findChild(QVBoxLayout,
                                                      'modelslayout')
        current_widget = foundModelsLayout
        end = False
        while not end:
            try:
                print('Widget ', current_widget.objectName(), ' has parent ',
                      current_widget.parent().objectName())
                current_widget = current_widget.parent()
            except Exception:
                print('The parent of', current_widget.objectName(),
                      'is of type', type(current_widget.parent()))
                print('No more parents.')
                end = True


class TestABGUi:

    def setup(self):
        self.ui = main.DnmrGui()
        self.ui.stackedWidget.setCurrentIndex(1)  # set view to AB model

        self.boxlist = [widget.key for widget in main.ab_vars]
        labellist = [box + '_label' for box in self.boxlist]
        widgetlist = self.boxlist + labellist

        boxdict = {widget: self.ui.findChild(QDoubleSpinBox, widget)
                   for widget in self.boxlist}
        labeldict = {widget: self.ui.findChild(QLabel, widget)
                     for widget in labellist}
        self.widgetdict = {**boxdict, **labeldict}
        print('box list:', self.boxlist)
        print('box dict:', boxdict)
        print('label list:', labellist)
        print('label dict:', labeldict)
        print('widget list:', widgetlist)
        print('widget dict:', self.widgetdict)

    def test_starting_with_ab_view(self):
        assert self.ui.stackedWidget.currentWidget().objectName() == 'abwidget'

    def test_ab_all_widgets_exist(self):
        """The user sees 5 labels and 5 'double spin box' numerical entries 
        corresponding to the 5 inputs needed for the AB simulation.
        """

        for widget in main.twosinglets_vars:
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
        layout = self.ui.findChild(QGridLayout, 'ablayout')
        widgetlist = main.ab_vars
        for i, widget in enumerate(widgetlist):
            widgetLabel = layout.itemAtPosition(0, i).widget()
            widgetBox = layout.itemAtPosition(1, i).widget()
            assert widgetLabel.text() == widget.string
            assert widgetBox.value() == widget.value

    def test_graph_spans_bottom_of_frame(self):
        """The user sees a graph object below the entry widgets, filling the 
        bottom of the frame. Its data matches that of the default system.
        """
        # TODO: learn how to assert a widget is a certain class
        # Test doesnt' test for correct graph widget, just contents

        layout = self.ui.findChild(QGridLayout, 'ablayout')
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
            except Exception:
                print("Unexpected widgets found in column 7")

    def test_status_bar_ready(self):
        """The user sees a 'Ready' status indicator at the bottom of the app 
        window.
        """
        statusbar_text = self.ui.statusBar().currentMessage()
        assert statusbar_text == 'Ready'

    def test_twiddle_buttons(self):
        """The user changed values in all of the numerical entries up and 
        down, and the program didn't crash.
        """

        for key in self.boxlist:
            widget = self.widgetdict[key]

            # success of test depends on WINDNMR's default values used,
            # i.e. test that j_ab, k_ab and wa + 20 - 40 don't go below 0
            widget.setValue(widget.value() + 20)
            widget.setValue(widget.value() - 40)
            widget.setValue(widget.value() + 20)

        for widget in main.ab_vars:
            print(widget.value, 'vs. ', self.widgetdict[widget.key].value())
            if widget.key == 'k_ab' or widget.key == 'wa':
                assert self.widgetdict[widget.key].value() == 20.01
                # k and wa widgets should not go below 0.01
            elif widget.key == 'j_ab':
                assert self.widgetdict[widget.key].value() == 20.00
                # j_ab should not go below 0
            else:
                assert self.widgetdict[widget.key].value() == widget.value

    def teardown(self):
        pass