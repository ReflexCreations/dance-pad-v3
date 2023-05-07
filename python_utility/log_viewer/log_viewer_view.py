from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class LogViewerView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)

    def update_log(self, message):
        self.text_edit.append(message)