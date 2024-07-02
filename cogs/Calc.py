import discord
from discord import app_commands
from discord.ext import commands


# Constructor
class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.describe(n1='O primeiro numero a ser somado', n2='Segundo numero a ser somado')
    @app_commands.command()
    async def sum(self, interact: discord.Interaction, n1: float, n2: float):
        await interact.response.send_message(n1 + n2)


# Aq que faz pra iniciar a cog
async def setup(bot):
    await bot.add_cog(Calc(bot))
