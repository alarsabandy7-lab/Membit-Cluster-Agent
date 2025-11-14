import discord

async def run(client, message, args, membit, ai):
    keyword = " ".join(args).strip()
    if not keyword:
        return await message.channel.send("Provide a keyword to scan.")

    data = membit.search(keyword)
    clusters = data.get("clusters", [])

    if not clusters:
        return await message.channel.send("No clusters found.")

    summary = "\n".join([f"- {c.get('summary','')}" for c in clusters[:5]])

    embed = discord.Embed(
        title=f"Trend Scan: {keyword}",
        description=summary,
        color=0x00CCFF
    )
    await message.channel.send(embed=embed)
