import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.command(name = 'Rick', help='Sends a Rick and Morty Quote')
async def rick(ctx):
    
    Rick_Quotes = [ 
        'It’s a figure of speech, Morty. They\'re bureaucrats. I don\'t respect them.',
        (
        '“Glip Glop?” You\'re lucky a Traflorkian doesn’t hear you say that. \n'
        'It\'s like the N-word and the C-word had a baby and it was raised by all the bad words for Jews.'
        ),
        'Wubalubadubdub!',
        'My life has been a lie! God is Dead! The government\'s lame! Thanksgiving is about killing Indians! Jesus wasn\'t born on Christmas! They moved the date! It was a pagan holiday!',
        'Do you wanna develop an app?',

    ]
    response = random.choice(Rick_Quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help = 'Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)