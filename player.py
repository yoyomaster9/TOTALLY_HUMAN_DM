import DM
import random
import json
import os

# Where user data is stored
PlayerDataDirectory = 'PlayerData/'

# Create folder if nonexistent
if not os.path.exists(PlayerDataDirectory):
    os.makedirs(PlayerDataDirectory)

class PlayerNotFoundError(Exception):
    pass

class Player:
    # def __init__(self, user, statmethod = 'standard', wallet = 0, **kwargs):
    #     # author is discord ctx.user
    #     self.playerID = user.id
    #     self.playerName = user.name
    #
    #     if os.path.exists(PlayerDataDirectory + str(self.playerID)):
    #         dir = PlayerDataDirectory + str(self.playerID)
    #         with open(dir, 'r') as file:
    #             dict = json.load(file)
    #             self.__dict__.update(dict)
    #     else:
    #         self.__dict__.update(kwargs)
    #         self.statmethod = statmethod
    #         self.wallet = wallet
    #         self.equipped = []
    #         self.items = []
    #         self.rollStats(self.statmethod)
    #         self.save()

    def __init__(self, user, **kwargs):
        self.playerID = user.id
        self.playerName = user.name

        dir = PlayerDataDirectory + str(self.playerID)
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
        x = self.baseStats['str']//2 - 5
        for item in self.equipped:
            x += item.str
        return x
    def dex(self):
        x = self.baseStats['dex']//2 - 5
        for item in self.equipped:
            x += item.dex
        return x
    def con(self):
        x = self.baseStats['con']//2 - 5
        for item in self.equipped:
            x += item.con
        return x
    def int(self):
        x = self.baseStats['int']//2 - 5
        for item in self.equipped:
            x += item.int
        return x
    def wis(self):
        x = self.baseStats['wis']//2 - 5
        for item in self.equipped:
            x += item.wis
        return x
    def cha(self):
        x = self.baseStats['cha']//2 - 5
        for item in self.equipped:
            x += item.cha
        return x
