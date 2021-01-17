import asyncio

import discord
import ipinfo
import requests
from discord.ext.commands import Cog, command, guild_only

from helpers.config import config
from helpers.embeds import requested_by


class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(
        description="Get info about a user",
        usage="<member>"
    )
    @guild_only()
    async def whois(self, ctx, member: discord.Member=None):
        async with ctx.typing():
            if not member:
                member = ctx.message.author

            roles = [role for role in member.roles[1:]]

            embed = discord.Embed(
                color=self.bot.color,
                timestamp=ctx.message.created_at,
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(
                name=member,
                url=f"https://discord.com/users/{member.id}"
            )
            if member.name != member.display_name:
                embed.add_field(
                    name="Nickname:",
                    value=member.display_name,
                    inline=False
                )
            embed.add_field(
                name="Account created:",
                value=member.created_at.strftime("%Y-%m-%d, %H:%M:%S"),
                inline=False
            )
            embed.add_field(
                name="Joined this server:",
                value=member.joined_at.strftime("%Y-%m-%d, %H:%M:%S"),
                inline=False
            )
            embed.add_field(
                name="Roles:",
                value=", ".join([role.mention for role in roles]),
                inline=False
            )
            embed.add_field(
                name="ID:",
                value=member.id,
                inline=False
            )
            requested_by(self.bot, ctx, embed)
            await ctx.send(embed=embed)

    @command(
        description="Gives you covid-19 statistics for the world or a given country.",
        usage="<country>"
    )
    async def covid(self, ctx, *, country=None):
        async with ctx.typing():
            url = "https://api.covid19api.com/summary"

            response = requests.get(url)
            response = response.json()

            if response["Message"] == "":
                if country is None:
                    embed = discord.Embed(
                        title="Global covid-19 statistics",
                        color=self.bot.color,
                        timestamp=ctx.message.created_at
                    )
                    embed.add_field(
                        name="Total confirmed cases:",
                        value=response["Global"]["TotalConfirmed"]
                    )
                    embed.add_field(
                        name="Total deaths:",
                        value=response["Global"]["TotalDeaths"]
                    )
                    embed.add_field(
                        name="Total recovered:",
                        value=response["Global"]["TotalRecovered"]
                    )
                    embed.set_footer(
                        text=f"Requested by {ctx.author}",
                        icon_url=ctx.message.author.avatar_url
                    )
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title=f"Covid-19 statistics for {country}",
                        color=self.bot.color,
                        timestamp=ctx.message.created_at
                    )

                    for dictionary in response["Countries"]:
                        if dictionary["Country"] == country or \
                        dictionary["CountryCode"] == country or \
                        dictionary["Slug"] == country:

                            embed.add_field(
                                name="Total confirmed cases:",
                                value=dictionary["NewConfirmed"]
                            )
                            embed.add_field(
                                name="Total deaths:",
                                value=dictionary["TotalDeaths"]
                            )
                            embed.add_field(
                                name="Total recovered:",
                                value=dictionary["TotalRecovered"]
                            )
                            requested_by(self.bot, ctx, embed)
                            await ctx.send(embed=embed)

            else:
                await ctx.send(f"API error: {response['Message']}")

    @command(
        aliases=["ip"],
        description="Get info on the specified IP adress.",
        usage="<ip>"
    )
    async def ipinfo(self, ctx, ip):
        token = config("config.json", "ipinfo_access_token")
        handler = ipinfo.getHandler(token)
        ip = handler.getDetails(ip)

        embed = discord.Embed(
            title=f"Information on the ip adress: {ip.ip}",
            color=self.bot.color,
            timestamp=ctx.message.created_at
        )
        embed.add_field(
            name="**Country:**",
            value=f":flag_{ip.country.lower()}: {ip.country_name}"
        )
        embed.add_field(name="**City:**", value=ip.city)
        embed.add_field(
            name="**Approximate coordinates:**",
            value=f"[{ip.latitude}, {ip.longitude}]"
            "(https://www.google.com/maps/@{ip.latitude},{ip.longitude},18z)"
        )
        requested_by(self.bot, ctx, embed)
        await ctx.send(embed=embed)
