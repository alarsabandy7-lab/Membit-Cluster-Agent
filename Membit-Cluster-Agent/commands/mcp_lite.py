import discord

async def run(client, message, args, membit, ai):
    keyword = " ".join(args).strip()
    if not keyword:
        return await message.channel.send("Provide a keyword.")

    data = membit.search(keyword)
    clusters = data.get("clusters", [])

    if not clusters:
        return await message.channel.send("No clusters found.")

    combined = "\n".join([c.get("summary", "") for c in clusters[:5]])

    try:
        result = ai.mcp_lite(combined)
    except:
        result = {"risk": "unknown", "opportunity": "unknown", "summary": "N/A"}

    embed = discord.Embed(
        title=f"MCP-Lite Processing: {keyword}",
        color=0x7777FF
    )
    embed.add_field(name="Summary", value=result["summary"], inline=False)
    embed.add_field(name="Risk", value=result["risk"], inline=True)
    embed.add_field(name="Opportunity", value=result["opportunity"], inline=True)

    await message.channel.send(embed=embed)
