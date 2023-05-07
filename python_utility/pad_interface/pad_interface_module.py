from injector import Binder, Module, SingletonScope
from .pad_interface_model import PadInterfaceModel
from .pad_interface_view import PadInterfaceView
from .pad_interface_controller import PadInterfaceController

class PadInterfaceModule(Module):
    def configure(self, binder: Binder):
        binder.bind(PadInterfaceModel, scope=SingletonScope)
        binder.bind(PadInterfaceView, scope=SingletonScope)
        binder.bind(PadInterfaceController, scope=SingletonScope)