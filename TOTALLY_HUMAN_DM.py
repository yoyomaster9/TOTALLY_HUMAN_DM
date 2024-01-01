import random, asyncio, aiohttp, json, sys, os
import discord
from discord.ext import commands
import tokens
import dm
import os
import sys

# Set working directory
os.chdir(sys.path[0])

intents = discord.Intents.default()

BOT_PREFIX = ('~')

client = commands.Bot(command_prefix=BOT_PREFIX, intents = intents)

@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return

    else:
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
async def roll(ctx, *msg):
    msg = list(msg)
    if not msg:
        await ctx.send('BZZT YOU NEED TO SPECIFY THE ROLL!')
        return
    elif msg[0] == 'stats':
        msg[0] = '4d6kh3 + 4d6kh3 + 4d6kh3 + 4d6kh3 + 4d6kh3 + 4d6kh3'
    try:
        msg = ''.join(msg)
        msg = msg.lower().replace(' ', '')
        l = [dm.Roll(s) for s in msg.split('+') if not s.isnumeric()]
        mods = [int(s) for s in msg.split('+') if s.isnumeric()]
        output = '\n'.join(str(x) for x in l)
        if mods != []:
            output += f'\nTotal mods: {sum(mods)}'
        if len(l) > 1 or len(mods) > 0:
            output += f'\nSum: `{sum(x.result for x in l) + sum(mods)}`'
        await ctx.send(output)
    except:
        await ctx.send('I COULD NOT UNDERSTAND YOUR INPUT KRRT!!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command(brief = 'Logs bot out of all servers [ADMIN ONLY]',
                description = 'Logs bot out of all servers [ADMIN ONLY]')
async def logout(ctx):
    if ctx.author.id == 241703543017308162:
        await ctx.send('GOODBYE!')
        await client.close()
    else:
        await ctx.send('CANNOT USE THIS COMMAND!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='DND WITH OTHER HUMANS'))
    print('Logged in as ' + client.user.name)
    print('---------------------')


client.run(tokens.release)
