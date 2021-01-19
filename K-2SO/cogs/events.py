import os

import discord
from discord.ext.commands import Cog

from helpers.embeds import contact_owner


class Events(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            embed = discord.Embed(
                description=f"This bots default prefix is `{self.bot.command_prefix}`\n"
                f"Do `{self.bot.command_prefix}help` to see all available commands!", 
                color=self.bot.color
            )
            contact_owner(self.bot, embed)
            ctx = await self.bot.get_context(message)
            await ctx.send(embed=embed)

        elif message.channel == self.bot.get_channel(799690675713081415):
            me = self.bot.get_user(514403029898887201)
            dm = await me.create_dm()
            await dm.send("Pulling commits and restarting...")

            await self.bot.close()
            os.system("bash K-2SO/start.sh")