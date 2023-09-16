from tkinter import *

import os
import sys

sys.path.insert(0, os.getcwd() + os.sep + os.pardir)

from module import watchful_eye

'''
Intro to Tkinter: https://realpython.com/python-gui-tkinter/
'''

def main():

    overlay_data = watchful_eye()

    win = Tk()
    win.geometry("300x200")
    
    Label(win, text="Hello World!").pack(pady=20)
    for key in overlay_data:
        Label(win, text=overlay_data[key]).pack(padx=10, pady=10)

    win.attributes('-topmost', True)
    win.attributes('-alpha', 0.5)
    win.mainloop()


if __name__ == "__main__":
    main()