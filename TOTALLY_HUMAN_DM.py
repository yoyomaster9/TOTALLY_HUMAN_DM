import random, asyncio, aiohttp, json, sys, os
import discord
from discord.ext import commands
import tokens
import dm
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

    # Check if player is registered
    if message.content.startswith(BOT_PREFIX + 'register'):
        await client.process_commands(message)
    elif message.content.startswith(BOT_PREFIX + 'roll'):
        await client.process_commands(message)
    elif not player.exists(message.author.id) and message.content.startswith(BOT_PREFIX):
        await message.channel.send('KRRT ERROR PLAYER NOT REGISTERED')
    elif player.exists(message.author.id) and message.content.startswith(BOT_PREFIX):
        await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    print(error)
    await ctx.send('BZZT ERROR ERROR! I CANNOT DO THAT!!')

    if error == player.PlayerNotFoundError:
        await ctx.send('BZZT YOU NEED TO REGISTER A CHARACTER!')


@client.command(name = 'roll',
                description = 'Will roll any number of dice - Write in #d# + ... format',
                help = '''Example: 2d6 + 1d4 + 3 will simulate 2 six-sided dice, 1 four-sided die, and add 3 at the end.''',
                brief = 'Rolls any number of dice',
                aliases = ['r'])
async def roll(ctx, msg):
    if not msg:
        await ctx.send('BZZT YOU NEED TO SPECIFY THE ROLL!')
    else:
        try:
            l = dm.roll(msg)
            msg = 'YOU ROLLED THE NUMBERS {Rolls}, YIELDING A SUM OF {Sum}!'.format(Rolls = l, Sum = sum(l))
            await ctx.send(msg)
        except:
            await ctx.send('I COULD NOT UNDERSTAND YOUR INPUT KRRT!!')

@client.command()
async def ping(ctx):
    p = player.Player(ctx.author)
    await ctx.send('Pong!')
    await ctx.send('Player found:\n```{}```'.format(p.__dict__))


@client.command()
async def register(ctx):
    if player.exists(ctx.author.id):
        await ctx.send('ERROR! YOU HAVE ALREADY REGISTERED! USE THIS COMMAND TO REMOVE YOUR CURRENT CHARACTER!\n```{}delcharacter```'.format(BOT_PREFIX))
    elif not player.exists(ctx.author.id):
        p = player.Player(ctx.author)
        await ctx.send('PLAYER CREATED!')
        await ctx.send(p.printStats())
    else:
        await ctx.send('COMMAND UNKNOWN! TRY AGAIN!')

@client.command()
async def stats(ctx):
    p = player.Player(ctx.author)
    s = p.printStats()
    await ctx.send(s)

@client.command(brief = 'Logs bot out of all servers [ADMIN ONLY]',
                description = 'Logs bot out of all servers [ADMIN ONLY]')
async def logout(ctx):
    p = player.Player(ctx.author)
    if p.playerID == 241703543017308162:
        await ctx.send('GOODBYE!')
        await client.logout()
    else:
        await ctx.send('CANNOT USE THIS COMMAND!')

@client.command()
async def delcharacter(ctx):
    player.remove(ctx.author.id)
    await ctx.send('PLAYER REMOVED! CREATE NEW CHARACTER WITH ```{}register```'.format(BOT_PREFIX))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='DND WITH OTHER HUMANS'))
    print('Logged in as ' + client.user.name)
    print('---------------------')


client.run(tokens.release)
