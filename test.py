import os
import sys
import win32com.shell.shell as shell
import ctypes

def checkAdminStatus():
    try:
         return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if not checkAdminStatus():
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        string1 = "net user administrator /active:yes"
        string2 = "runas /user:" + os.getenv('username') + "\Administrator /savecred" + os.path(test.py)
        os.write(string1)
        os.write(string2)
        print ("I am root now.")
        os.system("pause")
    except:
        print("no")
        os.system("pause")
        
else:
    print ("I am root now.")
    os.system("pause")
