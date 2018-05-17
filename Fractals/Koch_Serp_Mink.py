from PySide import QtCore, QtGui
import sys
import math


class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.__num = 0
        self.func = 0

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        X = self.size().width()
        Y = self.size().height() - 1
        if self.func == 1:
            x, y = X, Y
            b = min(x / 3 * 3 ** 0.5 / 2, y)
            a = b * 2 / 3 ** 0.5 * 3
            x1, y1 = (X - a) / 2, (Y + b) / 2
            x2, y2 = x1 + a, y1
            self.Koch(self.__num, x1, y1, x2, y2, painter)
        elif self.func == 2:
            b = min(X * 3 ** 0.5 / 2, Y)
            a = b * 2 / 3 ** 0.5
            x1, y1 = (X - a) / 2, (Y + b) / 2
            x3, y3 = x1 + a, y1
            x2, y2 = (x1 + x3) / 2, y1 - b
            self.Serpinskiy(self.__num, x1, y1, x2, y2, x3, y3, painter)
        elif self.func == 3:
            b = min(2 * X / 3, Y)
            a = b * 3 / 2
            x1, y1 = (X - a) / 2, Y / 2
            x2, y2 = x1 + a, y1            
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
            
    def Serpinskiy(self, n, x1, y1, x2, y2, x3, y3, painter):
        if n == 0:
            painter.drawLine(x1, y1, x3, y3)
            painter.drawLine(x1, y1, x2, y2)
            painter.drawLine(x2, y2, x3, y3)
        else:
            self.Serpinskiy(n - 1, x1, y1, ((x3 + x1) / 2 + x1) / 2, (y2 + y1) / 2, (x3 + x1) / 2, y1, painter)
            self.Serpinskiy(n - 1, (x1 + x2) / 2, (y2 + y1) / 2, x2, y2, (x3 + x2) / 2, (y2 + y1) / 2, painter)
            self.Serpinskiy(n - 1, (x3 + x1) / 2, y1, ((x3 + x1) / 2 + x3) / 2, (y2 + y1) / 2, x3, y3, painter)
            
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
        
    def setKoch(self):
        self.func = 1
        self.repaint()
        
    def setSerpinskiy(self):
        self.func = 2
        self.repaint()
        
    def setMinkovskiy(self):
        self.func = 3  
        self.repaint()
     
     
class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.resize(X, Y)
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Koch")
        self.Widget = MyWidget(self)
        
    def resizeEvent(self, event):
        self.Widget.setGeometry(0, 0, self.width(), self.height()) 
        
        
N = 0
X = 600
Y = 600
L = 300
app = QtGui.QApplication(sys.argv)
Window = MyWindow()
SpinBox = QtGui.QSpinBox(Window)
SpinBox.setGeometry(10, 10, 100, 30)
button1 = QtGui.QRadioButton('Koch', Window)
button1.setGeometry(10, 50, 100, 20)
button2 = QtGui.QRadioButton('Serpinskiy', Window)
button2.setGeometry(10, 70, 100, 20)
button3 = QtGui.QRadioButton('Minkovskiy', Window)
button3.setGeometry(10, 90, 100, 20)
QtCore.QObject.connect(SpinBox, QtCore.SIGNAL("valueChanged(int)"),
                       Window.Widget.setValue)
QtCore.QObject.connect(button1, QtCore.SIGNAL("clicked()"),
                       Window.Widget.setKoch)
QtCore.QObject.connect(button2, QtCore.SIGNAL("clicked()"),
                       Window.Widget.setSerpinskiy)
QtCore.QObject.connect(button3, QtCore.SIGNAL("clicked()"),
                       Window.Widget.setMinkovskiy)


Window.show()
app.exec_()