import logging
import sys
from PyQt5.QtCore import QObject, pyqtSignal

class LoggerHandler(logging.Handler): 
    def __init__(self, formatter, level):
        super().__init__(level)
        self.setFormatter(formatter)

    def emit(self, record):
        formatted_record = self.format(record)
        self.logger.new_message.emit(formatted_record)

class Logger(QObject, logging.Logger):
    new_message = pyqtSignal(str)

    def __init__(self, name, level=logging.DEBUG):
        QObject.__init__(self, name=name)
        logging.Logger.__init__(self, name=name)
        self.logger = logging.getLogger(name)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = LoggerHandler(formatter, logging.DEBUG)
        handler.logger = self
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)
    
    def _add_message(self, level, message, traceback):
        exc_info = None
        if traceback:
            exc_type, exc_value, tb = sys.exc_info()
            if tb is not None and tb.tb_next is not None:
                while tb.tb_next is not None:
                    tb = tb.tb_next
                exc_info = (exc_type, exc_value, tb)
        self.logger.log(level, message, exc_info=exc_info)

    def add_critical(self, message, traceback=True):
        self._add_message(logging.CRITICAL, message, traceback)

    def add_error(self, message, traceback=True):
        self._add_message(logging.ERROR, message, traceback)

    def add_warning(self, message, traceback=False):
        self._add_message(logging.WARNING, message, traceback)

    def add_info(self, message, traceback=False):
        self._add_message(logging.INFO, message, traceback)

    def add_debug(self, message, traceback=False):
        self._add_message(logging.DEBUG, message, traceback)

    def add_message(self, message, traceback=False):
        self._add_message(logging.NOTSET, message, traceback)

logger = Logger(__name__)