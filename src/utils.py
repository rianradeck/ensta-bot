import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

GUILD = os.getenv("DISCORD_GUILD")
SERVER_ADMINS_LIST = os.getenv("SERVER_ADMINS_LIST")

client: commands.Bot = None


def load(_client: commands.Bot):
    global client
    client = _client


async def call_admin(ctx, e=None):
    guild = discord.utils.get(client.guilds, name=GUILD)
    server_admins = []
    for member in guild.members:
        if member.name in SERVER_ADMINS_LIST:
            server_admins.append(member)
    
    await ctx.send(
        "Something went very wrong, "
        f"call {server_admins[0].mention}\nException: {e}"
    )
