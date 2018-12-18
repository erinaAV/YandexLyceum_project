import sys
# Импортируем наш интерфейс
from QWERTY import *
# from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     
        
        # Начало моего дописанного кода:
        self.ui.btnResult.clicked.connect(self.getResult)
        
    # функция которая выполняется при нажатии на кнопку 
    def getResult(self):
        try:
            n1 = self.ui.txtNum1.text()
            n2 = int(self.ui.txtNum2.text())
            s = int(n1, n2)
            self.ui.lblSum.setText(str(s))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()     

        # Конец моего кода


app = QtWidgets.QApplication(sys.argv)
myapp = MyWin()
myapp.show()
sys.exit(app.exec_())