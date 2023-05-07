from injector import inject
from utils import logger, Observer
from .log_viewer_model import LogViewerModel
from .log_viewer_view import LogViewerView

class LogViewerController(Observer):
    @inject
    def __init__(self,
                 model: LogViewerModel,
                 view: LogViewerView):
        self.model = model
        self.view = view
        logger.add_observer(self)

    def update(self, message):
        self.model.add_message(message)
        self.view.update_log(message)