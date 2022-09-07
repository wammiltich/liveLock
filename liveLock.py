import keyboard
from pyautogui import *
import pyautogui
import time,os
import datetime
import re


def settime():
    HR = re.compile(r"\d+")
    AP = re.compile(r"AM|PM")
    cutoff = ['','']
    while '' in cutoff:
        in_cutoff = input("Time to shutdown (e.g.: '3 AM', '2 PM'): ")
        try:
            cutoff[0] = HR.findall(in_cutoff)[0]
            cutoff[1] = AP.findall(in_cutoff)[0]
        except Exception as e:
            cutoff = ['','']
            print(f"Error interpretting input, follow example and try again\n{e}")
    return cutoff
#print("You have 5 seconds to minimize this window before mouse control is handed over")

def hour():
    hr = int(re.findall(r"^\d+",str(datetime.datetime.now().time()))[0])
    if hr >= 12:
        return [str(hr-12),"PM"]
    if hr < 12:
        return [str(hr),"AM"]

def abort():
    os.system('logoff')

def main():
    pid = os.getpid()
    HR = re.compile(r"\d+")
    AP = re.compile(r"AM|PM")
    pos = (1907,1066)
    cutoff = ['','']
    cutoff = settime()
    while hour() != cutoff:
        print(f"hour() ==> {hour()}\ncutoff ==> {cutoff}")
        #if keyboard.is_pressed('k'):
        #    break
        try:
            moveTo(pos)
        except pyautogui.FailSafeException as FSE:
            abort()
    abort()

if __name__ == "__main__":main()

''' Shutoff conditions:
1) if mouse is moved
2) if a certain hour is reached
3) TODO: find way to do from mobile? Would have to read text from disc
'''

''' Return to making a password protocol later. For now, self destruct
pw = ''
while len(pw)!=3:
    pw = input("3 character password: ")
    if len(pw)!=3:print("Please use 3 characters to set a password")
pw = [x for x in pw]
key = ['' for x in range(len(pw))]
'''