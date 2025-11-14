import discord

async def run(client, message, args, membit, ai):
    term = " ".join(args).strip()
    if not term:
        return await message.channel.send("Provide a term to explain.")

    try:
        definition = ai.define(term)
    except:
        definition = "No definition available."

    embed = discord.Embed(
        title=f"What is **{term}**?",
        description=definition,
        color=0x33AAFF
    )
    await message.channel.send(embed=embed)
