from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__, static_folder="css", template_folder="html")
app.url_map.strict_slashes = False

from module import watchful_eye

@app.route("/")
def base():
    return redirect(url_for("tracker"))

@app.route("/tracker")
def tracker():
    overlay_data = watchful_eye() 
    overlay_data["todays_match_placements"] = str(overlay_data["todays_match_placements"])
    return render_template("tracker_page.html", overlay_data=overlay_data)

@app.route("/get_overlay_data")
def get_overlay_data():
    print("Getting overlay data from backend...")
    data = watchful_eye()
    data["todays_match_placements"] = str(data["todays_match_placements"])
    return data

if __name__ == "__main__":
    app.run(port=5000)