import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id:{guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi{member.name}, welcome to my Discord server'
    )
@client.event
async def on_message(message):
    #makes the bot not talk to itself
    if message.author == client.user:
        return
    
    Rick_Quotes = [ 
        #'It\’s a figure of speech, Morty. They\’re bureaucrats. I don\’t respect them.',
        (
        '“Glip Glop?” You\’re lucky a Traflorkian doesn\’t hear you say that. \n'
        'It\’s like the N-word and the C-word had a baby and it was raised by all the bad words for Jews.'
        ),

    ]
    if message.content == 'Rick!':
        response = random.choice(Rick_Quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)