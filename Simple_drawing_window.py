import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100), QPoint(100,110),
            QPoint(130,100),QPoint(100,150),
        ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180 * 16)

        p.drawPolygon(
            [QPoint(50,200), QPoint(150,200),QPoint(100,400),]
        )

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing - 1")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(255,255,0))
        p.drawPolygon([
            QPoint(350,350), QPoint(300,300),
            QPoint(250,350), QPoint(275,280),
            QPoint(225,250), QPoint(275,250),
            QPoint(300,200), QPoint(325,250),
            QPoint(375,250), QPoint(325,280),
        ])

        p.end()
  
class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing - 2")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(150,0,90))
        p.setBrush(QColor(150,0,90))
        p.drawPie(50,150,100,100,0,180*16)
        p.drawPie(150,150,100,100,0,180*16)
        p.drawPolygon([QPoint(50,200), QPoint(250,200), QPoint(150,325),])
        
        p.end()
        
class Simple_drawing_window_3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing - 3")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(69,69,69))
        p.drawPolygon([
            QPoint(90,200), QPoint(90,250),
            QPoint(180,200),QPoint(180,250),
        ])

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(200,39,23))
        p.drawPie(50,150,100,100,0,180 * 16)

        p.drawPolygon(
            [QPoint(50,200), QPoint(150,200),QPoint(150,400),QPoint(50,400),]
        )

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
        
def main():
    app = QApplication(sys.argv)

    w1 = Simple_drawing_window()
    w1.show()
    w2 = Simple_drawing_window()
    w2.show()
    w3 = Simple_drawing_window()
    w3.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
