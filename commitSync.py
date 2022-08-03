from ast import main
import os
import datetime
import time

def gitSync():
    os.chdir("c:/Users/pillai_amal/")
    timenow = datetime.datetime.now()
    os.system("git add .")
    print("git add. - COMPLETE ")
    os.system('git commit -am "automated commit at {}"'.format(str(timenow)))
    print("git commit - COMPLETE")
    os.system("git push")
    print("git push -COMPLETE")
    //os.system("cls")
    print("\n \n Waiting for 10 minutes for next commit ... ")
    time.sleep(600)

