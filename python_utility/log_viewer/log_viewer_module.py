from injector import Module, Binder, SingletonScope
from .log_viewer_model import LogViewerModel
from .log_viewer_view import LogViewerView
from .log_viewer_controller import LogViewerController

class LogViewerModule(Module):
    def configure(self, binder: Binder):
        binder.bind(LogViewerModel, scope=SingletonScope)
        binder.bind(LogViewerView, scope=SingletonScope)
        binder.bind(LogViewerController, scope=SingletonScope)