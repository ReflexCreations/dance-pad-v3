from injector import Module, Binder, Injector
from .pad_interface import PadInterface
from .log_viewer import LogViewer

class AppModule(Module):
    def configure(self, binder: Binder):
        binder.install(LogViewer)
        binder.install(PadInterface)

def setup_injector():
    return Injector(AppModule())