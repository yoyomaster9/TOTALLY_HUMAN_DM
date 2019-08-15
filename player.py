import DM
import random
import json
import os

# Where user data is stored
PlayerDataDirectory = 'PlayerData/'

# Create folder if nonexistent
if not os.path.exists(PlayerDataDirectory):
    os.makedirs(PlayerDataDirectory)

class Player:
    def __init__(self, playerID, statmethod = 'standard', wallet = 0, **kwargs):
        self.__dict__.update(kwargs)
        self.wallet = wallet
        self.playerName = playerName
        if not hasattr(self, 'baseStats'):
            self.rollStats(statmethod)
        self.save()

    def save(self):
        dir = PlayerDataDirectory + self.playerID
        with open(dir, 'w') as file:
            data = vars(self)
            json.dump(data, file)

    def rollStats(self, statmethod):
        abilities = ['str', 'dex', 'con', 'int', 'wis', 'cha']
        if statmethod == 'standard':
            scores = [15, 14, 13, 12, 10, 8]
            random.shuffle(scores)
            self.baseStats = dict(zip(abilities, scores))
        elif statmethod == 'random':
            self.baseStats = dict()
            for a in abilities:
                rolls = [random.randint(1, 6) for x in range(4)]
                rolls.sort()
                self.baseStats[a] = sum(rolls[1:])

    # functions to determine stats based on items and base stats
    # returns the modifiers, not ability scores
    def str(self):
        pass
    def dex(self):
        pass
    def con(self):
        pass
    def int(self):
        pass
    def wis(self):
        pass
    def cha(self):
        pass

def loadPlayer(playerID):
    dir = PlayerDataDirectory + playerID
    try:
        with open(dir, 'r') as file:
            dict = json.load(file)
            return Player(**dict)
    except FileNotFoundError:
        print('File Error!!')
