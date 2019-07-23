#!/usr/bin/python3
# Only run with Python 3.6

import random
import asyncio
import aiohttp
import json
import sys
import DM
import discord
from discord.ext import commands

BOT_PREFIX = ('!')

# run python file with beta after
if sys.argv[1].lower() == 'beta':
    filepath = 'discord_beta.token'
else:
    filepath = 'discord.token'

with open(filepath, 'r') as file:
    TOKEN = file.read()

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    print(error)
    await ctx.send('BZZT ERROR ERROR! I CANNOT DO THAT!!')

@client.command(name = 'roll',
                description = 'Will roll any number of dice - Write in #d# + ... format',
                help = '''Example: 2d6 + 1d4 + 3 will simulate 2 six-sided dice, 1 four-sided die, and add 3 at the end.''',
                brief = 'Rolls any number of dice',
                aliases = ['r'])
async def roll(ctx, *arg):
    if not arg:
        await ctx.send('BZZT YOU NEED TO SPECIFY THE ROLL!')
    else:
        l = DM.roll(''.join(arg))
        msg = 'YOU ROLLED THE NUMBERS {Rolls}, YIELDING A SUM OF {Sum}!'.format(Rolls = l, Sum = sum(l))
        await ctx.send(msg)


@commands.has_permissions(administrator=True)
@client.command(brief = 'Logs bot out of all servers [ADMIN ONLY]',
                description = 'Logs bot out of all servers [ADMIN ONLY]')
async def logout(ctx):
    await ctx.send('Goodbye!')
    await client.logout()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='DND WITH OTHER HUMANS'))
    print('Logged in as ' + client.user.name)
    print('---------------------')
client.run(TOKEN)