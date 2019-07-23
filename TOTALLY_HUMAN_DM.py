#!/usr/bin/python3
# Only run with Python 3.6

import random
import asyncio
import aiohttp
import json
import DM
import discord
from discord.ext import commands

BOT_PREFIX = ('!')

# Adjust if not running beta
with open('discord_beta.token', 'r') as file:
    TOKEN = file.read()

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command(name = 'roll',
                description = 'Will roll any number of dice - Write in #d#+... format',
                brief = 'Rolls any number of dice')
async def roll(ctx, *arg):
    l = DM.roll(''.join(arg))
    msg = 'YOU ROLLED THE NUMBERS {Rolls}, YIELDING A SUM OF {Sum}!'.format(Rolls = l, Sum = sum(l))
    await ctx.send(msg)

@client.command()
@commands.has_permissions(administrator=True)
async def logout(ctx):
    await ctx.send('Goodbye!')
    await client.logout()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='DND WITH OTHER HUMANS'))
    print('Logged in as ' + client.user.name)
    print('---------------------')
client.run(TOKEN)