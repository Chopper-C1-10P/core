import discord

from bots.K2SO import K2SO
from helpers.config import config
from cogs.events import Events
from cogs.fun import Fun
from cogs.help import Help
from cogs.info import Info
from cogs.moderation import Moderation
from cogs.owner import Owner
from cogs.utility import Utility
from cogs.wikipedia import Wikipedia

cogs = [
    Admin,
    Events,
    Fun,
    Help,
    Info,
    Moderation,
    Owner,
    Utility,
    Wikipedia
]

prefix = config("config.json", "k2so_prefix")
token = config("config.json", "k2so_token")

bot = K2SO(prefix)


for cog in cogs:
    try:
        bot.add_cog(cog(bot))
        print(f"Loaded {cog.__name__}!")
    except Exception as e:
        print(e)


bot.run(token)
