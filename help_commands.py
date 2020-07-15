import discord
from discord.ext import commands
import datetime as dt


class HelpCog(commands.Cog, name = 'helpcmds'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, arg = None):
        list_of_cogs = self.bot.cogs
        cog_names = []
        for x in list_of_cogs:
                if 'cmds' in x:
                    cog_names.append(x.lower())
                    cog_names_newline = '\n'.join(cog_names)
        today_date = dt.date.today()
        string_date = today_date.strftime("%A, %B %d, %Y")
        now_time = dt.datetime.now()
        string_time = now_time.strftime("%H:%M:%S")
        command_invoked_by = f'Invoked by {ctx.author.name}#{ctx.author.discriminator}'
       
        if arg == None:
            embed1 = discord.Embed(
            title = 'Help',
            description = 'General help dialog for bot',
            colour = discord.Colour.blue()
            )
            # self.bot.user returns a ClientUser which has the avatar_url method
            embed1.set_author(name = f"{self.bot.user.name}#{self.bot.user.discriminator}", icon_url=str(self.bot.user.avatar_url))
            embed1.add_field(name = "List of command types: ", value = cog_names_newline)
            embed1.set_footer(text = f'{command_invoked_by}\n{string_date}\n{string_time}')
            await ctx.channel.send(embed = embed1)

        else:
            arg = arg.lower()
            if arg in cog_names:
                some_cog = self.bot.get_cog(arg)
                list_of_commands = some_cog.get_commands()
                command_names = [c.name for c in list_of_commands]
                command_names_str = '\n'.join(command_names)
                embed2 = discord.Embed(
                title = 'Help',
                description = 'Help for a category of commands',
                colour = discord.Colour.blue()
                )
                embed2.set_author(name = f"{self.bot.user.name}#{self.bot.user.discriminator}", icon_url=str(self.bot.user.avatar_url))
                embed2.add_field(name = f"List of commands under {arg}: ", value = command_names_str)
                embed2.set_footer(text = f'{command_invoked_by}\n{string_date}\n{string_time}')
                await ctx.channel.send(embed = embed2)
            

            else:
                some_command = self.bot.get_command(arg)
                all_names = some_command.aliases.copy()
                all_names.insert(0, some_command.name)
                string_of_names = ' | '.join(all_names)
                embed3 = discord.Embed(
                title = 'Help',
                description = f'Help for {arg} command',
                colour = discord.Colour.blue()
                )
                embed3.set_author(name = f"{self.bot.user.name}#{self.bot.user.discriminator}", icon_url=str(self.bot.user.avatar_url))
                embed3.add_field(name = "Aliases:", value = f"`{string_of_names}`", inline = False)
                embed3.add_field(name = "Brief description:", value = some_command.brief, inline = False)
                embed3.add_field(name = "Usage:", value = f"`.[{string_of_names}] {some_command.usage}`", inline = False)
                embed3.set_footer(text = f'{command_invoked_by}\n{string_date}\n{string_time}')
                await ctx.channel.send(embed = embed3)
    

def setup(bot):
    bot.add_cog(HelpCog(bot))