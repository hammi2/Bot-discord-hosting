import discord
import json
import os
import requests
import datetime
import time
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)
""""
#to load the cogs from ./cogs folder
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
"""
@bot.event
async def on_ready():
  print("Bot now online")
  

@bot.command()
async def ping(ctx, arg=None, option=1):
    if arg == "pong":
        await ctx.channel.send("You've already ponged yourself!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("error")
        await ctx.send(" you code is failed")
     
 @bot.command()
async def servers(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name=f'Servers({len(bot.guilds)})',value=f"".join(f"**{i}** `({i.member_count})` \n"for i in bot.guilds))
    await ctx.send(embed=embed)

@bot.command()
async def tax(ctx,*,input):
    input = input.replace('k','000')
    input = input.replace('m','000000')
    www = int(input)
    with_tax = round(www * 20) / 19 + 1
    embed= discord.Embed(description=f' Price: `{input}`\n With Tax: `{int(with_tax)}`',color=discord.Color.gold())
    embed.set_author(name=ctx.guild.name+' tax Calculator',icon_url=ctx.guild.icon_url)
    embed.set_footer(text=f'Required By {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

@bot.command()
async def user(ctx,user:discord.Member=None):
    if user is None:
        user = ctx.author
    embed = discord.Embed(color=discord.Color.red())
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name=user.name,icon_url=user.avatar_url)
    embed.add_field(name='Joined Discord :',value=f'**<t:{int(user.created_at.replace(tzinfo=datetime.timezone.utc).timestamp())}:R>**')
    embed.add_field(name='Joined Server :',value=f'**<t:{int(user.joined_at.replace(tzinfo=datetime.timezone.utc).timestamp())}:R>**')
    embed.set_footer(text=user.name,icon_url=user.avatar_url)
    await ctx.reply(embed=embed,mention_author=False)
    
@bot.command()
async def ch(ctx,url:str):
    imag = requests.get(url).content
    await bot.user.edit(avatar=imag)
    await ctx.send("Done.")
    

@bot.command()
async def unban(ctx, member):
    banUsers = await ctx.guild.bans()
    memberString = member.split("#")[0]
    memberNumber = member.split("#")[1]
    for banned in banUsers:
        user = banned.user

        if user.name == memberString and user.discriminator == memberNumber:
            await ctx.guild.unban(user)
            time.sleep(1)
            await ctx.channel.purge(limit=1)
            await ctx.send(f"unban {member}")
            return

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    time.sleep(0.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f"ban {member.mention}")
    
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    time.sleep(0.5)
    await ctx.channel.purge(limit=1)
    await ctx.send(f"kick {member.mention}")
    
@bot.command()
async def clear(ctx, *, amount=2):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"تم حذف {amount} رسائل")
    time.sleep(0.05)
    await ctx.channel.purge(limit=1)


To = 'OTU2MTgyMTM5OTk1NTUzODQy'
ke = '.G_19bR.umqMjRn_'
ns = 'qiMlxUe9QDNPp0kaSGKPbeoOWllQlE'
Token = To + ke + ns
bot.run(Token)
