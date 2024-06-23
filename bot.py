import os 
import discord
intents = discord.Intents.default()
from discord.app_commands import guilds
from discord.ext import commands
client = discord.Client(intents=intents)
#client = discord.Client(intents=discord.Intents.default())
#client = new Client(() intents: [Intents.FLAGS.GUILDS, #Intents.FLAGS.GUILD_MESSAGES] )
intents.message_content = True


@client.event
async def on_ready():
    print(f'{client.user} is connected to the following server:\n')
    for server in client.guilds:
        print(f'{server.name}(id: {server.id})')



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!commands'):
     await message.channel.send('!Minecraft, !Terraria, !Beam, !Forrest, !CSGO, !ARK')

  if message.content.startswith('!Minecraft'):
     await message.channel.send('Darriens 104.205.44.194:25566, Skyfactory 3 104.205.44.194:25567')

  if message.content.startswith('!Terraria'):
     await message.channel.send('Ryans 104.205.44.194:7777')

  if message.content.startswith('!Beam'):
     await message.channel.send('Beam Private 104.205.44.194:34197, Beam Public 104.205.44.194:34199')

  if message.content.startswith('!Forrest'):
     await message.channel.send('CBP Forest 104.205.44.194:8766')

  if message.content.startswith('!CSGO'):
      await message.channel.send('CSGO 104.205.44.194:27015')

  if message.content.startswith('!ARK'):
      await message.channel.send('ARK 104.205.44.194:27021')
   
  if message.content.startswith('!penis'):
      await message.channel.send('Sam is gay')
  
  if message.content.startswith('!shynoda'):
      await message.channel.send('is very cool')
my_secret = os.environ['Token']
client.run(my_secret)
