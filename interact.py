import discord
import os
import random
import interact
import time
from time import sleep
from keep_alive import keep_alive
from discord.ext import commands




async def teststuff():
  client = discord.Client()
  @client.event
  async def on_message(message):
    re = None
    if message.author != client.user:
      print("itworked")
      randomize = random.randint(1, 6)
      if (randomize == 1):
        xi = ("Hi I am on a zoom right now\ntalk later?")
      elif (randomize == 2):
        xi = ("Finally! Someone wants to talk to me!")
      elif (randomize == 3):
        xi = ("Hello, what would you like to talk about")
      elif (randomize == 4):
        xi = ("Hey, I am quite bored right now. Please intrest me")
      elif (randomize == 5):
        xi = ("Please kill Satan")
      else:
        xi = ("hello")
      await message.channel.send(xi)
def testvar(self):
  xi = 100



  def stringtolist(x):
  placeholder = ""
  placeholderlist = []
  # removes spaces
  for i in x:
    if i != " ":
      placeholder += i
  pholder2 = ""
  for i in placeholder:
    if i == ',':
      placeholderlist.append(float(pholder2))
      pholder2 = ""
    else:
      pholder2 += i
  placeholderlist.append(float(pholder2))
  return(placeholderlist)





import discord
import os
import random
client = discord.Client()
from keep_alive import keep_alive
from discord.ext import commands
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
people_and_number_of_messages = []
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content == "|hello":
          await message.channel.send("Hello!")
        if message.content == "|xkcd":
          await message.channel.send(f"https://xkcd.com/{random.randint(1,2355)}/")
        if message.content == "|kick me":
          discord.Member = message.author
          print(message.author)          
          await discord.Member.kick(reason = None)
        if message.content == "|Analog interface":
          print(message.content)
          await message.delete()
          if message.author.id == 515704039686668310:
            await message.channel.send(input("What do you want Samaritan to say: "))
        if message.content == "Samaritan, I summon you, smite this chat":
          for i in range(100):
            if message.author.id == 515704039686668310: 
              await message.channel.send("** ** \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ** **")   
        if message.content.startswith("testing "):
          breakdownlist = []
          for i in message.content:
            breakdownlist.append(i)
          breakdownlist = breakdownlist[9:len(breakdownlist) - 1]
          #13
          breakdownmessage = ""
          for i in breakdownlist:
            breakdownmessage += i
          allnumbers = stringtolist(breakdownmessage)
          print(stringtolist(breakdownmessage))
          print(allnumbers)