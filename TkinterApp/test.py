from tkinter import *
from PIL import ImageTk, Image

import os
import sys

sys.path.insert(0, os.getcwd() + os.sep + os.pardir)

from module import watchful_eye

'''
Intro to Tkinter: https://realpython.com/python-gui-tkinter/
'''

def main():

    overlay_data = watchful_eye()
    overlay_data["tier_icon"] = "C:\\Users\\Vincent\\Desktop\\TFTStatBot\\TkinterApp\\rankicons\\image.png"

    win = Tk()
    win.geometry("300x200")

    for key in overlay_data:
        if key == "tier_icon":
            load = Image.open(overlay_data[key])
            render = ImageTk.PhotoImage(load)
            Label(win, image=render).pack(padx=10, pady=10)
        else:
            text = key + " " + str(overlay_data[key])
            Label(win, text=text).pack(padx=10, pady=10)

    win.attributes('-topmost', True)
    win.attributes('-alpha', 0.5)
    win.mainloop()


if __name__ == "__main__":
    main()