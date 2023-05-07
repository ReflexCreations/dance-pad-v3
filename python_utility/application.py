import sys
import traceback
from PyQt5.QtWidgets import QApplication
from injector import Injector
from app_module import AppModule
from main_window import MainWindow

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        injector = Injector([AppModule()])
        self.main_window = injector.get(MainWindow)

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    try:
        application = Application()
        application.run()
    except Exception as e:
        traceback.print_exc()
        sys.exit()