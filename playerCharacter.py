import DM

import json
import os

# Where user data is stored
PlayerDataDirectory = 'PlayerData/'

# Create folder if nonexistent
if not os.path.exists(PlayerDataDirectory):
    os.makedirs(PlayerDataDirectory)

class User:
    def __init__(self, playerName,**kwargs):

        self.playerName = playerName
        self.rollStats()

        # In case extra variables are stored
        self.__dict__.update(kwargs)
        self.save()

    def save(self):
        dir = PlayerDataDirectory + self.nick
        with open(dir, 'w') as file:
            data = vars(self)
            json.dump(data, file)


def loadPlayer(nick):
    dir = PlayerDataDirectory + nick
    try:
        with open(dir, 'r') as file:
            dict = json.load(file)
            return User(**dict)
    except FileNotFoundError:
        print('File Error!!')