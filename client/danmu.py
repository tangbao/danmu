# -*- coding:utf-8 -*-
from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui


class Danmu(QtGui.QLabel):
    def __init__(self, text, style, parent, *args):
        QtGui.QLabel.__init__(self, text, parent, *args)

        font = QtGui.QFont()
        font.setPointSize(style.get('font_PointSize', 48))
        font.setFamily(style.get('font_Family', 'Microsoft Yahei'))
        self.setFont(font)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.WindowText,
                         style.get('palette_Color', Qt.Qt.black))
        self.setPalette(palette)

        self.setText(text)
        self.move(parent.width(), 0)

        self.show()

        animation = QtCore.QPropertyAnimation(self, 'pos', self)

        animation.setDuration(style.get('animation_Duration', 1000))
        animation.setStartValue(QtCore.QPoint(parent.width(), 0))
        animation.setEndValue(QtCore.QPoint(-self.width(), 0))

        animation.start()
