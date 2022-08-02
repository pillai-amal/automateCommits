from ast import main
from ctypes.wintypes import PINT
import os
import datetime
import time


def gitSync():
    os.chdir("put your repo directory here")
    timenow = datetime.datetime.now()
    os.system("git add .")
    print("git add. - COMPLETE ")
    os.system('git commit -am "automated commit at {}"'.format(str(timenow)))
    print("git commit - COMPLETE")
    os.system("git push")
    print("git push -COMPLETE")
    print("\n \n Waiting for 30 minutes for next commit ... ")
    time.sleep(1800)

