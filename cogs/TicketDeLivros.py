import discord
from discord.ext import commands


class TicketDeLivros(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()


async def setup(bot):
    await bot.add_cog(TicketDeLivros(bot))
