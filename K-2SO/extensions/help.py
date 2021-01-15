import discord
from discord.ext.commands import Cog, command

from helpers.embeds import contact_owner


class Help(Cog):
    def __init__(self, bot=None):
        self.bot = bot

    @command(aliases=["commands"], hidden=True)
    async def help(self, ctx):
       # def check(reaction, user):
           # return user == ctx.message.author and \
           #    str(reaction.emoji) in nemojis
           #
           # try:
           #      reaction, user = await self.bot.wait_for("reaction_add",
           #                                               timeout=60.0,
           #                                               check=check)
           # except asyncio.TimeoutError:
           #     await ctx.send("Took too long to react", delete_after=10)
           # else:
  
        embed = discord.Embed(
                title=f"{self.bot.user.name}'s commands",
            url="https://github.com/K-2SO-the-bot/core",
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
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/"
            "793282567000162354/797467065203949588/K-2SO_wide.png"
        )
        owner = self.bot.get_user(514403029898887201)
        contact_owner(self.bot, embed)
        await ctx.send(embed=embed)
