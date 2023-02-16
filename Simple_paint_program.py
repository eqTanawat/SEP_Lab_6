import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_paint_program(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple paint program")
    
    def paintEvent(self, e):
        p = QPainter()

def main():
    app = QApplication(sys.argv)

    w = Simple_paint_program()
    w.show()
    
    return app.exec()

if __name__ == '__main__':
    

    sys.exit(main())