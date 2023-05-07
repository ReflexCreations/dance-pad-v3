class LogViewerModel:
    def __init__(self):
        self.log_messages = []

    def add_message(self, message):
        self.log_messages.append(message)