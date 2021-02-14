import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= '-',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online<<")

@bot.event
async def on_member_join(member):
    cheannel = bot.get_channel(699598675659194368)
    await cheannel.send(f"{member} 進來了!")

@bot.event
async def on_member_remove(member):
    cheannel = bot.get_channel(699598713986744331)
    await cheannel.send(f"{member} 飛走了!")

@bot.command()
async def ping(ctx):
    await ctx.send("%0.1f ms"%(bot.latency*1000))


bot.run('ODEwNDAzNjI4NjY5MDc1NDg2.YCjJMQ.fQg4W0z0KiYbo_FaH85TMjwEfsU')