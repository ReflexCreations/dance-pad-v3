import platform
import importlib

_system = platform.system()

if _system == "Linux":
    system = importlib.import_module(".system_linux", "utils").SystemLinux
elif _system == "Windows":
    system = importlib.import_module(".system_windows", "utils").SystemWindows
else:
    system = importlib.import_module(".system_unsupported", "utils").SystemUnsupported