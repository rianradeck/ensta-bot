import asyncio
import copy
import os
from pathlib import Path
from threading import Thread

import subprocess
import discord
import pytubefix
from discord.ext import commands

from utils import call_admin

song_queue = []
client: commands.Bot = None
root_path = Path(__file__).parent.parent.parent


def load_net_info(_client: commands.Bot):
    global client
    client = _client

    load_commands()


def load_commands():
    client.command()(ip)

async def ip(ctx: commands.Context, *args):
    subcommand, *query = args

    match subcommand:
        case "info":
            ipconfig = (subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE ).communicate()[0]).decode("utf-8")
            info_start = ipconfig.find("Wi-Fi")
            info_end = info_start
            n_collons = 0
            while n_collons < 12:
                if ipconfig[info_end] == ":":
                    n_collons += 1
                info_end += 1
            infos = ipconfig[info_start:info_end].split("\n")
            infos = "```" + "\n".join(infos[2:-1]) + "```"
            infos = infos.replace(". ", "")
            infos = infos.replace(" :", ":")
            await ctx.send(infos)
        case _:
            await ctx.send("Invalid subcommand.")
