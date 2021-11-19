import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Random ellipse')
        self.do_paint = False
        self.btn.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(1, 250)
        qp.drawEllipse(30, 30, x, x)

    def draw(self):
        self.do_paint = True
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
