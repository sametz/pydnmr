import os, sys
from PyQt5.QtWidgets import (QStackedWidget, QMainWindow,
                             QHBoxLayout, QPushButton, QApplication, QLabel,
                             QWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = LoginWidget(self)
        login_widget.button.clicked.connect(self.login)
        self.central_widget.addWidget(login_widget)

        search_widget = searchWidget(self)
        search_widget.returnButton.clicked.connect(
            self.returning)  # The returnButton from searchWidget(self) connects to the function returning(self), but the returning function does not return to the home menu.
        self.central_widget.addWidget(search_widget)

    def login(self):
        layout = QHBoxLayout()
        self.button = QPushButton('Login')
        layout.addWidget(self.button)
        self.setLayout(layout)
        logged_in_widget = searchWidget(self)
        search_widget = searchWidget(self)
        self.central_widget.addWidget(logged_in_widget)  # This part is key
        self.central_widget.setCurrentWidget(logged_in_widget)

    def returning(self):
        # Here what im doing is restoring everything like it was before in the home menu, that's why I put the "Login" button again (in line 31).
        # This is not very optimized but i put it all again so that its more understandable. I can also, instead of all this code (from line 30 to 37), put a call to the login function like this: login(self) but I prefer the first way.
        layout = QHBoxLayout()
        self.button = QPushButton('Login')
        layout.addWidget(self.button)
        self.setLayout(layout)
        logged_in_widget = searchWidget(self)
        search_widget = searchWidget(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)
        # So, i got the buttons there they look fine, but the return button doesn't do anything, while the "login" button (that switchs to the searchWidget) does work.


class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.button = QPushButton('Login')
        self.label = QLabel('You are on the menu now')
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        # you might want to do self.button.click.connect(self.parent().login) here


class searchWidget(QWidget):
    def __init__(self, parent=None):
        super(searchWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.returnButton = QPushButton('Return')
        layout.addWidget(self.returnButton)
        self.label = QLabel('logged in in searchwidget!!!!')
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()