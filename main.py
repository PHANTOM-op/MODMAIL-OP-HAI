from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
# we need members intent too
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
	print("The bot is online!")
	bot.load_extension("cogs.onMessage")

bot.run(os.environ.get("NzczNzUzOTU0NjIyMjQyODE3.X6N0hg.6HJAtO0x5xzZ_q7YpVl01-6l3zI"))
