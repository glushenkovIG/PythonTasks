from PySide import QtCore, QtGui
import sys


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(200, 200)
        self.__num = 0

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        x = 0
        width = self.size().width() - 1
        height = self.size().height() - 1
        painter.begin(self)
        for i in range(self.__num):
            painter.drawRect(x, x, width, height)
            x += 2
            width -= 4
            height -= 4
        painter.end()

    def setValue(self, val):
        self.__num = val
        self.repaint()

app = QtGui.QApplication(sys.argv)
Window = QtGui.QMainWindow()
Window.setWindowTitle("Painter demo")
Window.resize(200, 250)
SpinBox = QtGui.QSpinBox(Window)
SpinBox.setGeometry(10, 10, 100, 30)
Widget = MyWidget(Window)
Widget.setGeometry(0, 50, 200, 200)
QtCore.QObject.connect(SpinBox, QtCore.SIGNAL("valueChanged(int)"),
                       Widget.setValue)
Window.show()
app.exec_()