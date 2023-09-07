import tkinter as tk

import os
import sys

sys.path.insert(0, os.getcwd() + os.sep + os.pardir)

def main():
    root = tk.Tk()
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()