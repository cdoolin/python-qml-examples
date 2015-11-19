#
# hello_world.py
# basic example app for using python + pyqt5 to run a qml ui
#
# based of the c++ programs QtCreator creates when making a QtQuick
# application.

# see http://pyqt.sourceforge.net/Docs/PyQt5/qml.html
# for guide on using QML with PyQt

import sys

from PyQt5.QtCore import QUrl, QLibraryInfo
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine


app = QApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.load(QUrl("main.qml"))

app.exec()
