import discord
from discord.ext import commands
import random
import os
import requests

anorganik = ["plastic", "botol", "kaca", "besi", "kertas"]
organik = ["leaves"," eggshells", "food", "vegeatable"]
b3 = ["electronic", "battery", "lightbulb", "flashlight"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def sampah(ctx, barang):
    if barang in anorganik:
      await ctx.send("Anorganic")
    if barang in organik:
      await ctx.send("Organik")
    if barang in b3:
      await ctx.send("B3")


bot.run("Not mine")
