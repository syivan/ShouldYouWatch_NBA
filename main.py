# First we will import our packages
from nba_api.live.nba import endpoints

# MAIN
if __name__ == '__main__':
    # Access scoreboard modules in dictionary format
    dataToday = endpoints.scoreboard.ScoreBoard().get_dict()
    # gameData contains a value of games being played today
    gameData = dataToday.get('scoreboard').get('games')

    # Future: Plan to implement input to access different teams
    # teamToWatch = verifyUserInput()

    myTeam = 'Celtics'
    print(gameData)
    print(dataToday)
    for i in range(len(gameData)):
        # Checks in the iterated games array if the Celtics play in the games today
        currentHomeTeam = gameData[i].get('homeTeam')
        currentAwayTeam = gameData[i].get('awayTeam')
        if currentHomeTeam.get('name') == myTeam or currentAwayTeam.get('name') == myTeam:
            print('[%s]: %d\n[%s]: %d'.format(currentHomeTeam.get('name'),
                                              currentHomeTeam.get('score'),
                                              currentAwayTeam.get('name'),
                                              currentAwayTeam.get('score')))
            
