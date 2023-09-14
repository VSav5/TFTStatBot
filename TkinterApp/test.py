from tkinter import *

import os
import sys

sys.path.insert(0, os.getcwd() + os.sep + os.pardir)

'''
Intro to Tkinter: https://realpython.com/python-gui-tkinter/
'''

def main():

    win = Tk()
    win.geometry("300x200")
    Label(win, text="Hello World!").pack(pady=20)
    win.attributes('-topmost', True)
    win.attributes('-alpha', 0.5)
    win.mainloop()


if __name__ == "__main__":
    main()