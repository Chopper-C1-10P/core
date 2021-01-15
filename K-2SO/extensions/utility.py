from datetime import datetime
from random import randint

import discord
from discord.ext.commands import Cog, command, has_permissions, guild_only

from helpers.embeds import requested_by

class Utility(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(description=f"Invite the bot to your server")
    async def invite(self, ctx):
        async with ctx.typing():
            embed = discord.Embed(
                color=self.bot.color,
                timestamp=ctx.message.created_at
            )
            embed.set_author(
                name=f"Invite {self.bot.user.name} to your server",
                url="https://discord.com/api/oauth2/authorize?"
                "client_id=760913295644295176&permissions=8&scope=bot"
            )
            requested_by(self.bot, ctx, embed)
            await ctx.send(embed=embed)

    @command(
        description="DM a user",
        usage="<member> <message>",
        hidden=True
    )
    @has_permissions(manage_messages=True)
    async def dm(self, ctx, member: discord.Member, *, message):
        dm = await member.create_dm()
        await dm.send(message)

    @command(description="Check the bots latency")
    async def ping(self, ctx):
        await ctx.send(f"Responded in {round(self.bot.latency, 6)} seconds!")

    @command(
        description="Random color or the given color",
        usage="<hexcolor>"
    )
    async def color(self, ctx, hexcolor=None):
        embed = discord.Embed(
            color=self.bot.color,
            timestamp=ctx.message.created_at
        )
        if not hexcolor:
            randcolor = hex(randint(1118481, 16777215))
            randhex = randcolor[2:]
            embed.set_image(url=f"https://singlecolorimage.com/get/{randhex}/400x400")
            requested_by(self.bot, ctx, embed)
            embed.set_author(name=f"#{randhex}")
        else:
            embed.set_image(url=f"https://singlecolorimage.com/get/{int(hexcolor)}/400x400")
        await ctx.send(embed=embed)

    @command(
            description="Get the avatar from a user",
            usage="<member>"
        )
    @guild_only()
    async def avatar(self, ctx, member: discord.Member=None):
        async with ctx.typing():
            if not member:
                member = ctx.message.author

            embed = discord.Embed(
                color=member.color,
                timestamp=ctx.message.created_at,
            )
            embed.set_image(url=member.avatar_url)
            requested_by(self.bot, ctx, embed)
            await ctx.send(embed=embed)