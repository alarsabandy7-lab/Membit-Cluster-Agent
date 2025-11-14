import os
import discord
from bot import create_bot

def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise Exception("DISCORD_TOKEN not found. Please set environment variable.")

    bot = create_bot()
    bot.run(token)

if __name__ == "__main__":
    main()
