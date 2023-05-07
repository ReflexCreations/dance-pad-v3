import logging
import sys
from .observer import Subject

class LoggerHandler(logging.Handler): 
    def __init__(self, formatter, level):
        super().__init__(level)
        self.setFormatter(formatter)
        self.last_log = ""

    def emit(self, record):
        self.last_log = self.format(record)

class Logger(Subject):
    def __init__(self):
        self.logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        handler = LoggerHandler(formatter, logging.DEBUG)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

        Subject.__init__(self)
        sys.excepthook = self.exception_hook

    def exception_hook(self, exc_type, exc_value, exc_traceback):
        self.add_message("Uncaught exception: {} - {}".format(exc_type.__name__, exc_value), level=logging.ERROR)

    def add_message(self, message, level=logging.INFO):
        self.logger.log(level, message)
        self.notify(self.logger.handlers[0].last_log)

logger = Logger()