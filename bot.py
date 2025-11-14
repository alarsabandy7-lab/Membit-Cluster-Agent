import discord
from discord.ext import commands

from commands.hunt import hunt_cmd
from commands.analyze import analyze_cmd
from commands.whatis import whatis_cmd
from commands.trend import trend_cmd
from commands.context_cmd import context_cmd
from commands.mcp_lite import mcp_cmd

def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    # Register commands
    bot.add_command(hunt_cmd)
    bot.add_command(analyze_cmd)
    bot.add_command(whatis_cmd)
    bot.add_command(trend_cmd)
    bot.add_command(context_cmd)
    bot.add_command(mcp_cmd)

    @bot.event
    async def on_ready():
        print(f"Bot online as {bot.user}")

    return bot ￼Enter
