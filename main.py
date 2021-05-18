import os
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv

#from dotenv import find_dotenv

load_dotenv()
secret = os.getenv("TOKEN")
word = os.getenv("WORD")

print(word)


intents = discord.Intents.default()
description = '''A triva bot for vocal-synths and virtual idols* \n \ncreator: @riimo#1343 \nversion: 0.0.2 (pre-alpha)\n\n*virtual idol, utau, synth-v and cvio trivia comming soon! (^-^)'''

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
  question = random.randint(1,9)
  if question == 1:
    await ctx.send('Who is Aoki Lapis\'s sister - Miku, Meiko, Merli, or Mew?')
    
  if question == 2:
    await ctx.send('Who had the first multi-lingual voicebank - Luka, Lola, Leon, or Miku? ')
  if question == 3:
    await ctx.send('Which Crypton consert isn\'t a Japan exclusive - Magical Mirai, Miku Expo, NicoNico Cho Party, or VocAmerica?')
  if question == 4:
    await ctx.send("Which Voicebank set are confimermed to be twins - Kigamine Rin/Len, MEIKA Hime/Mikoto, Anon/Kanon, or Yuezheng Ling/Longya?")
  if question == 5:
    await ctx.send("Which non-crypton vocaloid has made a cameo in Project Mirai - Luo Tianyi, IA, Gumi, or SeeU?")
  if question == 6:
    await ctx.send("True or false, Project Diva Future Tone is a port of Project Diva Arcade.")
  if question == 7:
    await ctx.send("Which non-crypton vocaloud has their own video game (chose two) - IA, Gakupo, Oliver, or Gumi?")
  if question == 8:
    await ctx.send("Which Crypton vocal did not get a V2 Append - Miku, Rin, Luka, or Len?")
  if question == 9:
    await ctx.send("Which vocal did not move to CVio as an alternitive to V5 - Miku, IA, vFlower, or Yukari?")

bot.run(secret)

#coder - riimo#1343
#icon - VSinger (Luo Tianyi V4 Japanese)
#Hi there!