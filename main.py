import os
import random


import time

from time import sleep
from keep_alive import keep_alive
from discord.ext import commands
import discord.utils
from discord.utils import get
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from discord.ext import commands

bot = Bot(command_prefix='')


@bot.command()
async def commands(ctx):
    
    await ctx.send('Commands')
    embed=discord.Embed(title="Bot commands for Timmy Jr., Tom, and Caffine:", description="",color=discord.Color.blue())
    embed.add_field(name="start game", value="must use to gain xp to fight timmy", inline=False)
    embed.add_field(name="xp", value="gain xp to fight timmy and boost", inline=False)
    embed.add_field(name="work", value="also gain xp to fight timmy and boost", inline=False)
    embed.add_field(name="what are you doing?", value="Tom will answer", inline=False)
    embed.add_field(name="why", value="randomized answer", inline=False)
    embed.add_field(name="spam", value="spams in current channel and every message has a 4 percent chance of ending the spam", inline=False)
    embed.add_field(name="dm @person", value="spams their private dm, ex: spam @ThatGuy would spam thatguys dm", inline=False)
    await ctx.send(embed=embed)

@bot.command(name = "!clear")
async def xp(ctx):
  sleep(4)
  await ctx.send(f"You better not delete any pinned messages")

@bot.command(name = "xp")
async def xp(ctx):
  return

@bot.command(name = "-p ")
async def xp(ctx):
  li = random.randint(1, 2)
  if li == 1:
    await ctx.send("I hate that song")
  else:
    await ctx.send("ooh I love that song")

@bot.command(name = "-play ")
async def xp(ctx):
  li = random.randint(1, 2)
  if li == 1:
    await ctx.send("I hate that song")
  else:
    await ctx.send("ooh I love that song")

@bot.command(name="dm")
async def id_(ctx, user: discord.User):
    await ctx.send(f"its marks fault, {user.name}")
    spame = user
    spam = 1
    while spam == 1:
      await spame.send("marks fault sorry")
      sleep(1)
      spamr = random.randint(1, 25)
      print(spamr)
      if spamr == 25:
        spam = 3


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()



@bot.command(name="spam")
async def on_message(ctx):
  wh = "spam"
  spam = 1


  while spam == 1:
    await ctx.send("whats up?\nI'm bored")
    empty = " . "
    
    sleep(1)
    spamr = random.randint(1, 25)
    print(spamr)
    if spamr == 25:
      spam = 2

ROLE = "Spammer"
@bot.command(name="testp")
async def on_message(ctx, user: discord.User, member):
  await ctx.send(user)
  role = get(member.guild.roles, name=ROLE)
  await user.add_roles(role)
  await ctx.send("test complete")

# Accounts for paperclip robots
ROLE = "Spammer"





@bot.command(name="testt")
async def on_message(member):
  role = get(member.guild.roles, name=ROLE)
  await member.add_roles(role)
  
keep_alive()

token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
token2 = os.environ.get("DISCORD_BOT_SECRET2")
bot.run(token2)

#interact.teststuff()