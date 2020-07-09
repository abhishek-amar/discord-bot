from discord.ext import commands

class OwnerCog(commands.Cog, command_attrs = dict(case_insensitive = True, hidden = True)):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog):
        try:
            self.bot.load_extension(cog)
            await ctx.channel.send("Loaded successfully")
        
        except Exception as e:
            await ctx.channel.send(f"Error loading: {type(e).__name__} - {e}")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        try:
            self.bot.unload_extension(cog)
            await ctx.channel.send("Unloaded successfully")

        except Exception as e:
            await ctx.channel.send(f"Error unloading: {type(e).__name__} - {e}")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        try:
            self.bot.reload_extension(cog)
            await ctx.channel.send("Reloaded successfully")
        
        except Exception as e:
            await ctx.channel.send(f"Error reloading: {type(e).__name__} - {e}")

def setup(bot):
    bot.add_cog(OwnerCog(bot))