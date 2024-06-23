import os
from dotenv import load_dotenv
import discord
from discord.app_commands import guilds
from discord.ext import commands
reason = discord.Intents.default
client = discord.Client(intents=reason)


@client.event
async def on_ready():
    print(f'{client.user} is connected to the following server:\n')
    for server in client.guilds:
        print(f'{server.name}(id: {server.id})')

@client.command(name="Minecraft", help="nope")

client.run(TOKEN)
