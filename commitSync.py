from ast import main
from ctypes.wintypes import PINT
import os
import datetime
import time


def gitSync():
    os.chdir("C:/Users/pillai_amal/Documents/notes/vonB2")
    timenow = datetime.datetime.now()
    os.system("git add .")
    print("git add. - COMPLETE ")
    os.system("git commit -m 'automated commit at {}'".format(str(timenow)))
    print("git commit - COMPLETE")
    os.system("git push")
    print("git push -COMPLETE")
    time.sleep(1800)
    print("\n \n Waiting for 30 minutes for next commit ... ")