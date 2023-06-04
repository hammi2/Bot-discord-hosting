#from unicodedata import name
import discord
import json
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

#to load the cogs from ./cogs folder
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
  print("Bot now online")
  #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name = 'mouve'))
  await bot.change_presence(activity=discord.Streaming(name="/bot" , url='https://www.youtube.com/watch?v=-zY2hA8mRr4'))
  
@bot.command()
async def ping(ctx):
    await ctx.send(f"ping!{round(bot.latency * 1000)}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("error")
        await ctx.send(" you code is failed")
     
 
To = 'OTU2MTgyMTM5OTk1NTUzODQy'
ke = '.G_19bR.umqMjRn_'
ns = 'qiMlxUe9QDNPp0kaSGKPbeoOWllQlE'
Token = To + ke + ns
bot.run(Token)
