import os
import sys
import ctypes

def forceAdmin():
    try:
         isAdmin =  ctypes.windll.shell32.IsUserAnAdmin()
    except:
        isAdmin =  False
    
    if not isAdmin:
        try:
            while not isAdmin:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                isAdmin =  ctypes.windll.shell32.IsUserAnAdmin()
        except:
           exit(1)

forceAdmin()

##dont run this code :) rl annoying piece of code