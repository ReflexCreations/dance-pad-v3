from .system_base import SystemBase
import fcntl

class SystemLinux(SystemBase):
    def lock_access(self, pad):
        pad_path = pad.fileno()
        fcntl.flock(pad_path, fcntl.LOCK_EX | fcntl.LOCK_NB)
        pad.locked_file_path = pad_path

    def unlock_access(self, pad):
        fcntl.flock(pad.locked_file_path, fcntl.LOCK_UN)