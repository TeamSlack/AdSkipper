import pyautogui as pag
import cv2
import time
import subprocess
import sys

try:
    with open("state.txt","r") as inStat:
        appStat = inStat.read()
        inStat.close()
        if appStat[8] == "0":
            try:
                subprocess.check_call("setup.bat")
                print("Setup complete")
                with open("state.txt","w+") as outStat:
                    outStat.write("install=1")
                    inStat.close()
            except CalledProcessError:
                print("Failed to run bat file")
        else:
            print("Already setup")
    print("App started, will automatically look for \"Skip Ads\" button ")
    while True:
        y = pag.locateOnScreen("Untitled_1.png",confidence=0.95)
        print(y)
        if y is not None:
            pag.moveTo(y[0],y[1])
            pag.move(0,32)
            print("Curr pos: ", pag.position())
            x1 = pag.locateOnScreen("skpAd1.png",confidence=0.95)
            print("x1: ",x1)
            if x1 is not None:
                pag.click(x1[0],x1[1])
            else:
                x2 = pag.locateOnScreen("skpAd.png",confidence=0.95)
                print("x2: ",x2)
                if x2 is not None:
                    pag.click(x2[0],x2[1])
            time.sleep(2)   
except KeyboardInterrupt:
    print("\nSaved")