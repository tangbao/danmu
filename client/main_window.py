# -*- coding:utf-8 -*-

import sys
import types

from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui

import screen_test_window
import screen_window


class systemTray(QtGui.QSystemTrayIcon):
    def __init__(self, parent, *args):
        QtGui.QSystemTrayIcon.__init__(self, parent, *args)

        self.setIcon(QtGui.QIcon('icon.ico'))

        self.activated.connect(self.on_activated)

        self.show()

    @QtCore.pyqtSlot(QtGui.QSystemTrayIcon.ActivationReason)
    def on_activated(self, e):
        if e == QtGui.QSystemTrayIcon.DoubleClick:
            if not isinstance(self.parent(), types.NoneType):
                if self.parent().isVisible():
                    self.parent().hide()
                else:
                    self.parent().show()
                    self.parent().activateWindow()


class MainWindow(QtGui.QWidget):
    def __init__(self):
        self.screen_window_list = list()

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
        self.hideButton.clicked.connect(self.hideButtonClicked)
        h_boxlayout.addWidget(self.hideButton)
        self.configButton = QtGui.QPushButton('&Config')
        h_boxlayout.addWidget(self.configButton)
        self.aboutButton = QtGui.QPushButton('&About')
        self.aboutButton.clicked.connect(self.aboutButtonClicked)
        h_boxlayout.addWidget(self.aboutButton)
        layout.addLayout(h_boxlayout)

        h_boxlayout = QtGui.QHBoxLayout()
        self.startButton = QtGui.QPushButton('&Start')
        h_boxlayout.addWidget(self.startButton)
        layout.addLayout(h_boxlayout)

        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint
                            | Qt.Qt.WindowMinimizeButtonHint)

        self.setLayout(layout)
        self.setFixedSize(600, 225)
        self.setWindowTitle('Main Window')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.initScreenTestWindow()

        self.initScreenWindow([0, ])

        self.show()

    def initScreenTestWindow(self):
        screen_count = QtGui.QDesktopWidget().screenCount()
        for screen_id in range(screen_count):
            # print screen_id
            screen_test_window.ScreenTestWindow(self, screen_id)

    def initScreenWindow(self, screen_list):
        for screen_id in screen_list:
            self.screen_window_list.append(screen_window.ScreenWindow(self, screen_id))

    @QtCore.pyqtSlot()
    def hideButtonClicked(self):
        self.hide()

    @QtCore.pyqtSlot()
    def aboutButtonClicked(self):
        QtGui.QMessageBox().about(self, 'About',
                                  u'''
                                  <strong>看什么看</strong>
                                  <p>就是个填坑中的弹幕小程序</p>
                                  <p>有什么好看的</p>
                                  <a href="https://github.com/Frederick-Zhu/danmu">https://github.com/Frederick-Zhu/danmu</a>
                                  ''')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main_window = MainWindow()

    sys.exit(app.exec_())
