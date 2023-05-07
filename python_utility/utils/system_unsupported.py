from .system_base import SystemBase

class SystemUnsupported(SystemBase):
    def lock_access(self, pad):
        raise NotImplementedError("Method not implemented for this system type.")

    def unlock_access(self, pad):
        raise NotImplementedError("Method not implemented for this system type.")