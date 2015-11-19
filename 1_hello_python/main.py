#
# hello_world.py
# basic example app for using python + pyqt5 to run a qml ui
#
# based of the c++ programs QtCreator creates when making a QtQuick
# application.

# see http://pyqt.sourceforge.net/Docs/PyQt5/qml.html
# for guide on using QML with PyQt

import sys

from PyQt5.QtCore import QUrl, QLibraryInfo, pyqtSlot, QObject
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType


class Funcs(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def hello():
        print("hello from python")


qmlRegisterType(Funcs, "PyFuncs", 1, 0, "Funcs")

app = QApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.load(QUrl("main.qml"))


app.exec()
