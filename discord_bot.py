import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.', case_insensitive = True)
client.remove_command('help')

def get_token():
    with open('token.txt', 'r') as f:
        f_contents = f.readline()
        return f_contents


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! API latency is {round(client.latency * 1000)} ms")


extensions = ['command_events', 'admin_commands', 'member_commands', 'member_events', 'owner_commands', 'help_commands']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

print(f"Running discord.py version: {discord.__version__}")

client.run(get_token())