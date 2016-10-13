# -*- coding:utf-8 -*-

import sys

from PyQt4 import QtGui

import screen_test_window


class systemTray(QtGui.QSystemTrayIcon):
    def __init__(self, parent, *args):
        QtGui.QSystemTrayIcon.__init__(self, parent, *args)

        self.setIcon(QtGui.QIcon('icon.ico'))

        self.show()

class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.system_tray = systemTray(self)

        layout = QtGui.QVBoxLayout(self)

        h_boxlayout = QtGui.QHBoxLayout()
        h_boxlayout.addWidget(QtGui.QLabel('Server:'))
        self.serverLineEdit = QtGui.QLineEdit()
        self.serverLineEdit.setText('https://www.google.com')
        h_boxlayout.addWidget(self.serverLineEdit)
        layout.addLayout(h_boxlayout)

        h_boxlayout = QtGui.QHBoxLayout()
        h_boxlayout.addWidget(QtGui.QLabel('Password:'))
        self.passwordLineEdit = QtGui.QLineEdit()
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setText('123')
        h_boxlayout.addWidget(self.passwordLineEdit)
        layout.addLayout(h_boxlayout)

        h_boxlayout = QtGui.QHBoxLayout()
        self.hideButton = QtGui.QPushButton('&Hide')
        h_boxlayout.addWidget(self.hideButton)
        self.startButton = QtGui.QPushButton('&Start')
        h_boxlayout.addWidget(self.startButton)
        layout.addLayout(h_boxlayout)

        self.setLayout(layout)
        self.resize(600, 200)
        self.setWindowTitle('config')

        self.initScreenTestWindow()

        self.show()

    def initScreenTestWindow(self):
        screen_count = QtGui.QDesktopWidget().screenCount()
        for screen_id in range(screen_count):
            print screen_id
            screen_test_window.ScreenTestWindow(self, screen_id)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main_window = MainWindow()

    sys.exit(app.exec_())
