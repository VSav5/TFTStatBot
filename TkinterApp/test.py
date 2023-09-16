import tkinter as tk
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

    win = tk.Tk()
    win.geometry("300x200")

    # {'summoner_name': 'llVSAVll', 'tier': 'UNRANKED', 'rank': '', 'lp': '', 'todays_match_placements': [], 'todays_average': 0, 'tier_icon': 'Could Not Load Icon'}


    overlay_data["tier_icon"]
    load = Image.open(overlay_data["tier_icon"])
    render = ImageTk.PhotoImage(load)
    tk.Label(win, image=render, ).pack(padx=10, pady=10)
    
    # List of data points to add to tkinter window
    overlay_data["summoner_name"]
    overlay_data["tier"]
    overlay_data["rank"]
    overlay_data["lp"]
    overlay_data["todays_match_placements"]
    overlay_data["todays_average"]
    tk.Label(win, text="").pack(padx=10, pady=10)

    """ for key in overlay_data:
        if key == "tier_icon":
            load = Image.open(overlay_data[key])
            render = ImageTk.PhotoImage(load)
            tk.Label(win, image=render).pack(padx=10, pady=10)
        else:
            text = key + " " + str(overlay_data[key])
            tk.Label(win, text=text).pack(padx=10, pady=10) """
    


    win.attributes('-topmost', True)
    win.attributes('-alpha', 0.5)
    win.mainloop()


if __name__ == "__main__":
    main()