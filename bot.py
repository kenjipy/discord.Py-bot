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
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency * 1000,  'ms')))


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f' user {member} has been kicked.')

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, self, user: discord.Member, *, reason=None):
    await member.mute(reason=reason)
    await ctx.send(f' user {member} has been muted.')



client.run('PUTTOKENHERE')
