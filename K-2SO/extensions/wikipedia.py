import asyncio

import discord
from discord.ext.commands import Cog, command
from helpers.embeds import requested_by
from helpers.emojis import demojis, nemojis

import wikipedia


class Wikipedia(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(
        description="Searches on wikipedia and gives you a summary of that.",
        usage="<something>")
    async def wiki(self, ctx, *, thing: str):
        async with ctx.typing():
            results = wikipedia.search(thing, results=9)
            results = dict(enumerate(results, start=1))
            embed = discord.Embed(
                description=f"Please react with the desired article number:",
                color=self.bot.color,
                timestamp=ctx.message.created_at)
            for pair in results:
                embed.add_field(name=pair, value=results[pair])

            msg = await ctx.send(embed=embed)

            for emoji in nemojis:
                await msg.add_reaction(emoji)

            def check(reaction, user):
                return user == ctx.message.author and \
                    str(reaction.emoji) in nemojis

            try:
                reaction, user = await self.bot.wait_for("reaction_add",
                                                         timeout=60.0,
                                                         check=check)
            except asyncio.TimeoutError:
                await ctx.send("Took too long to react", delete_after=10)
            else:
                pageid = results[demojis[str(reaction.emoji)]]
                page = wikipedia.page(pageid, auto_suggest=False)

                embed = discord.Embed(description=wikipedia.summary(
                    pageid, sentences=4),
                                      color=self.bot.color,
                                      timestamp=ctx.message.created_at)
                embed.set_author(name=page.title, url=page.url)
                embed.set_thumbnail(url=page.images[0])
                requested_by(self.bot, ctx, embed)
                await ctx.send(embed=embed)
