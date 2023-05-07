from .system_base import SystemBase
import mmap
import win32file
import win32api

class SystemWindows(SystemBase):
    def lock_access(self, pad):
        interface_buffer, interface_size = pad.get_feature_report(0)
        mmap_obj = mmap.mmap(-1, interface_size, tagname=f"Global\\reflex_pad_{pad.serial}")
        mmap_obj.write(interface_buffer)
        pad_file = win32file._get_osfhandle(mmap_obj.fileno())
        win32file.LockFileEx(pad_file, win32file.LOCKFILE_EXCLUSIVE_LOCK | win32file.LOCKFILE_FAIL_IMMEDIATELY, 0, win32api.UINT_MAX, win32file.PyOVERLAPPED())
        pad.locked_file_path = mmap_obj

    def unlock_access(self, pad):
        hfile = win32file._get_osfhandle(pad.locked_file_path.fileno())
        win32file.UnlockFileEx(hfile, 0, win32api.UINT_MAX, win32file.PyOVERLAPPED())
        pad.locked_file_path.close()