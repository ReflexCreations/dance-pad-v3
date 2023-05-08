import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
import platform
import importlib

_system = platform.system()

if _system == "Linux":
    SystemClass = importlib.import_module(".system_linux", "utils").SystemLinux
elif _system == "Windows":
    SystemClass = importlib.import_module(".system_windows", "utils").SystemWindows
else:
    SystemClass = importlib.import_module(".system_unsupported", "utils").SystemUnsupported

system = SystemClass()