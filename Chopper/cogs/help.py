import asyncio

import discord
from discord.ext.commands import Cog, command

from helpers.embeds import contact_owner, requested_by
from helpers.emojis import hemojis


class Help(Cog):
    def __init__(self, bot=None):
        self.bot = bot

    @command(aliases=["commands"], hidden=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Commands", color=self.bot.color)
        for command in self.bot.commands:
            if not command.hidden:
                if not command.usage:
                    embed.add_field(
                        name=f"`{self.bot.command_prefix}{command}`", 
                        value=command.description,
                        inline=False
                    )
                else:
                    embed.add_field(
                        name=f"`{self.bot.command_prefix}{command} {command.usage}`", 
                        value=command.description,
                        inline=False
                    )
        await ctx.send(embed=embed)