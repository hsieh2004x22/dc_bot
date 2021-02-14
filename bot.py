import discord
from discord.ext import commands
import json
with open('setting.json','r',encoding='utf8') as jfile:
    jdata =json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= '?!',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online<<")

@bot.event
async def on_member_join(member):
    cheannel = bot.get_channel(int(jdata['comecheannel']))
    await cheannel.send(f"{member} 進來了!")

@bot.event
async def on_member_remove(member):
    cheannel = bot.get_channel(int(jdata['leavecheannel']))
    await cheannel.send(f"{member} 飛走了!")

@bot.command()
async def ping(ctx):
    await ctx.send("%0.1f ms"%(bot.latency*1000))


bot.run(jdata['TOKEN'])