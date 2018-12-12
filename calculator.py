import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui',self)
        [i.clicked.connect(self.run) for i in self.buttonGroup_digits.buttons()]        
        self.pushButton_0.clicked.connect(self.input_num, 0)
        self.pushButton_1.clicked.connect(self.input_num, 1)
        self.pushButton_2.clicked.connect(self.input_num, 2)
        self.pushButton_3.clicked.connect(self.input_num, 3)
        self.pushButton_4.clicked.connect(self.input_num, 4)
        self.pushButton_5.clicked.connect(self.input_num, 5)
        self.pushButton_6.clicked.connect(self.input_num, 6)
        self.pushButton_7.clicked.connect(self.input_num, 7)
        self.pushButton_8.clicked.connect(self.input_num, 8)
        self.pushButton_9.clicked.connect(self.input_num, 9)
 
    def input_num(self, n):
        self.lcdNumber.display(n)
 
 
app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())