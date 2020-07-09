from discord.ext import commands

class MemberEvents(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(505992554697850890)
        await channel.send(f"{member.mention} has joined the server! Welcome!")
        role = discord.utils.get(member.guild.roles, name = 'whatever')
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left the server")

def setup(bot):
    bot.add_cog(MemberEvents(bot))