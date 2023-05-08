import types
from functools import wraps
from PyQt5.QtCore import pyqtSlot
from .logger import logger

def qt_slot(*args):
    if len(args) == 0 or isinstance(args[0], types.FunctionType):
        args = []
    pyqtSlot(*args)
    def slotdecorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args)
            except Exception as e:
                logger.add_error(e)
        return wrapper
    return slotdecorator