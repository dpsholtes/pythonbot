import os
import random
import requests
import json
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

@bot.command(name='weather', help = 'Gives current weather of a city.')
async def weather(ctx, city_name: str):
    api_key = "f447a8cebf03bf8ee549a7edd9bf0b06"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        weather_data = [
        'Temperature in Kelvin: ' + str(current_temperature), 
        'Atmospheric Pressure in hPa: ' + str(current_pressure),
        'Humidity Percentage: ' + str(current_humidity),
        'Description: ' + str(weather_description)
       ]

    else:
        weather_data = [
            'I\'m sorry, I was unable to find the weather conditions for ' + city_name + ' .'
        ]
    response = weather_data
    await ctx.send('\n '.join(response))

bot.run(TOKEN)