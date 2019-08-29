import dm
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
    # Note: 'user' is the discord ctx.author class
    def __init__(self, user, wallet = 0, statmethod = 'standard', **kwargs):
        self.playerID = user.id
        self.playerName = user.name
        dir = PlayerDataDirectory + str(self.playerID)
        if os.path.exists(dir):
            with open(dir, 'r') as file:
                dict = json.load(file)
                self.__dict__.update(dict)
        else:
            self.wallet = wallet
            self.statmethod = statmethod
            self.xp = 0
            self.equipped = []
            self.items = []
            self.proficiencies = []
            self.proficiencyBonus = 2
            self.rollStats()
            self.save()

    def save(self):
        dir = PlayerDataDirectory + str(self.playerID)
        with open(dir, 'w') as file:
            data = vars(self)
            json.dump(data, file)

    def rollStats(self):
        abilities = ['str', 'dex', 'con', 'int', 'wis', 'cha']
        if self.statmethod == 'standard':
            scores = [15, 14, 13, 12, 10, 8]
            random.shuffle(scores)
            self.baseStats = dict(zip(abilities, scores))
        elif self.statmethod == 'random':
            self.baseStats = dict()
            for a in abilities:
                rolls = [random.randint(1, 6) for x in range(4)]
                rolls.sort()
                self.baseStats[a] = sum(rolls[1:])

    def printStats(self):
        s = 'Stat - Score - Mod'
        for x in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            s +='\n {}:   {:2}    ({:+d})'.format(x.upper(), self.baseStats[x], eval('self.' + x + '()'))
        s += '\nProficiency Bonus: +{}'.format(self.proficiencyBonus)
        s += '\nProficiencies: {}'.format(', '.join(self.proficiencies))
        s += '\nXP: {}'.format(self.xp)
        return '```' + s + '```'

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

# Check if player exists in PlayerData folder
def exists(playerID):
    dir = PlayerDataDirectory + str(playerID)
    return os.path.exists(dir)

def remove(playerID):
    dir = PlayerDataDirectory + str(playerID)
    os.remove(dir)
