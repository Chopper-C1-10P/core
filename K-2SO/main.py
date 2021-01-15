import discord

from bots.K2SO import K2SO
from helpers.config import config
from extensions.events import Events
from extensions.fun import Fun
from extensions.help import Help
from extensions.info import Info
from extensions.moderation import Moderation
from extensions.owner import Owner
from extensions.utility import Utility
from extensions.wikipedia import Wikipedia

extensions = [
    Events,
    Fun,
    Help,
    Info,
    Moderation,
    Owner,
    Utility,
    Wikipedia
    ]

prefix = config("config.json", "k-2so_prefix")
token = config("config.json", "k-2so_token")

bot = K2SO(prefix)

for extension in extensions:
    try:
        bot.add_cog(extension(bot))
        print(f"Loaded extension {extension.__name__}!")
    except Exception as e:
        print(e)

bot.run(token)
