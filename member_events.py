from discord.ext import commands
import discord
import datetime as dt

class MemberEvents(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.log_channel = self.bot.get_channel(732908487717158962)
        self.welcome_channel = self.bot.get_channel(505992554697850890)
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.welcome_channel.send(f"{member.mention} has joined the server! Welcome!")
        role = discord.utils.get(member.guild.roles, name = 'whatever')
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left the server")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # Prevents empty message edits (like discord auto embedding YT links) from triggering this event
        # If this event is triggered for empty message edits, it will return a HTTP error saying that the embed 'value' is required
        # Boolean value of an empty string is False
        if not before.content or not after.content:
            return
        today_date = dt.date.today()
        string_date = today_date.strftime("%A, %B %d, %Y")
        now_time = dt.datetime.now()
        string_time = now_time.strftime("%H:%M:%S")
        embed4 = discord.Embed(
                title = 'Message Edit',
                colour = discord.Colour.blue()
                )
        embed4.set_author(
            name = f"{before.author.name}#{before.author.discriminator}\n({before.author.id})",icon_url=str(before.author.avatar_url)
        )
        embed4.add_field(name = "Channel:", value = f"{before.channel.mention}\n({before.channel.id})", inline = False)
        embed4.add_field(name = "Before:", value = before.content, inline = False)
        embed4.add_field(name = "After:", value = after.content, inline = False)
        embed4.set_footer(text = f'Message ID: {before.id}\n{string_date}\n{string_time}')
        await self.log_channel.send(embed = embed4)
    

def setup(bot):
    bot.add_cog(MemberEvents(bot))