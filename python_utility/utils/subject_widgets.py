from PyQt5.QtWidgets import QPushButton
from .observer import Subject

class SButton(Subject, QPushButton):
    def __init__(self, text):
        QPushButton.__init__(self)
        Subject.__init__(self)
        self.setText(text)

        self.clicked.connect(self.notify)