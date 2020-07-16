from discord.ext import commands
import discord
import datetime as dt

class MemberEvents(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.log_channel = self.bot.get_channel(732908487717158962)
        self.welcome_channel = self.bot.get_channel(505992554697850890)
        self.guild =  self.bot.get_guild(505981261693845514)

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
        else:
            #Prevents attribute error if after is NoneType
            string_date_time = after.edited_at.strftime("%A, %B %d, %Y\n%H:%M:%S")
        embed4 = discord.Embed(
                title = 'Message Edit',
                colour = discord.Colour.blue()
                )
        embed4.set_author(
            name = f"{before.author.name}#{before.author.discriminator}\n({before.author.id})",
            icon_url = str(before.author.avatar_url)
        )
        embed4.add_field(name = "Channel:", value = f"{before.channel.mention}\n({before.channel.id})", inline = False)
        embed4.add_field(name = "Before:", value = before.content, inline = False)
        embed4.add_field(name = "After:", value = after.content, inline = False)
        embed4.set_footer(text = f'Message ID: {before.id}\n{string_date_time}')
        await self.log_channel.send(embed = embed4)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        #Prevents error if an embed is deleted (treated like an empty message)
        if not message.content:
            return

        #Checks audit logs if a user deleted his own message or someone else's message to edit the author of embed
        async for entry in self.guild.audit_logs(action = discord.AuditLogAction.message_delete, limit=1):
            if entry.user != entry.target:
                name = entry.user.name
                disc = entry.user.discriminator
                ident = entry.user.id
                pic = entry.user.avatar_url
            else:
                name = message.author.name
                disc = message.author.discriminator
                ident = message.author.id
                pic = message.author.avatar_url

        now_date_time = dt.datetime.now(dt.timezone.utc)
        string_date_time = now_date_time.strftime("%A, %B %d, %Y\n%H:%M:%S")
        embed5 = discord.Embed(title = "Message Delete", colour = discord.Colour.red())
        embed5.set_author(
            name = f"{name}#{disc}\n({ident})",
            icon_url= str(pic)
        )
        embed5.add_field(name = "Channel:", value = f"{message.channel.mention}")
        embed5.add_field(name = "Author:", value = f"{message.author.name}#{message.author.discriminator}\n({message.author.id})")
        embed5.add_field(name = "Message:", value = message.content, inline = False)
        embed5.set_footer(text = f'Message ID: {message.id}\n{string_date_time}')
        await self.log_channel.send(embed = embed5)
        
def setup(bot):
    bot.add_cog(MemberEvents(bot))