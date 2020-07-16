from discord.ext import commands

class CommandEvents(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f'{ctx.command} was invoked incorrectly by {ctx.author.name}#{ctx.author.discriminator}')
        # error = getattr(error, "original", error)
        # print(error)
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(f"{ctx.author.mention} You do not have enough permissions.")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(f"You must provide all required arguments for said command.\nUse the `.help` command for more info")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.channel.send(f"Command not found")

        elif isinstance(error, commands.UserInputError):
            await ctx.channel.send(f"Erroneous input")

        elif isinstance(error, commands.MissingAnyRole):
            roles_needed = error.missing_roles
            roles_needed = ', '.join(roles_needed)
            await ctx.channel.send(f"You do not have the following role(s) required to run this command: {roles_needed}")

        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.channel.send(f"Bot doesn't have enough permissions")

        elif isinstance(error, commands.errors.NoPrivateMessage):
            await ctx.channel.send("This command can't be used in a DM")
        
        elif isinstance(error, commands.errors.CommandInvokeError):
            await ctx.channel.send("Command not found")
        
        else:
            raise error

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f'{ctx.command} was invoked correctly by {ctx.author.name}#{ctx.author.discriminator}')

def setup(bot):
    bot.add_cog(CommandEvents(bot))