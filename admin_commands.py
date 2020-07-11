import discord
from discord.ext import commands

class AdministrationCommands(commands.Cog, name = 'admin'):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['purge'])
    @commands.has_permissions(kick_members=True)
    async def clear(self, ctx, num_lines = 5):
        await ctx.channel.purge(limit = num_lines + 1)
        await ctx.channel.send(f"Removed {num_lines} messages")

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
            await member.kick(reason = reason)
            await ctx.channel.send(f"{member.mention} has been kicked")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.channel.send(f"{member.mention} has been banned")
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for banned_user in banned_users:
            if (banned_user.user.name, banned_user.user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(banned_user.user)
                await ctx.channel.send(f"@{banned_user.user.name}#{banned_user.user.discriminator} has been unbanned")

def setup(bot):
    bot.add_cog(AdministrationCommands(bot))