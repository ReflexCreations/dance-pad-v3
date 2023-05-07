from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)