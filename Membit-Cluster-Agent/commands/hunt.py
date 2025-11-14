from discord.ext import commands
from core.membit_client import fetch_clusters
from core.ai_engine import ai_insight
from core.utils import safe_block

@commands.command(name="hunt")
async def hunt_cmd(ctx, *, query: str):
    await ctx.send("🔍 Fetching clusters...")

    clusters = await fetch_clusters(query)
    if not clusters:
        return await ctx.send("No clusters found!")

    ai_result = await ai_insight(clusters)
    await ctx.send(embed=safe_block("Hunt Result", ai_result))
