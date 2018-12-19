import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui',self)
        
        [i.clicked.connect(self.run) for i in self.buttonGroup_numbers.buttons()]
        [i.clicked.connect(self.calc) for i in self.buttonGroup_binary.buttons()]
        self.pushButton_comma.clicked.connect(self.run)
        self.pushButton_equally.clicked.connect(self.result)
        self.pushButton_AC.clicked.connect(self.clear)
        self.pushButton_square.clicked.connect(self.square)
        self.pushButton_cube.clicked.connect(self.cube)
        self.pushButton_factorial.clicked.connect(self.fact)
        self.pushButton_sin.clicked.connect(self.sin)
        self.pushButton_cos.clicked.connect(self.cos)
        self.pushButton_tan.clicked.connect(self.tan)
        self.pushButton_sinh.clicked.connect(self.sinh)
        self.pushButton_cosh.clicked.connect(self.cosh)
        self.pushButton_tanh.clicked.connect(self.tanh)
        self.pushButton_log.clicked.connect(self.log)
        self.pushButton_inverse_fraction.clicked.connect(self.inverse_fraction)
        self.pushButton_pi.clicked.connect(self.pi)
        self.pushButton_ten_in_X.clicked.connect(self.ten_in_X)
        self.pushButton_plus_minus.clicked.connect(self.plus_minus)
        self.data = ''
        self.data_eval = ''
        
        
    ##реализация кнопки AC на калькуляторе(стирает все введенные ранее данные)
    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.table.display('') 
    
    def run(self):
        if self.sender().text()=='.':
            if '.' in self.data:
                return
        if self.data!='0' or (self.data=='0' and self.sender().text()=='.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.table.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.display(self.data)
            
    
            
    def calc(self):
        if self.data_eval:
            self.result()
            if (self.data_eval[-1] not in ['+','-',':','x', 'x^y']):
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0:len(self.data_eval)-1] + self.sender().text()
            self.data_eval = self.data_eval.replace('x^y',
                                                    '**').replace(':','/').replace('x', '*')
            
    ##факториал числа   
    def real_fact(self,n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.real_fact(n - 1)    
            
    def fact(self):
        if self.data_eval:
            self.data_eval = "self.real_fact({})".format(self.data_eval)
            print(self.data_eval)
            self.result()  
            
    ##синус числа
    def sin(self):
        if self.data_eval:
            self.data_eval = "math.sin(math.radians({}))".format(self.data_eval)
            self.result() 
        
    ##косинус числа
    def cos(self):
        if self.data_eval:
            self.data_eval = "math.cos(math.radians({}))".format(self.data_eval)
            self.result() 
        
    ##тангенс числа
    def tan(self):
        if self.data_eval:
            self.data_eval = "math.tan(math.radians({}))".format(self.data_eval)
            self.result()
        
    ##гиперболический синус    
    def sinh(self):
        if self.data_eval:
            self.data_eval = "math.sinh(math.radians({}))".format(self.data_eval)
            self.result()        
        
    ##гиперболический косинус
    def cosh(self):
        if self.data_eval:
            self.data_eval = "math.cosh(math.radians({}))".format(self.data_eval)
            self.result()  
            
    ##гиперболический тангенс
    def tanh(self):
        if self.data_eval:
            self.data_eval = "math.tanh(math.radians({}))".format(self.data_eval)
            self.result() 
            
    ##десятичный логарифм
    def log(self):
        if self.data_eval:
            self.data_eval = "math.log10({})".format(self.data_eval)
            self.result()
    
    ##1/x
    def inverse_fraction(self):
        if self.data_eval:
            self.data_eval = "1/{}".format(self.data_eval)
            self.result()
            
    ##число пи
    def pi(self):
        self.data_eval = "math.pi"
        self.result() 
        
    ##10^x
    def ten_in_X(self):
        if self.data_eval:
            self.data_eval = "10**{}".format(self.data_eval)
            self.result()
           
            
    ##возведение числа в квадрат        
    def square(self):
        if self.data_eval:
            self.data_eval += '**2'
            self.result() 
    
    ##возведение числа в куб
    def cube(self):
        if self.data_eval:
            self.data_eval += '**3'
            self.result()
            
    ##процент    
    def percent(self):
        if self.data_eval:
            self.data_eval += '/100'
            self.result()
    
    ##+-
    def plus_minus(self):
        if self.data_eval:
            self.data_eval += '-{}'.format(self.data_eval) 
            self.result()
        
            
    def result(self):
        try:
            float(self.data_eval)
        except:
            try:
                self.data = eval(self.data_eval)
                self.data_eval = str(self.data)
                self.table.display(self.data)
            except ZeroDivisionError:
                self.table.display('Error')
            except:
                pass
        self.data = ''
    
        
app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())