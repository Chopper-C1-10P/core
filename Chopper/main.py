import discord
from discord.ext.commands import Bot

from helpers.config import config
from cogs.events import Events
from cogs.fun import Fun
from cogs.help import Help
from cogs.info import Info
from cogs.moderation import Moderation
from cogs.owner import Owner
from cogs.utility import Utility
from cogs.wikipedia import Wikipedia

intents = discord.Intents.all()

prefix = config("config.json", "chopper_prefix")
token = config("config.json", "chopper_token")

cogs = [
    Events,
    Fun,
    Help,
    Info,
    Moderation,
    Owner,
    Utility,
    Wikipedia
]

class Chopper(Bot):
    def __init__(self):
        super().__init__(command_prefix=prefix,
                         intents=intents)

        self.color = 0x2F3136

        self.remove_command("help")
        self.loop.create_task(self.when_ready())

    async def when_ready(self):
        await self.wait_until_ready()

        for cog in cogs:
            try:
                self.add_cog(cog(self))
            except Exception as e:
                print(e)
        print(f"Loaded cogs...")

        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{self.command_prefix}help"
        )
        await self.change_presence(activity=activity)
        print(f"Logged in as {self.user}")

Chopper().run(token)
