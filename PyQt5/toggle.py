from PyQt5.QtWidgets import (QWidget, QPushButton,
                            QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)
        redb = QPushButton('Red', self)
        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)
