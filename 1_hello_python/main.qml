import QtQuick 2.5
import QtQuick.Window 2.2

import QtQuick.Controls 1.4

import PyFuncs 1.0

Window {
    visible: true
    title: "Hello World"

    Button {
        id: button
        anchors.centerIn: parent
        text: "Click Me"

        onClicked: {
            console.log("hello from qml");
            Funcs.hello();
        }
    }
}
