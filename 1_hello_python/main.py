#
# hello_python.py
# basic example app for using python + pyqt5 to run a qml ui
# includes example of running python code from QML
#

# see http://pyqt.sourceforge.net/Docs/PyQt5/qml.html
# for guide on using QML with PyQt

import sys

from PyQt5.QtCore import qDebug, QUrl, QObject, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType


# To run python code, the easiest way is to create a Python class
# that subclasses a QObject and implements properties, signals, and slots
# which can be accessed from QML
class Test(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._text = ""

    # to implement a property we use pyqtProperty to define
    # python-like property with a getter and a setter.

    # For use in QML,  it is recommended to create a notify
    # signal so QML knows when UI elements need updateing
    textChanged = pyqtSignal()

    # define the property by decorating it's getter
    @pyqtProperty('QString', notify=textChanged)
    def text(self):
        return self._text

    # define a setter for a writable property.
    # the function name must be the same as the property
    @text.setter
    def text(self, text):
        # prevent infinite loops caused by emmitting the textChanged signal
        if self._text != text:
            qDebug("set text \"%s\"" % text)
            self._text = text
            self.textChanged.emit()

    # to make a function callable from QML, declare it as a slot
    @pyqtSlot()
    def hello(self):
        qDebug("hello from python")

# Finally register the type so it can be imported from QML
qmlRegisterType(Test, "Tests", 1, 0, "Test")


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl("main.qml"))

    app.exec()
