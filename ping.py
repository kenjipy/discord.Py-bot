import discord
from discord.ext import commands
import random
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix='PUTYOURSTATUSHERE')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('SETSTATUSHERE'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency * 1000,  'ms')))
    
 
client.run('PUTTOKENHERE')
