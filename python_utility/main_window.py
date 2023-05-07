from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget
from log_viewer import LogViewerView
from pad_interface import PadInterfaceView

from injector import inject

class MainWindow(QMainWindow):
    @inject
    def __init__(self,
                 pad_interface_view: PadInterfaceView,
                 log_viewer_view: LogViewerView):
        super(MainWindow, self).__init__()
        self.setWindowTitle("RE:Flex Python Utility")
        self.setMinimumSize(800, 600)

        layout = QGridLayout()
        layout.addWidget(pad_interface_view, 0, 0)
        layout.addWidget(log_viewer_view, 1, 0)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)