from PySide import QtCore, QtGui
import sys
import math


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(X, Y)
        self.__num = 0

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
    
        self.Serpinskiy(self.__num, 0, L, X / 2 - L / 2, Y / 2 + 1/(2 * math.sqrt(3)) * L, X / 2, Y / 2 - 1 / math.sqrt(3), (X + L) / 2, Y / 2 + 1/(2 * math.sqrt(3)) * L, painter)
        painter.end()
        
    def Koch(self, N, x1, y1, x2, y2, painter):
        if N == 0:
            painter.drawLine(x1, y1, x2, y2)
        else:
            A_x, A_y, B_x, B_y = x1, y1, x2, y2
            x1, x2 = x1 + (x2 - x1) / 3, x1 + 2 * (x2 - x1) / 3
            y1, y2 = y1 + (y2 - y1) / 3, y1 + 2 * (y2 - y1) / 3
            x_ = (x2 - x1) * math.cos(math.pi / 3) + (y2 - y1) * math.sin(math.pi / 3) + x1
            y_ = -(x2 - x1) * math.sin(math.pi / 3) + (y2 - y1) * math.cos(math.pi / 3) + y1
            x__ = (x1 - x2) * math.cos(math.pi * -1 / 3) + (y1 - y2) * math.sin(math.pi * -1 / 3) + x2
            y__ = -(x1 - x2) * math.sin(math.pi * -1 / 3) + (y1 - y2) * math.cos(math.pi * -1 / 3) + y2  
            self.Koch(N - 1, A_x, A_y, A_x + (B_x - A_x) / 3, A_y + (B_y - A_y) / 3, painter)
            self.Koch(N - 1, A_x + 2 * (B_x - A_x) / 3, A_y + 2 * (B_y - A_y) / 3, B_x, B_y, painter)
            self.Koch(N - 1, x1, y1, x_, y_, painter)
            self.Koch(N - 1, x__, y__, x2, y2, painter)
            
    def Serpinskiy(self, a, n, x1, y1, x2, y2, x3, y3, painter):
        if n == 0:
            #x1, y1, x2, y2, x3, y3 = X / 2 - L / 2, Y / 2 + 1/(2 * math.sqrt(3)) * L, X / 2, Y / 2 - 1 / math.sqrt(3), (X + L) / 2, Y / 2 + 1/(2 * math.sqrt(3)) * L
            painter(x1, y1, x2, y2)
            painter(x1, y1, x3, y3)
            painter(x3, y3, x2, y2)
        else:
            Serpinskiy(x1, y1, ((x3 + x1) / 2 + x1) / 2, y1 / 2, (x3 + x1) / 2, y1)
    def setValue(self, val):
        self.__num = val 
        self.repaint()        
            
N = 3
X = 600
Y = 600
app = QtGui.QApplication(sys.argv)
Window = QtGui.QMainWindow()
Window.setWindowTitle("Painter demo")
Window.resize(X, Y)
Widget = MyWidget(Window)
SpinBox = QtGui.QSpinBox(Window)
SpinBox.setGeometry(10, 10, 100, 30)
QtCore.QObject.connect(SpinBox, QtCore.SIGNAL("valueChanged(int)"),
                       Widget.setValue)
Window.show()
app.exec_()