import discord
from discord.ext import commands


class HelpCog(commands.Cog, name = 'helpcommand'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, arg = None):
        list_of_cogs = self.bot.cogs
        cog_names = []
        for x in list_of_cogs.items():
                cog_names.append(x.lower())
                cog_names_newline = '\n'.join(cog_names)
       
        if arg == None:
            await ctx.channel.send("Here is a list of command types:")
            await ctx.channel.send(cog_names_newline)


        else:
            arg = arg.lower()
            if arg in cog_names:
                some_cog = self.bot.get_cog(arg)
                list_of_commands = some_cog.get_commands()
                command_names = [c.name for c in list_of_commands]
                await ctx.channel.send('\n'.join(command_names))
            

            else:
                some_command = self.bot.get_command(arg)
                all_names = some_command.aliases.copy()
                all_names.insert(0, some_command.name)
                string_of_names = ' | '.join(all_names)
                await ctx.channel.send(f"Aliases: {string_of_names} Brief: {some_command.brief} Usage: {some_command.name} {some_command.usage}")

def setup(bot):
    bot.add_cog(HelpCog(bot))