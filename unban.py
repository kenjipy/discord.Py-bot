@client.command()
@commands.has_permissions(Kick_member=True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} was unbanned.")
            return
