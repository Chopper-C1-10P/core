import discord

def contact_owner(bot, embed):
    owner = bot.get_user(514403029898887201)
    embed.set_footer(
        text=f"Please contact {owner} if you are having any issues",
        icon_url=owner.avatar_url
    )

def requested_by(bot, ctx, embed):
    embed.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.message.author.avatar_url
    )