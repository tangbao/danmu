# -*- coding:utf-8 -*-
from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui

from client import screen_test_window


class ConfigWindow(QtGui.QWidget):
    def __init__(self, *args):
        self.screen_test_window_list = list()
        self.checkbox_list = list()

        QtGui.QWidget.__init__(self, *args)

        self.initScreenTestWindow()

        self.setWindowFlags(QtCore.Qt.Window
                            | QtCore.Qt.WindowMinimizeButtonHint)

        layout = QtGui.QVBoxLayout(self)

        # self.screen_test_window_list = range(10)

        for screen in self.screen_test_window_list:
            self.checkbox_list.append(
                QtGui.QCheckBox('screen{0}'.format(self.screen_test_window_list.index(screen)), self))

        scrollArea = QtGui.QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scrollAreaWidgetContents = QtGui.QWidget()
        v_boxlayout = QtGui.QVBoxLayout()

        # 加入v_boxlayout 并 绑定信号
        for checkbox in self.checkbox_list:
            v_boxlayout.addWidget(checkbox)
            checkbox.stateChanged.connect(self.checkBoxChanged)

        scrollAreaWidgetContents.setLayout(v_boxlayout)
        scrollArea.setWidget(scrollAreaWidgetContents)
        layout.addWidget(scrollArea)

        self.okButton = QtGui.QPushButton('OK')
        self.okButton.clicked.connect(self.close)
        layout.addWidget(self.okButton)

        self.setFixedSize(450, 500)
        self.setWindowTitle('Config')

        self.show()

    def initScreenTestWindow(self):
        screen_count = QtGui.QDesktopWidget().screenCount()
        for screen_id in range(screen_count):
            self.screen_test_window_list.append(screen_test_window.ScreenTestWindow(self, screen_id))

    def closeEvent(self, QCloseEvent):
        for screen in self.screen_test_window_list:
            screen.close()
        self.close()

    @QtCore.pyqtSlot(int)
    def checkBoxChanged(self, state):
        if state == Qt.Qt.Unchecked:
            self.screen_test_window_list[self.checkbox_list.index(self.sender())].deselected()
        else:
            self.screen_test_window_list[self.checkbox_list.index(self.sender())].selected()
