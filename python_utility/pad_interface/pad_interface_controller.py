from injector import inject
from . import PadInterfaceModel, PadInterfaceView
from ..utils import logger, qt_slot

class PadInterfaceController():
    @inject
    def __init__(self, model: PadInterfaceModel, view: PadInterfaceView):
        self.model = model
        self.view = view
        self.connect = self.view.connect_button.clicked
        self.disconnect = self.view.disconnect_button.clicked
        self.refresh = self.view.refresh_button.clicked
    
    @qt_slot()
    def enumerate(self):
        print(self.model.enumerate())
    
    @qt_slot()
    def open(self):
        self.model.open()

    @qt_slot()
    def disconnect_clicked(self):
        logger.add_info("Disconnect clicked.")