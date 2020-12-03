# CPSC 329 Unessay Project Group 12

## Introduction

For this project, we made a keylogger that targets the Windows 10 operating system. This keylogger will be hidden in a Trojan program that displays a gif of dancing pigs and runs the keylogger for the first time. The keylogger will send the target's keystrokes, time of keystroke and window where the key was pressed. to a Goggle Firebase database via an HTTP post request. Another script on the attacker's computer retrieves this data using an HTTP get request.

## Technologies

This project was created entirely (primarily) in Python 3 using several external libraries such as requests and the Google Firebase API. Both the keylogger and the Trojan file are bundled with necessary libraries into executable files so that the target does not need to have Python installed on their machine for the keylogger to run. It is assumed that the attacker has Python installed and those programs are run as standard Python scripts.

### Files

There are two folders in this project: main_ver and getLogFile. The files in the main_ver folder are placed on the target machine, namely the keylogger and the hook. The executable fies for both of these programs are inside the dist subfolder of main_ver. The other folder, getLogFile, contains the Python scripts needed to generate and read the log files as well as some smaple log files.

## Launch
To launch the keylogger or Trojan program (called hook.py or hook.exe), you can either run the Python file from the command line or click on the executable file in the dist folder.