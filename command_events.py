from discord.ext import commands

class CommandEvents(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f'{ctx.command} was invoked incorrectly by {ctx.author.name}#{ctx.author.discriminator}')
        error = getattr(error, "original", error)
        # print(error)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author.mention} You do not have enough permissions.")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"You must provide all required arguments for said command.")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command not found")

        elif isinstance(error, commands.UserInputError):
            await ctx.send(f"Erroneous input")

        elif isinstance(error, commands.MissingAnyRole):
            roles_needed = error.missing_roles
            roles_needed = ', '.join(roles_needed)
            await ctx.send(f"You do not have the following role(s) required to run this command: {roles_needed}")

        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.channel.send(f"Bot doesn't have enough permissions")

        elif isinstance(error, commands.errors.NoPrivateMessage):
            await ctx.send("This command can't be used in a DM")

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f'{ctx.command} was invoked correctly by {ctx.author.name}#{ctx.author.discriminator}')

def setup(bot):
    bot.add_cog(CommandEvents(bot))