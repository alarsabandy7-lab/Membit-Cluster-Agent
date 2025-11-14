import discord

def safe_block(title, text):
    embed = discord.Embed(title=title, description=text[:3000], color=0x0099ff)
    return embed
