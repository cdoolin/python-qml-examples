import QtQuick 2.5
import QtQuick.Window 2.2

import QtQuick.Controls 1.4

import Tests 1.0

Window {
    visible: true
    title: "Hello World"

    Test {
        id: test
        text: "yolo"
    }

    Button {
        id: button
        anchors.centerIn: parent
        text: test.text

        onClicked: {
            test.hello();
        }
    }
}
