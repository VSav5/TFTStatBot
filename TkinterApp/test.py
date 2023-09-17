import tkinter as tk
from PIL import ImageTk, Image

import os
import sys

sys.path.insert(0, os.getcwd() + os.sep + os.pardir)

from module import watchful_eye

'''
Intro to Tkinter: https://realpython.com/python-gui-tkinter/
https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
'''

def main():

    overlay_data = watchful_eye()
    #overlay_data = {'summoner_name': 'emilyywang', 'tier': 'GRANDMASTER', 'rank': 'I', 'lp': '248 LP', 'todays_match_placements': [4, 8], 'todays_average': 6.0, 'tier_icon': 'C:\\Users\\Vincent\\Desktop\\TFTStatBot\\FlaskApp\\css\\GRANDMASTER.png'}
    overlay_data["tier_icon"] = "C:\\Users\\Vincent\\Desktop\\TFTStatBot\\TkinterApp\\rankicons\\GRANDMASTER.png"
    
    win = tk.Tk()
    #win.geometry("300x200")

    # {'summoner_name': 'llVSAVll', 'tier': 'UNRANKED', 'rank': '', 'lp': '', 'todays_match_placements': [], 'todays_average': 0, 'tier_icon': 'Could Not Load Icon'}


    overlay_data["tier_icon"]
    load = Image.open(overlay_data["tier_icon"])
    render = ImageTk.PhotoImage(load)
    tier_icon = tk.Label(win, image=render)
    tier_icon.grid(row=0, column=0, rowspan=3, padx=2)

    summoner_name = tk.Label(win, text=overlay_data["summoner_name"], font='16')
    summoner_name.grid(row=0, column=1, padx=2, sticky="sw")

    tier_rank_text = ""
    if overlay_data["tier"].lower() in ["master", "grandmaster", "challenger"]:
        tier_rank_text = overlay_data['tier']
    else:
        tier_rank_text = f"{overlay_data['tier']} {overlay_data['rank']}"
    tier_rank = tk.Label(win, text=tier_rank_text.upper(), font='bold 16')
    tier_rank.grid(row=1, column=1, padx=2, sticky="w")

    lp = tk.Label(win, text=overlay_data["lp"], font='16')
    lp.grid(row=2, column=1, padx=2, sticky="nw")

    todays_average = tk.Label(win, text=overlay_data["todays_average"], font='bold 25')
    todays_average.grid(row=0, column=2, rowspan=2, padx=6)
    tk.Label(win, text="Avg. Place", font='16').grid(row=2, column=2, padx=6, sticky="n")

    # List of data points to add to tkinter window
    todays_placements = tk.Label(win, text=str(overlay_data["todays_match_placements"]))
    todays_placements.grid(row=3, column=0, columnspan=3, sticky="w")

    """ for key in overlay_data:
        tk.Label(win, text="").pack(padx=10, pady=10)
        if key == "tier_icon":
            load = Image.open(overlay_data[key])
            render = ImageTk.PhotoImage(load)
            tk.Label(win, image=render).pack(padx=10, pady=10)
        else:
            text = key + " " + str(overlay_data[key])
            tk.Label(win, text=text).pack(padx=10, pady=10) """
    


    win.attributes('-topmost', True)
    #win.attributes('-alpha', 0.5)
    win.mainloop()


if __name__ == "__main__":
    main()