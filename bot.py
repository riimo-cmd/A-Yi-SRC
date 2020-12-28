import os
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
description = '''A triva bot for vocal-synths and virtual idols* \n *virtual idol, utau, synth-v and cvio trivia comming soon! '''

bot = commands.Bot(command_prefix='yi', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def vocaloid(ctx):
    '''Time for vocaloid trivia :D'''
    question = random.randint(1,2)
    if question == 1:
      await ctx.send('Who is Aoki Lapis\'s sister - Merlin, Miku, Kaito, or Kanon?')
    
    if question == 2:
      await ctx.send('Who had the first multi-lingual voicebank - Luka, Lola, Leon, or VY1? ')
    
bot.run('token')