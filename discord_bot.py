import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

def get_token():
    with open('discord-bot/token.txt', 'r') as f:
        f_contents = f.readline()
        return f_contents


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! API latency is {round(client.latency * 1000)} ms")


extensions = ['command_events', 'admin_commands', 'member_commands', 'member_events', 'owner_commands']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

print(f"Running discord.py version: {discord.__version__}")

client.run(get_token())