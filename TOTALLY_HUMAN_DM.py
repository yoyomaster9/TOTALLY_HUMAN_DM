#!/usr/bin/python3
# Only run with Python 3.6

'''
Example of format:
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True) # pass context to get the actual message - not necessary
async def eightball(context):
    await client.say(message)

---THIS PROJECT IS HEAVILY CLASS DRIVEN
Classes required:
    - Player character class
    -- Will need many functions to roll dice, determine checks/saves,
    - Monster Classes
    -- Monsters will have attributes
    -- Will have XP and gold to gain.
    - Equipment Classes
    -- Need classes for boons/extra damage

--- Potentially create classes in seperate .py file?
--- Have one file be running bot, second for handling backend...

THINGS TO BUILD
Dice roller - roll d20 for checks/saves
            - Will need to roll stats based on character class
            -- eg. character.roll('DEX') or character.roll('PERCEPTION')
            -- Accounts for proficiencies

Player Profile - randomly roll stats for characters
               - allow choosing for race
               - include equipment section
               - Need way to roll for checks based on characters
               -- character class - char.roll(DEX)?
               -- Have function cycle through all buffs/debuffs to add to roll
               -- Need advantage section

Dungeon Delver - kick down door and fight enemy for XP and gold
               - chance for equipment based on challenge of monster and rarity of item
               -- Will need sectioned equipment data (common/uncommon/rare/masterwork)
               -- Bot will not be very sophisticated, items will only provide boons/extra damage rolls
'''


import random
import asyncio
import aiohttp
import json
import DM
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ('!')

TokenFile = open('DiscordToken', 'r')
TOKEN = TokenFile.read()
TokenFile.close()

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name = 'roll',
                description = 'Will roll any number of dice - Write in #d# + ... format',
                brief = 'Rolls any number of dice')
async def roll(arg):
    l = DM.roll(arg)
    msg = 'YOU ROLLED THE NUMBERS {Rolls}, YIELDING A SUM OF {Sum}!'.format(Rolls = l, Sum = sum(l))
    await client.say(msg)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='DND WITH OTHER HUMANS'))
    print("Logged in as " + client.user.name)
client.run(TOKEN)