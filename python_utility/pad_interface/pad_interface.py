from ..utils import ModuleBase
from . import PadInterfaceModel, PadInterfaceView, PadInterfaceController

class PadInterface(ModuleBase):
    def __init__(self):
        super().__init__(PadInterfaceModel, PadInterfaceView, PadInterfaceController)