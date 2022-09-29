# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from urllib.request import urlopen
import json
from datetime import datetime

#needed functions
def get_current_season():
    currentSeason = 0
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    
    if currentMonth > 7:
        currentSeason = currentYear
    else:
        currentSeason = currentYear - 1
        
    return currentSeason

def get_past_seasons():
    for season in range(startingSeason, currentSeason):
        for gameday in range(1, 35): # iterating over every gameday in the season
            url = "https://api.openligadb.de/getmatchdata/bl1/" + str(season) + "/" + str(gameday)
            json_obj = urlopen(url)
            data = json.load(json_obj)
            for game in range(0, 9): # iterating over every game of the gameday
                team1 = data[game]["team1"]["teamName"]
                team2 = data[game]["team2"]["teamName"]
                date = data[game]["matchDateTime"]
                scoreTeam1 = data[game]["matchResults"][0]["pointsTeam1"]
                scoreTeam2 = data[game]["matchResults"][0]["pointsTeam2"]
                df_gameday = df_gameday.append(
                {'season': season, 
                'gameday': gameday,
                'game': game,
                'date': date,
                'home_team': team1,
                'away_team': team2,
                'score_home_team': scoreTeam1,
                'score_away_team': scoreTeam2
                }
                , ignore_index=True)
                
def get_current_season():
    

#In the beginning I want to get as much data as possible
#starting from the first season available until the last gameday of the current season

#first season available is the 2003 season
startingSeason = 2009
currentSeason = get_current_season()

df_gameday = pd.DataFrame(columns = ['season', 'gameday', 'game', 'date', 'home_team', 'away_team', 'score_home_team', 'score_away_team'])
#getting the data from 2003 until the last finished season

#get_past_seasons()
#get_current_season()

#saving the gamedays in an Excel file
with pd.ExcelWriter('soccergames_data.xlsx') as writer:
    df_gameday.to_excel(writer, sheet_name='Sheet_1')
    
    
