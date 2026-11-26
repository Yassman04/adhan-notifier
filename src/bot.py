import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")                      # hint: the token's name in .env
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))               # hint: your user ID's name; int() because IDs are numbers

intents = discord.Intents.default()          # what events the bot listens to; the defaults are enough
client = discord.Client(intents=intents)


@client.event                                # tells discord.py: call this when the event happens
async def on_ready():
    print(f"Logged in as {client.user}")
    channel = await client.fetch_channel(CHANNEL_ID)  # ask Discord for your user (we wait for the reply)
    await channel.send("TIME TO PRAY")                     # hint: your test message, as a string


client.run(TOKEN)                            # connects to Discord and keeps the bot running