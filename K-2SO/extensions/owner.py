import os

import discord
from discord.ext.commands import Cog, command

from helpers.checks import is_owner


class Owner(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(description="Leaves the guild", hidden=True)
    @is_owner()
    async def leave(self, ctx):
        await ctx.guild.leave()

    @command(description="Restarts the bot", hidden=True)
    @is_owner()
    async def restart(self, ctx):
        await self.bot.close()
        os.system("bash K-2SO/start.sh")
