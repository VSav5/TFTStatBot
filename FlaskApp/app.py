from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__, static_folder="css", template_folder="html")
app.url_map.strict_slashes = False

import os
import sys

sys.path.insert(0, os.getcwd() + os.sep + os.pardir)

from module import watchful_eye

@app.route("/")
def base():
    return redirect(url_for("tracker"))

@app.route("/tracker")
def tracker():
    """ Static data for testing, since API calls take 5 ish seconds to get a response
    overlay_data = {'summoner_name': 'llVSAVll', 'tier': 'DIAMOND', 'rank': 'IV', 'lp': "62 LP", 'todays_match_placements': [], 'todays_average': 0, 'tier_icon': '/css/DIAMOND.png'}
    """
    overlay_data = watchful_eye() 
    return render_template("tracker_page.html", overlay_data=overlay_data)

@app.route("/get_overlay_data")
def get_overlay_data():
    print("Getting overlay data from backend...")
    """ Static data for testing
    data = {'summoner_name': 'llVSAVll', 'tier': 'DIAMOND', 'rank': 'IV', 'lp': "62 LP", 'todays_match_placements': [], 'todays_average': 0, 'tier_icon': '/css/DIAMOND.png'}
    data["tier"] = "CHALLENGER"
    data["rank"] = ""
    data["todays_match_placements"] = [1]
    data["tier_icon"] = '/css/CHALLENGER.png'
    """
    data = watchful_eye()
    return data

''' 
    Flask app is up and running and now displays the overlay data
    
    ARCHIVE: 
        - DONE : Figure out how to make a listener 
            - It has to be on the html/JS side becuase the tracker func returns the template, so it can not loop
            - Reference Lattice architecture for help
        - DONE : Figure out how the listener can make async calls to the watchful_eye func that only update the data on the page when it gets the return
        - DONE : Separate the user's league and rank in the watchful_eye return to make parsing league easier
        - DONE : Download images of each TFT league to display on the page that corresponds to the user's rank

    Next Steps:
        - Change ajax call to input correct data now that we have the html formatted how we want
        - Play around with grid display to align the box like tracker.gg version
            - tinker with other ideas for displaying the data, I don't have to mimic tracker.gg
'''

if __name__ == "__main__":
    app.run(port=5000)