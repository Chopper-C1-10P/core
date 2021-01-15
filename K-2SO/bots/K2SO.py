from discord import Intents
from discord.ext.commands import Bot


class K2SO(Bot):
    def __init__(self, prefix):
        super().__init__(
            command_prefix=prefix,
            intents=Intents.all()
        )
        self.remove_command("help")
        self.color = 0x11101e
