# -*- coding:utf-8 -*-
from PyQt4 import Qt
from PyQt4 import QtGui

from client import screen_test_window


class ConfigWindow(QtGui.QWidget):
    def __init__(self, *args):
        self.screen_test_window_list = list()

        QtGui.QWidget.__init__(self, *args)

        self.initScreenTestWindow()

        self.setWindowFlags(Qt.Qt.Window)

        self.resize(500, 200)

        self.show()

    def initScreenTestWindow(self):
        screen_count = QtGui.QDesktopWidget().screenCount()
        for screen_id in range(screen_count):
            self.screen_test_window_list.append(screen_test_window.ScreenTestWindow(self, screen_id))

    def closeEvent(self, QCloseEvent):
        for screen in self.screen_test_window_list:
            print screen.screen_id
            screen.close()
        self.close()
