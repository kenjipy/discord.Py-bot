import discord
from discord.ext import commands
import random

from urllib import parse, request
import re

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('SETSTATUSHERE'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.command()
async def ping():


@client.command()
@commands.has_permissions(MANAGE_MASSAGE=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limet=amount)



client.run('PUTTOKENHERE')