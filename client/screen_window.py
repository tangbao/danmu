# -*- coding:utf-8 -*-
from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui


class ScreenWindow(QtGui.QWidget):
    def __init__(self, parent, screen_id):
        QtGui.QWidget.__init__(self)

        self.setParent(parent)

        self.setWindowFlags(Qt.Qt.Window
                            | Qt.Qt.FramelessWindowHint
                            | Qt.Qt.WindowStaysOnTopHint)

        self.setAttribute(Qt.Qt.WA_DeleteOnClose, True)
        # ----WA_DeleteOnClose----
        # Makes Qt delete this widget when the widget has accepted
        # the close event (see QWidget::closeEvent()).

        self.setAttribute(Qt.Qt.WA_Disabled, True)
        # ----WA_Disabled----
        # Indicates that the widget is disabled, i.e. it does not receive
        # any mouse or keyboard events. There is also a getter functions
        # QWidget::isEnabled(). This is set/cleared by the Qt kernel.

        self.setAttribute(Qt.Qt.WA_TransparentForMouseEvents, True)
        # ----WA_TransparentForMouseEvents----
        # When enabled, this attribute disables the delivery of mouse
        # events to the widget and its children. Mouse events are
        # delivered to other widgets as if the widget and its children
        # were not present in the widget hierarchy; mouse clicks and
        # other events effectively "pass through" them. This attribute
        # is disabled by default.

        # self.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
        # ----WA_TranslucentBackground----
        # Indicates that the widget should have a translucent background,
        # i.e., any non-opaque regions of the widgets will be translucent
        # because the widget will have an alpha channel. Setting this flag
        # causes WA_NoSystemBackground to be set. On Windows the widget
        # also needs the Qt::FramelessWindowHint window flag to be set.
        # This flag is set or cleared by the widget's author.

        screen = QtGui.QDesktopWidget().screenGeometry(screen_id)

        self.resize(screen.width() / 4, screen.height() / 4)
        # self.move(screen.width() - self.width(), screen.y())

        animation = QtCore.QPropertyAnimation(self, 'pos')

        animation.setDuration(1000)
        animation.setStartValue(QtCore.QPoint(screen.width() - self.width(), screen.y()))
        animation.setEndValue(QtCore.QPoint(screen.width() / 2 - self.width(), screen.y()))

        self.show()
        print id(animation.targetObject())
        print id(self)
        animation.start()
