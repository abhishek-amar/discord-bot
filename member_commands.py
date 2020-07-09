import discord
from discord.ext import commands

class MemberCommands(commands.Cog, command_attrs = dict(case_insensitive = True)):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'assignrole', aliases = ['addrole'])
    @commands.has_permissions(kick_members=True)
    async def add_role_command(self, ctx, role: discord.Role, member: discord.Member):
        await member.add_roles(role)
        await ctx.channel.send(f"{role.name} role has been added to {member.mention}")
    
    @commands.command(name = 'removerole', aliases = ['deleterole'])
    @commands.has_permissions(kick_members=True)
    async def remove_role_command(self, ctx, role: discord.Role, member: discord.Member):
        await member.remove_roles(role)
        await ctx.channel.send(f"{role.name} role has been removed from {member.mention}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def hello(self, ctx):
        await ctx.send(f"Hello,{ctx.author.mention}")
    
    @commands.command()
    async def channelid(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            await ctx.channel.send(f"Channel ID of {ctx.channel.mention} is: {ctx.channel.id}")
        else:
            await ctx.channel.send(f"Channel ID of {channel.mention} is: {channel.id}")
    
    @commands.command()
    async def userid(self, ctx, member: discord.Member = None):
        if member != None:
            await ctx.channel.send(f"User ID of {member.mention} is: {member.id}")
        else:
            await ctx.channel.send(f"User ID of {ctx.author.mention} is: {ctx.author.id}")
            
def setup(bot):
    bot.add_cog(MemberCommands(bot))