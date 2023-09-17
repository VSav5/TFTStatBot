import riotwatcher
import configparser
import os
from datetime import datetime

# REF: https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6

def disect_match(match, PUUID):
    for player in match["info"]['participants']:
        #print(player)
        if player["puuid"] == PUUID:
            for key, val in player.items():
                print(f"\t{key}: {val}") 

                if key == "traits":
                    for trait in val:
                        for key2, val2 in trait.items():
                            print(f"\t\t{key2}: {val2}")
                        print()
                elif key == "units":
                    for trait in val:
                        for key2, val2 in trait.items():
                            print(f"\t\t{key2}: {val2}")
                        print()

def get_placement_by_puuid(match, puuid):

    match_datetime = datetime.fromtimestamp(match["info"]["game_datetime"] / 1e3)
    if datetime.today().date() != match_datetime.date():
        return 0

    for player in match["info"]['participants']:
        if player["puuid"] == puuid:
            return player["placement"]

def parent_dir_and(f):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), f)

def watchful_eye():

    f = configparser.ConfigParser()
    f.read(parent_dir_and(os.pardir) + os.sep + "config.ini")
    config = f['config']
    
    watcher = riotwatcher.TftWatcher(config["API_KEY"])
    player = watcher.summoner.by_name(config["REGION"], config["SUMMONER_NAME"])
    ranked_stats = watcher.league.by_summoner(config["REGION"], player['id'])
    match_history = watcher.match.by_puuid(config["REGION"], player["puuid"])

    todays_match_placements = []
    for match_id in match_history:
        match = watcher.match.by_id(config["REGION"], match_id)
        placement = get_placement_by_puuid(match, player["puuid"])
        if placement > 0:
            todays_match_placements.append(placement)
    
    overlay_data = {}
    overlay_data["summoner_name"] = player["name"]
    try:
        overlay_data["tier"] = ranked_stats[0]["tier"]
        overlay_data["rank"] = ranked_stats[0]["rank"]
        overlay_data["lp"] = "" + str(ranked_stats[0]["leaguePoints"]) + " LP"
    except:
        overlay_data["tier"] = "UNRANKED"
        overlay_data["rank"] = ""
        overlay_data["lp"] = ""
    overlay_data["todays_match_placements"] = todays_match_placements
    overlay_data["todays_average"] = round(sum(todays_match_placements) / len(todays_match_placements), 1) if len(todays_match_placements) > 0 else 0

    css = os.listdir(parent_dir_and("css"))
    if f"{overlay_data['tier'].upper()}.png" in css:
        overlay_data["tier_icon"] = "css" + os.sep + overlay_data['tier'] + ".png"
    else:
        overlay_data["tier_icon"] = "Could Not Load Icon"
    print(overlay_data)
    return overlay_data

if __name__ == "__main__":
    #main()
    watchful_eye()