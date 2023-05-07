from abc import ABC, abstractmethod

class SystemBase(ABC):
    @abstractmethod
    def lock_access(self, pad):
        pass

    @abstractmethod
    def unlock_access(self, pad):
        pass