import discord
from discord.ext.commands import Cog, command

from helpers.embeds import contact_owner


class Help(Cog):
    def __init__(self, bot=None):
        self.bot = bot

    @command(aliases=["commands"], hidden=True)
    async def help(self, ctx):
        embed = discord.Embed(
            title=f"{self.bot.user.name}'s commands",
            color=self.bot.color,
            timestamp=ctx.message.created_at
        )
        for command in self.bot.commands:
            if command.hidden is False:
                if command.usage is None:
                    embed.add_field(
                        name=f"`{self.bot.command_prefix}{command}`",
                        value=command.description
                    )
                else:
                    embed.add_field(
                        name=f"`{self.bot.command_prefix}{command} {command.usage}`",
                        value=command.description
                    )
        owner = self.bot.get_user(514403029898887201)
        contact_owner(self.bot, embed)
        await ctx.send(embed=embed)
