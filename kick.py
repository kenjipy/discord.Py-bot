import discord
from discord.ext import commands
import random
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix='PUTYOURPREFIXHERE')

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
