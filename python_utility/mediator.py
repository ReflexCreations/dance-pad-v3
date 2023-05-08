from PyQt5.QtCore import QObject
from injector import inject
from .pad_interface import PadInterfaceController
from .log_viewer import LogViewerController
from .utils import logger

class Mediator(QObject):
    @inject
    def __init__(self, pad_interface_controller: PadInterfaceController, log_viewer_controller: LogViewerController):
        super().__init__()
        self.PI = pad_interface_controller
        self.LV = log_viewer_controller
        self.setup_pad_interface_listeners()
        self.setup_logger_listeners()

    def setup_pad_interface_listeners(self):
        self.PI.refresh.connect(lambda: self.PI.enumerate())
        self.PI.connect.connect(lambda: self.PI.open())
        self.PI.disconnect.connect(lambda: self.PI.disconnect_clicked())

    def setup_logger_listeners(self):
        logger.new_message.connect(lambda message: self.LV.update(message))