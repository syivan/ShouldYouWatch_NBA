# First we will import our packages
import pandas as pd
import numpy as np
from sklearn import linear_model
import requests
from nba_api.live.nba import endpoints
from matplotlib import pyplot as plt

def verifyUserInput():
    teamNames=['Hawks', 'Celtics', 'Nets', 'Hornets',]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Here we access the leagueleaders module through endpoints & assign the class to "data"
    dataToday = endpoints.scoreboard.ScoreBoard().get_dict()
    # Our "data" variable now has built in functions such as creating a dataframe for our data
    gameData = dataToday.get('scoreboard').get('games')
    teamToWatch = input("What Team to Watch\n")
    print(dataToday)
    for i in range(len(gameData)):
        if (gameData[i].get('homeTeam').get('teamName') == teamToWatch):
            print('[%s]: %d' % (teamToWatch, gameData[i].get('homeTeam').get('score')))
        print(gameData[i])

    #r = requests.get("http://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2020/league/00_full_schedule.json")
    #print(type(r))
    #print(r.json())

