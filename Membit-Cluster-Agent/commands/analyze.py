import discord

async def run(client, message, args, membit, ai):
    text = " ".join(args).strip()
    if not text:
        return await message.channel.send("Please provide text to analyze.")

    try:
        sentiment = ai.sentiment(text)
    except:
        sentiment = {"tag": "neutral", "score": 0.0}

    embed = discord.Embed(
        title="Sentiment Analysis",
        color=0x0099FF
    )
    embed.add_field(name="Input", value=text, inline=False)
    embed.add_field(name="Tag", value=sentiment["tag"], inline=True)
    embed.add_field(name="Score", value=str(sentiment["score"]), inline=True)

    await message.channel.send(embed=embed)
