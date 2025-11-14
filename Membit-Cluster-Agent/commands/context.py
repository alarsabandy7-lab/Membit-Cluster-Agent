import discord

async def run(client, message, args, membit, ai):
    embed = discord.Embed(
        title="Context Agent",
        description=(
            "This agent uses Membit clusters + lightweight AI to generate "
            "real-time contextual insights. Built for fast scanning, risk spotting, "
            "and understanding emerging narratives."
        ),
        color=0x55AAFF
    )
    await message.channel.send(embed=embed)
