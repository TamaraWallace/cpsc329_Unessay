import os
import sys
import win32com.shell.shell as shell
import shutil
import ctypes


if not ctypes.windll.shell32.IsUserAnAdmin():
    print('Not enough priviledge, restarting...')
    import sys
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    exit(0)
else:
	print('Elevated privilege acquired')

# Insert code to write bat file here