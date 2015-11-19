#
# hello_world.py
# basic example app for using python + pyqt5 to run a qml ui
#
# based of the c++ programs QtCreator creates when making a QtQuick
# application.

# see http://pyqt.sourceforge.net/Docs/PyQt5/qml.html
# for guide on using QML with PyQt

import sys

from PyQt5.QtCore import QUrl
# need a QGuiApplication for QtQuick to work.  Could
# also use a QApplication from QtWidgets
from PyQt5.QtGui import QGuiApplication
# QQmlApplication makes it easier to load a QML file,  but the
# QML file needs to put things in a Window object
from PyQt5.QtQml import QQmlApplicationEngine


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.load(QUrl("main.qml"))

app.exec()
