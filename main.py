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

winX = scrW/2
winY = scrH/2

winH = 200
winW = 500

xLoc = int(winX - (winW/2))
yLoc = int(winY - (winH/2))
print('Window location at: ' + str(xLoc) + ' ' + str(yLoc))

# Window Components START
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
# Window Components END
window.eval('tk::PlaceWindow . center')
window.title("Auto Mouse Mover")
window.geometry("{}x{}+{}+{}".format(winW,winH,xLoc,yLoc))
window.mainloop()


"""
while(autoloop == 0):
    for z in range(1,2):
        x = random.randint(0,500)
        y = random.randint(0,500)
        pyautogui.moveTo(x,y)
        time.sleep(2)
"""