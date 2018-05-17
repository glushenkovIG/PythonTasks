from PySide import QtCore, QtGui
import sys
import random
app = QtGui.QApplication(sys.argv)


def Ans():
        ans = random.randint(1023, 9877)
        if len(set(str(ans))) != 4:
                return Ans()
        return ans


class CowsBulls(QtCore.QObject):
        def __init__(self):
                QtCore.QObject.__init__(self)
                self.__data = 0 
                self.ans = Ans()
                self.__num = 0
                print(self.ans)
                      
        def setValue(self, value = 1):
                try:
                        self.__data = value
                except ValueError as S:
                        return
        
        def Check(self):
                if not (1023 <= int(self.__data) <= 9876 and len(set(str(self.__data))) == 4 and len(self.__data) == 4):
                        self.emit(QtCore.SIGNAL("setText(QString)"), "Wrong format.")     
                else:
                        self.__num += 1
                        self.__data = int(self.__data)
                        C = self.Cows(self.__data)
                        B = self.Bulls(self.__data)
                        if B == 4:
                                self.emit(QtCore.SIGNAL("setText(QString)"), "You win! My congratulations")
                        else:       
                                self.emit(QtCore.SIGNAL("setText(QString)"), str(C) + " Cows " + str(B) + " Bulls ")
            
        def Cows(self, val):
                Val = list(map(int, str(val)))
                Ans = list(map(int, str(self.ans)))
                Cow = 0         
                if Val[0] in Ans and Ans[0] != Val[0]:
                        Cow += 1
                if Val[1] in Ans and Ans[1] != Val[1]:
                        Cow += 1
                if Val[2] in Ans and Ans[2] != Val[2]:
                        Cow += 1
                if Val[3] in Ans and Ans[3] != Val[3]:
                        Cow += 1
                return Cow
    
        def Bulls(self, val):
                Val = list(map(int, str(val)))
                Ans = list(map(int, str(self.ans)))
                Bull = 0
                if Ans[0] == Val[0]:
                        Bull += 1
                if Ans[1] == Val[1]:
                        Bull += 1
                if Ans[2] == Val[2]:
                        Bull += 1
                if Ans[3] == Val[3]:
                        Bull += 1
                return Bull       
        

Window = QtGui.QMainWindow()
Window.setWindowTitle("Cows and Bulls")
Window.resize(500, 300)
CB = CowsBulls()
__data = 0
label = QtGui.QLabel(Window)
label.setText("Write digit")
label.setGeometry(130, 70, 400, 100)
LineEdit = QtGui.QLineEdit(Window)
LineEdit.setGeometry(110, 40, 100, 30)

End = QtGui.QPushButton("End", Window)
End.setGeometry(240, 70, 100, 30)

Button = QtGui.QPushButton("Check", Window)
Button.setGeometry(240, 40, 100, 30)        
QtCore.QObject.connect(End, QtCore.SIGNAL("clicked()"),
                       Window, QtCore.SLOT("close()"))

QtCore.QObject.connect(LineEdit, QtCore.SIGNAL("textChanged(QString)"),
                       CB.setValue)    

QtCore.QObject.connect(Button, QtCore.SIGNAL("clicked()"),
                       CB.Check)

QtCore.QObject.connect(CB, QtCore.SIGNAL("setText(QString)"),
                       label.setText)


Window.show()
app.exec_()