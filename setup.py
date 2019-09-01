import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("app.py", base=base, icon="src/app_icon.ico")]

cx_Freeze.setup(
    name = "AMov",
    options = {"build_exe": {"packages":["tkinter","matplotlib","amov"], "include_files":["src/app_icon.ico"]}},
    version = "0.01",
    description = "Movement Analysis (with a Bitalino), Developed for a master student who worked at AnimalCare.",
    executables = executables
    )
