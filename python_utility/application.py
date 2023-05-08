from PyQt5.QtWidgets import QApplication
from .app_module import setup_injector
from .main_window import MainWindow
from .mediator import Mediator

class Application(QApplication):
    def __init__(self):
        super().__init__([])
        injector = setup_injector()
        self.main_window = injector.get(MainWindow)
        self.mediator = injector.get(Mediator)

    def run(self):
        self.main_window.show()
        self.exec()