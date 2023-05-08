from injector import inject
from . import LogViewerModel, LogViewerView
from ..utils import qt_slot

class LogViewerController():
    @inject
    def __init__(self, model: LogViewerModel, view: LogViewerView):
        self.model = model
        self.view = view

    @qt_slot()
    def update(self, message):
        self.model.add_message(message)
        self.view.update_log(message)