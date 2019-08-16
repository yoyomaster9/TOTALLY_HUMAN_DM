import random, asyncio, aiohttp, json, sys, os
import discord
from discord.ext import commands
import tokens
import DM
import player

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

BOT_PREFIX = ('!')

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
async def roll(ctx, msg):
    print(msg)
    if not msg:
        await ctx.send('BZZT YOU NEED TO SPECIFY THE ROLL!')
    else:
        try:
            l = DM.roll(msg)
            msg = 'YOU ROLLED THE NUMBERS {Rolls}, YIELDING A SUM OF {Sum}!'.format(Rolls = l, Sum = sum(l))
            await ctx.send(msg)
        except:
            await ctx.send('I COULD NOT UNDERSTAND YOUR INPUT KRRT!!')

@client.command()
async def ping(ctx):
    print(ctx)
    print(ctx.author)
    p = player.Player(ctx.author)
    print(p.__dict__)

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


client.run(tokens.beta)
