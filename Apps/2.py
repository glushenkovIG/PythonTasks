from PySide import QtCore, QtGui
import sys


class MyCounter(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.__data = 0

    def setValue(self, value = 1):
        try:
            value = int(value)
            if value < 0 or value > 50:
                return
            else:
                self.__data = value
        except ValueError as S:
            return
    
        self.emit(QtCore.SIGNAL("valueChanged(int)"), self.__data)
        self.emit(QtCore.SIGNAL("valueChanged(QString)"), str(self.__data))
        
    def Incr(self):
        self.__data += 1
        self.emit(QtCore.SIGNAL("valueChanged(int)"), self.__data)
        self.emit(QtCore.SIGNAL("valueChanged(QString)"), str(self.__data))
        
    def Decr(self):
        self.__data -= 1
        self.emit(QtCore.SIGNAL("valueChanged(int)"), self.__data)
        self.emit(QtCore.SIGNAL("valueChanged(QString)"), str(self.__data))
    
    def Clean(self):
        self.__data = 0
        self.emit(QtCore.SIGNAL("valueChanged(int)"), self.__data)
        self.emit(QtCore.SIGNAL("valueChanged(QString)"), str(self.__data))        

app = QtGui.QApplication(sys.argv)
Window = QtGui.QMainWindow()
Window.resize(500, 300)
SpinBox = QtGui.QSpinBox(Window)
SpinBox.setMaximum(50)
SpinBox.setWindowTitle("Spinbox")
SpinBox.setGeometry(10, 10, 100, 30)
Slider = QtGui.QSlider(QtCore.Qt.Horizontal, Window)
Slider.setMaximum(50)
Slider.setGeometry(10, 50, 100, 50)
LineEdit = QtGui.QLineEdit(Window)
LineEdit.setGeometry(10, 110, 100, 30)
Incr = QtGui.QPushButton("+1", Window)
Incr.setGeometry(120, 10, 50, 50)
Decr = QtGui.QPushButton("-1", Window)
Decr.setGeometry(180, 10, 50, 50)
Counter = MyCounter()
Clean = QtGui.QPushButton("Clean", Window)
Clean.setGeometry(140, 60, 70, 40)

QtCore.QObject.connect(Incr, QtCore.SIGNAL("clicked()"),
                       Counter.Incr)
QtCore.QObject.connect(Decr, QtCore.SIGNAL("clicked()"),
                       Counter.Decr)
QtCore.QObject.connect(Clean, QtCore.SIGNAL("clicked()"),
                       Counter.Clean)

QtCore.QObject.connect(Slider, QtCore.SIGNAL("valueChanged(int)"),
                       Counter.setValue)
QtCore.QObject.connect(SpinBox, QtCore.SIGNAL("valueChanged(int)"),
                       Counter.setValue)
QtCore.QObject.connect(LineEdit, QtCore.SIGNAL("textChanged(QString)"),
                       Counter.setValue)

QtCore.QObject.connect(Counter, QtCore.SIGNAL("valueChanged(int)"),
                       SpinBox.setValue)
QtCore.QObject.connect(Counter, QtCore.SIGNAL("valueChanged(int)"),
                       Slider.setValue)
QtCore.QObject.connect(Counter, QtCore.SIGNAL("valueChanged(QString)"),
                       LineEdit.setText)
Window.show()
app.exec_()