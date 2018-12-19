import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
#from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt, QTimer
 
class myApp(QWidget):
 
    def __init__(self):
 
        QWidget.__init__(self)
 
        self.init_ui()
 
    def init_ui(self):
        self.speed = 10
        self.timer = QTimer(self)
        btn_left = QPushButton("влево", self)
        btn_right = QPushButton("вправо", self)
        btn_stop = QPushButton("stop", self)
        btn_left.move(10, 10)
        btn_right.move(350, 10)
        btn_stop.move(180, 10)
        self.x = 200
        self.y = 150
        self.setWindowTitle("бегущая строка")
        self.label = QLabel("бегущая строка", self)
        self.label.move(self.x, self.y)
        self.setGeometry(300, 300, 450, 300)
 
 
        btn_right.clicked.connect(self.buttonClicked)
        btn_left.clicked.connect(self.buttonClicked)
        btn_stop.clicked.connect(self.buttonClicked)
 
 
 
 
        self.show()
 
 
    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == "вправо":
            if self.timer.isActive():
                self.timer.stop()
                self.timer.timeout.disconnect()
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_right)
            else:
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_right)
 
 
 
 
        elif sender.text() == "влево":
            if self.timer.isActive():
                self.timer.stop()
                self.timer.timeout.disconnect()
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_left)
            else:
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_left)
        elif sender.text() == "stop":
            self.stop_move()
 
    def move_label_left(self):
        if self.x == -100:
            self.x = 500
            self.x = self.x - 0.5
            self.label.move(self.x, self.y)
 
        else:
            self.x = self.x - 0.5
            self.label.move(self.x, self.y)
 
 
 
 
    def move_label_right(self):
 
        if self.x == 500:
            self.x = -100
            self.x = self.x + 0.5
            self.label.move(self.x, self.y)
 
        else:
            self.x = self.x + 0.5
            self.label.move(self.x, self.y)
 
    def stop_move(self):
        if self.timer.isActive():
            self.timer.stop()
            self.timer.timeout.disconnect()
 
 
 
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = myApp()
    sys.exit(app.exec_())