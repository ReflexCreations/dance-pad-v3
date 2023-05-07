from PyQt5.QtWidgets import QWidget, QComboBox, QHBoxLayout
from utils import SButton

class PadInterfaceView(QWidget):
    def __init__ (self, parent=None):
        super().__init__(parent)

        self.connect_button = SButton('Connect')
        self.disconnect_button = SButton('Disconnect')
        self.refresh_button = SButton('Refresh')
        self.available_pad_list = QComboBox()

        layout = QHBoxLayout()
        layout.addWidget(self.connect_button)
        layout.addWidget(self.disconnect_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.available_pad_list)

        self.setLayout(layout)