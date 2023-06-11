# First we will import our packages
import pandas as pd
import numpy as np
from sklearn import linear_model
import requests
from nba_api.live.nba import endpoints
from matplotlib import pyplot as plt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Here we access the leagueleaders module through endpoints & assign the class to "data"
    dataToday = endpoints.scoreboard.ScoreBoard().get_dict()
    # Our "data" variable now has built in functions such as creating a dataframe for our data
    gameData = dataToday.get('scoreboard').get('games')
    print(gameData)
    print(dataToday)

