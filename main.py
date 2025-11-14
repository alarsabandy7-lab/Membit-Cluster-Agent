import os
import discord
from discord.ext import commands

# ===== Load Engine =====
from engine.membit_client import MembitClient
from engine.ai_client import AIClient

# ===== Bot Setup =====
INTENTS = discord.Intents.default()
INTENTS.message_content = True

bot = commands.Bot(command_prefix="!", intents=INTENTS)

# ===== Load Clients =====
membit = MembitClient()
ai = AIClient()


# ===== Auto Import Commands =====
def load_commands():
    commands_folder = "commands"
    for filename in os.listdir(commands_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            try:
                module = __import__(f"{commands_folder}.{module_name}", fromlist=["run"])
                # Bind command
                async def cmd(ctx, *args, module=module):
                    await module.run(bot, ctx.message, args, membit, ai)
                bot.command(name=module_name)(cmd)
                print(f"[OK] Loaded command: {module_name}")
            except Exception as e:
                print(f"[ERR] Failed to load {module_name}: {e}")


@bot.event
async def on_ready():
    print(f"Bot ready as {bot.user}")


# ===== Initialize & Run =====
if __name__ == "__main__":
    load_commands()
    bot.run(os.getenv("DISCORD_TOKEN"))
