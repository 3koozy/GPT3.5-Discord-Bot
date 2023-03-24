import os
import discord
from discord.ext import commands
from discord import Intents
import aiohttp
import nest_asyncio
import openai

nest_asyncio.apply()

intents = Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Don't process messages sent by the bot itself
    if message.author == bot.user:
        return

    # Check if the bot was mentioned in the message
    if bot.user.mentioned_in(message):
    #     await message.channel.send(f'Hello {message.author.mention}! How can I help you?')

    # Process commands, if any
      response = openai.ChatCompletion.create(
          model='gpt-3.5-turbo',
          messages = [{"role": "system", "content": "you are a game dev consultant. Help the user to develop games."},
                      {"role": "system", "content": "provide a precise answer in less than 200 tokens."},
                        {"role": "user", "content": message.content}],
          max_tokens= 200,
          temperature= 0.7,
          n= 1
      )
      await message.channel.send(response['choices'][0]['message']['content'].strip())

# Replace 'your-gpt-3.5-api-key' with your actual GPT-3.5 API key
openai.api_key = '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'

# Replace 'your-discord-bot-token' with your actual Discord bot token
bot.start('MTA4ODY2NTQ4MzYzODc0MzEwMQ.G4gfHt.sjh_GeL-bts6Vc1p1XPsqOC7uoAxiMidD2dONs') #await 
