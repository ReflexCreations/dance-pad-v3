from ..utils import ModuleBase
from . import LogViewerModel, LogViewerView, LogViewerController

class LogViewer(ModuleBase):
    def __init__(self):
        super().__init__(LogViewerModel, LogViewerView, LogViewerController)