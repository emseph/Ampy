import pyautogui
import random
import time
from tkinter import *

autoloop = 0

window = Tk()
window.resizable(False,False)

# Get display dimensions
scrH = window.winfo_screenheight()
scrW = window.winfo_screenwidth()
print("Screen Size is: " + str(scrW) + "x" + str(scrH))

# Set window dimensions
winH = 200
winW = 500

# Initialize screen location
winX = scrW/2
winY = scrH/2
winx = winW/2
winy = winH/2
xLoc = int(winX - winx)
yLoc = int(winY - winy)
print('Window location at: ' + str(xLoc) + ' ' + str(yLoc))

# Window Components START
btnStart = Button(window, text="Start")
btn.grid(column=0, row=0)
btnEnd = Button(window, text="End")
btn.grid(column=0, row=1)
# Window Components END

window.eval('tk::PlaceWindow . center')
window.title("Auto Mouse Mover")
window.geometry("{}x{}+{}+{}".format(winW,winH,xLoc,yLoc))
window.mainloop()


def move():
    while(autoloop == 0):
        for z in range(1,2):
            x = random.randint(0,500)
            y = random.randint(0,500)
            pyautogui.moveTo(x,y)
            time.sleep(2)
