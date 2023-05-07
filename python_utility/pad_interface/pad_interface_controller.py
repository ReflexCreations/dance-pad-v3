from injector import inject
from .pad_interface_model import PadInterfaceModel
from .pad_interface_view import PadInterfaceView
from utils import Observer, logger

class PadInterfaceController():
    @inject
    def __init__(self,
                 model: PadInterfaceModel,
                 view: PadInterfaceView):
        view.refresh_button.add_observer(PadEnumerateObserver(model))
        view.connect_button.add_observer(LogMessageObserver(model))

class PadEnumerateObserver(Observer):
    def __init__(self, model):
        self.model = model

    def update(self, event):
        self.model.enumerate()

class LogMessageObserver(Observer):
    def __init__(self, model):
        self.model = model

    def update(self, event):
        logger.add_message("Stuff happened!")