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
        x1, y1, x2, y2 = (X - L) / 2, Y / 2, (X + L) / 2, Y / 2
        #self.Koch(self.__num, 0, Y / 2, X, Y / 2, painter)
        self.Minkovskiy(L, self.__num, x1, y1, x2, y2, painter)
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
            painter.drawline(x1, y1, x2, y2)
            painter.drawline(x1, y1, x3, y3)
            painter.drawline(x3, y3, x2, y2)
        else:
            self.Serpinskiy(a, n - 1, x1, y1, ((x3 + x1) / 2 + x1) / 2, y1 / 2, (x3 + x1) / 2, y1, painter)
            
    def Minkovskiy(self, l, n, x1, y1, x2, y2, painter):
        if n == 0:
            painter.drawLine(x1, y1, x2, y2)
        else:
            A_x, A_y = x1, y1
            B_x, B_y = (3 * x1 + x2) / 4, (3 * y1 + y2) / 4
            C_x, C_y = (x1 + x2) / 2, (y1 + y2) / 2
            D_x, D_y = (3 * x2 + x1) / 4, (3 * y2 + y1) / 4
            d_x = (x2 - x1) / 4
            d_y = (y2 - y1) / 4
            E_x, E_y = B_x + d_y, B_y - d_x
            F_x, F_y = C_x + d_y, C_y - d_x
            G_x, G_y = C_x - d_y, C_y + d_x
            H_x, H_y = D_x - d_y, D_y + d_x
            K_x, K_y = x2, y2
            self.Minkovskiy(l, n - 1, A_x, A_y, B_x, B_y, painter)
            self.Minkovskiy(l, n - 1, B_x, B_y, E_x, E_y, painter)
            self.Minkovskiy(l, n - 1, E_x, E_y, F_x, F_y, painter)
            self.Minkovskiy(l, n - 1, F_x, F_y, C_x, C_y, painter)
            self.Minkovskiy(l, n - 1, C_x, C_y, G_x, G_y, painter)
            self.Minkovskiy(l, n - 1, G_x, G_y, H_x, H_y, painter)
            self.Minkovskiy(l, n - 1, H_x, H_y, D_x, D_y, painter)
            self.Minkovskiy(l, n - 1, D_x, D_y, K_x, K_y, painter)
            
    def setValue(self, val):
        self.__num = val 
        self.repaint()
        
    def setFunc(self, val):
        self.func = val 
        self.repaint()      
N = 0
X = 600
Y = 600
L = 500
app = QtGui.QApplication(sys.argv)
Window = QtGui.QMainWindow()
Window.setWindowTitle("Painter demo")
Window.resize(X, Y)
Widget = MyWidget(Window)
SpinBox = QtGui.QSpinBox(Window)
SpinBox.setGeometry(10, 10, 100, 30)
button1 = QtGui.QRadioButton("Koch", Window)
button1.setGeometry(10, 30, 100, 100)
button2 = QtGui.QRadioButton("Serpinskiy", Window)
button2.setGeometry(10, 50, 100, 100)
button3 = QtGui.QRadioButton("Minkovskiy", Window)
button3.setGeometry(10, 70, 100, 100)
QtCore.QObject.connect(SpinBox, QtCore.SIGNAL("valueChanged(int)"),
                       Widget.setValue)
QtCore.QObject.connect(button1, QtCore.SIGNAL("checked"),
                       Widget.setFunc)
Window.show()
app.exec_()