import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Drawing_area(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.position().x()
            self.last_y = e.position().y()
            return # Ignore the first time.

        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.drawLine(self.last_x, self.last_y, e.position().x(), e.position().y())
        painter.end()
        self.label.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = e.position().x()
        self.last_y = e.position().y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def clear(self):
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)

class main_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.Drawing_area = Drawing_area()

        layout = QVBoxLayout()
        layout.addWidget(self.Drawing_area)

        label = QLabel(self)
        label.setText("Drag the mouse to draw")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        clear_button = QPushButton('Clear', self)
        clear_button.clicked.connect(self.Drawing_area.clear)
        layout.addWidget(clear_button)

        self.setLayout(layout)
        self.setMinimumSize(400,400)

def main():
    app = QApplication(sys.argv)

    w=main_window()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
