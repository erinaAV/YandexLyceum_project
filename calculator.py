import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import math
from random import random


'''«Многофункциональный калькулятор»

Возможности:

1. Калькулятор (базовые функции, тригонометрические функции, возведение в степень,
извлечение корней)

2. Построение графиков функций

3. Перевод из любой системы счисления в десятичную


Инструкция:

Калькулятор работает стандартно.

Графики. Введите в поле функцию от «х» (напр. «х + 5»), нажмите построить.
Приложение выведет график заданной вами функции.
«Спинбоксы» позволяют отрегулировать масштаб.

Для перевода в десятичную систему счисления необходимо ввести в верхнее поле число.
В следующем поле ввести основание системы счисления от 2 до 36.
После нажатие на кнопку «Выполнить» приложение выведет получившееся число.'''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Work.ui', self)
        # кнопки калькулятора
        [i.clicked.connect(self.run) for i in self.buttonGroup_numbers.buttons()]
        [i.clicked.connect(self.calc) for i in self.buttonGroup_binary.buttons()]
        self.pushButton_comma.clicked.connect(self.run)
        self.pushButton_equally.clicked.connect(self.result)
        self.pushButton_AC.clicked.connect(self.clear)
        self.pushButton_square.clicked.connect(self.square)
        self.pushButton_cube.clicked.connect(self.cube)
        self.pushButton_factorial.clicked.connect(self.fact)
        self.pushButton_percent.clicked.connect(self.percent)
        self.pushButton_pi.clicked.connect(self.pi)
        self.pushButton_random.clicked.connect(self.random_new)
        self.pushButton_sqr_root.clicked.connect(self.square_root)
        self.pushButton_cube_root.clicked.connect(self.cube_root)
        self.pushButton_sin.clicked.connect(self.sin) 
        self.pushButton_cos.clicked.connect(self.cos) 
        self.pushButton_tan.clicked.connect(self.tan)
        self.pushButton_sinh.clicked.connect(self.sinh) 
        self.pushButton_cosh.clicked.connect(self.cosh) 
        self.pushButton_tanh.clicked.connect(self.tanh)
        self.pushButton_inverse_fraction.clicked.connect(self.inverse_fraction)
        self.pushButton_log.clicked.connect(self.log)
        self.pushButton_10x.clicked.connect(self.ten_x)
        self.pushButton_e.clicked.connect(self.e)
        self.pushButton_x4.clicked.connect(self.x4)
        self.pushButton_root4.clicked.connect(self.root4)
        self.data = ''
        self.data_eval = ''
        
        # кнопка перевода в другую систему счисления
        self.btnResult.clicked.connect(self.getResult_systems)
        
        # кнопка построения графика
        self.pushButton_draw.clicked.connect(self.func)
        
    # реализация кнопки AC на калькуляторе(стирает все введенные ранее данные)
    def clear(self):
        self.data = '0'
        self.data_eval = '0'
        self.table.setText(str(self.data)) 
    
    def run(self):
        if self.sender().text() == '.':
            if '.' in self.data:
                return
        if self.data != '0' or (self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.table.setText(str(self.data))
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.setText(str(self.data))
            
    def calc(self):
        if self.data_eval:
            self.result()
            if (self.data_eval[-1] not in ['+', '-', ':', 'x', 'x^y', 'y√x']):
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0: len(self.data_eval) -
                                                1] + self.sender().text()
            self.data_eval = self.data_eval.replace('x^y',
                '**').replace(':', '/').replace('x', '*').replace('pi',
                'math.pi').replace('Random', 'random.random()')
            
    # факториал числа   
    def real_fact(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.real_fact(n - 1)    
            
    def fact(self):
        if self.data_eval:
            self.data_eval = "self.real_fact({})".format(self.data_eval)
            self.result()  
            
    # возведение числа в квадрат        
    def square(self):
        if self.data_eval:
            self.data_eval += '**2'
            self.result() 
    
    # возведение числа в куб
    def cube(self):
        if self.data_eval:
            self.data_eval += '**3'
            self.result()
            
    # квадратный корень из числа
    def square_root(self):
        if self.data_eval:
            self.data_eval += '**0.5'
            self.result()
    
    # кубический корень из числа      
    def cube_root(self):
        if self.data_eval:
            self.data_eval += '**(1/3)'
            self.result()
            
    # возведение числа в четвертую степень   
    def x4(self):
        if self.data_eval:
            self.data_eval += "**4"
            self.result() 
     
    # корень из числа четверной степени 
    def root4(self): 
        if self.data_eval: 
            self.data_eval += "{}**0.25".format(self.data_eval) 
            self.result()    
            
    # перевод числа в проценты
    def percent(self):
        if self.data_eval:
            self.data_eval = "{}/100".format(self.data_eval) 
            self.result()
            
    # ввод числа пи
    def pi(self):
        self.data_eval += 'math.pi'
        self.result()
        
    # ввод числа е 
    def e(self): 
        self.data_eval += "math.e" 
        self.result()    
        
    # ввод случайного числа от 0 до 1
    def random_new(self):
        self.data_eval += 'random()'
        self.result()
        
    # синус числа 
    def sin(self): 
        if self.data_eval: 
            self.data_eval = "math.sin(math.radians({}))".format(self.data_eval) 
            self.result() 
    
    # косинус числа 
    def cos(self): 
        if self.data_eval: 
            self.data_eval = "math.cos(math.radians({}))".format(self.data_eval) 
            self.result() 
    
    # тангенс числа 
    def tan(self): 
        if self.data_eval: 
            self.data_eval = "math.tan(math.radians({}))".format(self.data_eval) 
            self.result()
            
    # гиперболический синус 
    def sinh(self): 
        if self.data_eval: 
            self.data_eval = "math.sinh(math.radians({}))".format(self.data_eval) 
            self.result() 
    
    # гиперболический косинус 
    def cosh(self): 
        if self.data_eval: 
            self.data_eval = "math.cosh(math.radians({}))".format(self.data_eval) 
            self.result() 
        
    # гиперболический тангенс 
    def tanh(self): 
        if self.data_eval: 
            self.data_eval = "math.tanh(math.radians({}))".format(self.data_eval) 
            self.result()
            
    # 1/x 
    def inverse_fraction(self): 
        if self.data_eval: 
            self.data_eval = "1/{}".format(self.data_eval) 
            self.result()
            
    # десятичный логарифм 
    def log(self): 
        if self.data_eval: 
            self.data_eval = "math.log10({})".format(self.data_eval) 
            self.result()
            
    # возведение 10 в степень x
    def ten_x(self):
        if self.data_eval:
            self.data_eval = "10**{}".format(self.data_eval)
            self.result()
            
    def plus_minus(self):
        if self.data_eval:
            self.data_eval = '-{}'.format(self.data_eval)
            self.result
    
    # результат калькулятора  
    def result(self):
        try:
            float(self.data_eval)
        except:
            try:
                self.data = eval(self.data_eval)
                self.data_eval = str(self.data)
                self.table.setText(str(self.data))
            except ZeroDivisionError:
                self.table.display('Error')
            except:
                pass
        self.data = ''
        
    # результат перевода в другую систему счисления
    def getResult_systems(self):
        try:
            n1 = self.txtNum1.text()
            n2 = int(self.txtNum2.text())
            s = int(n1, n2)
            self.lblSum.setText(str(s))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()
            
    # построение графика
    def func(self):
        if self.lineEdit.text():
            self.widget.clear()
            data_x = [i for i in range(self.spinBox_a.value(), self.spinBox_b.value())]
            try:
                function = lambda x: eval(self.lineEdit.text())
                self.widget.plot(data_x, [function(i) for i in data_x], pen='r')
            except:
                pass
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())