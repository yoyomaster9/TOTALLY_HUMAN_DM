import DM
import random
import json

class Item:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        # Needs - rarity, flavor text, ability mods,
        # will load from file
