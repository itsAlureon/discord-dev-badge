import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
GUILD_ID = discord.Object(id=123456789)  # <-- Put your server's Guild ID here as an integer

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync(guild=GUILD_ID) 
        print(f"Synced {len(synced)} command(s) to guild {GUILD_ID.id}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}! 👋")

bot.run(TOKEN)
