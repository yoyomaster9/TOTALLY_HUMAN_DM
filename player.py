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
    def __init__(self, user, statmethod = 'standard', wallet = 0, **kwargs):
        # author is discord ctx.user
        self.playerID = user.id
        self.playerName = user.name
        if os.path.exists(PlayerDataDirectory + str(self.playerID)):
            self.loadPlayer(self.playerID)
        else:
            kwargs['statmethod'] = statmethod
            kwargs['wallet'] = wallet
            self.newPlayer(kwargs)

    def newPlayer(self, kwargs):
            self.__dict__.update(kwargs)
            if not hasattr(self, 'baseStats'):
                self.rollStats(self.statmethod)
            self.save()

    def loadPlayer(self, playerID):
        dir = PlayerDataDirectory + str(playerID)
        with open(dir, 'r') as file:
            dict = json.load(file)
            self.__dict__.update(dict)

    def save(self):
        dir = PlayerDataDirectory + str(self.playerID)
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
