from discord.ext.commands import check

def is_owner():
    def predicate(ctx):
        return ctx.message.author.id == 514403029898887201
    return check(predicate)
