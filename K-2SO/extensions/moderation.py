import discord
from discord.ext.commands import Cog, command, guild_only, has_permissions


class Moderation(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=["purge", "delete", "wipe"],
             description="Clears the given amount of messages",
             usage="<amount>",
             hidden=True)
    @guild_only()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        async with ctx.typing():
            embed = discord.Embed(description=f"Deleted {amount} messages!",
                                  color=self.bot.color,
                                  hidden=True)
            await ctx.send(embed=embed)
            await ctx.channel.purge(limit=amount + 2)
