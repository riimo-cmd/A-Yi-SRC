import discord
import os
import random
import time

client = discord.Client()

BotPoints = 0

@client.event
async def on_ready():
    print('Logged in as')
    print('A-Yi')
    print('793240767702761473')
    print('------')


@client.event
async def on_message(message):
    #default
    if message.author == client.user:
        return
    #Test command
    if message.content.startswith('yi!hello'):
        await message.channel.send('Hello!')
    #Help command
    if message.content.startswith('yi!help'):
      await message.channel.send('Hello, I\'m A-Yi, an idol trivia bot. I currently only have vocaloid questions, but I\'ll be getting UTAU, CVio, and Love Live trivia soon! (^^)')
      await message.channel.send('Here\'s my commands:')
      await message.channel.send('help: this help message')
      await message.channel.send('vocaloid: a random vocaloid trivia message will appear')
      await message.channel.send('hello: I say hello. Hello! :D')
    #good bot/bad bot
    if message.content.startswith('good bot a-yi'):
      await message.channel.send('^^ thank you')
    if message.content.startswith('bad bot a-yi'):
      await message.channel.send('>:D')
    #vocaloid trivia
    if message.content.startswith('yi!vocaloid'):
      await message.channel.send('Time for vocaloid trivia :D')
      question = random.randint(1,3)
      if question == 1:
        await message.channel.send('Who is Aoki Lapis\'s sister - Merli, Miku, Kaito, or Kanon?')
        time.sleep(30)
        await message.channel.send('It\'s Merli')
    
      if question == 2:
        await message.channel.send('Who had the first multi-lingual voicebank - Luka, Lola, Miku, or Fukase? ')
        time.sleep(30)
        await message.channel.send('Luka was first! :D')

      if question == 3:
        await message.channel.send('Which song series has been adadapted into a stage play - samfree\'s \"Night\" series, mothy\'s \"Evillious Chronicles\", comos-p\'s \"___ of Hatsune Miku\" series, or suzumu\'s \"idol\" series?')
        time.sleep(30)
        await message.channel.send('It\'s the Evillious Chronicles! \nI wonder if I play a character in that series? 🤔')
      

      

#logon
client.run("lol")