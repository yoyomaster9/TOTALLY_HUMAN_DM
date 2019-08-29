import random

def roll(s): # Simulates rolls of the form #d#+#d#..
    l = []
    s = s.lower()
    for i in s.split('+'):
        if 'd' in i:
            try:
                if i[0] == 'd':
                    i = '1' + i
            except:
                i = '1' + i
            [n, max] = [int(x) for x in i.split('d')]
            for j in range(n):
                l.append(random.randint(1, max))
        else:
            l.append(int(i))
    return l

import json
import os

# Where user data is stored
PlayerDataDirectory = 'PlayerData/'

# Create folder if nonexistent
if not os.path.exists(PlayerDataDirectory):
    os.makedirs(PlayerDataDirectory)

class Player:
    def __init__(self, playerName, statmethod = 'standard', wallet = 0, equipment = {}, **kwargs):
        self.__dict__.update(kwargs)
        self.wallet = wallet
        self.playerName = playerName
        if not hasattr(self, 'baseStats'):
            self.rollStats(statmethod)
        self.save()

    def save(self):
        dir = PlayerDataDirectory + self.playerName
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

    def str(self):
        modifiers = [item.stats['str'] for item in self.equipment]
        return self.baseStats['str'] + sum(modifiers)

    def dex(self):
        modifiers = [item.stats['dex'] for item in self.equipment]
        return self.baseStats['dex'] + sum(modifiers)

    def con(self):
        modifiers = [item.stats['con'] for item in self.equipment]
        return self.baseStats['con'] + sum(modifiers)

    def int(self):
        modifiers = [item.stats['int'] for item in self.equipment]
        return self.baseStats['int'] + sum(modifiers)

    def wis(self):
        modifiers = [item.stats['wis'] for item in self.equipment]
        return self.baseStats['wis'] + sum(modifiers)

    def cha(self):
        modifiers = [item.stats['cha'] for item in self.equipment]
        return self.baseStats['cha'] + sum(modifiers)

class Item:
    def __init__(self, name, brief, description, stats = {}):
        self.name = name
        self.brief = brief
        self.description = description
        # Expand on this

def loadPlayer(nick):
    dir = PlayerDataDirectory + nick
    try:
        with open(dir, 'r') as file:
            dict = json.load(file)
            return Player(**dict)
    except FileNotFoundError:
        print('File Error!!')

