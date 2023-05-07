from injector import Module, Binder
from pad_interface import PadInterfaceModule, PadInterfaceController
from log_viewer import LogViewerModule, LogViewerController

class AppModule(Module):
    def configure(self, binder: Binder):
        binder.install(PadInterfaceModule)
        binder.install(LogViewerModule)
        binder.injector.get(PadInterfaceController)
        binder.injector.get(LogViewerController)