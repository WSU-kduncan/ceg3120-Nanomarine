import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    futurama = [
        'Good news, everyone.',
        'Bite my shiny metal ass!',
        
            'You win again gravity',
            'By the way, I took the liberty of fertilizing your caviar.'
        
    ]

    if message.content == '!hitme':
        response = random.choice(futurama)
        
        await message.channel.send(response)

client.run(TOKEN)
