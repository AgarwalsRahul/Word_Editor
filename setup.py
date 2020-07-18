import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Rahul Agarwal\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Rahul Agarwal\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("msg1.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Word editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )