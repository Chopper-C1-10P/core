import discord
import requests
from bots.reddit import reddit
from discord.ext.commands import Cog, command
from helpers.config import config
from helpers.embeds import requested_by


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(description="Sends a random subreddit picture.",
             usage="<subreddit>")
    async def reddit(self, ctx, subreddit):
        async with ctx.typing():
            index = 0
            while True:
                index += 1
                if index > 9:
                    embed = discord.Embed(
                        description="Couldn't find an image on this subreddit",
                        color=self.bot.color)
                    await ctx.send(embed=embed)

                    break

                post = reddit.subreddit(subreddit).random()
                if "i.redd.it" in post.url:
                    embed = discord.Embed(description=post.title,
                                          color=self.bot.color,
                                          timestamp=ctx.message.created_at)
                    embed.set_image(url=post.url)
                    requested_by(self.bot, ctx, embed)
                    await ctx.send(embed=embed)

                    break

    @command(description="Sends a random meme.")
    async def meme(self, ctx):
        async with ctx.typing():
            while True:
                post = reddit.subreddit("memes").random()
                if "i.redd.it" in post.url:
                    embed = discord.Embed(description=post.title,
                                          color=self.bot.color,
                                          timestamp=ctx.message.created_at)
                    embed.set_image(url=post.url)
                    requested_by(self.bot, ctx, embed)
                    await ctx.send(embed=embed)

                    break
