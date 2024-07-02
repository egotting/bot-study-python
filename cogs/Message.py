import discord
from discord import app_commands
from discord.ext import commands


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # EVENT
    @commands.Cog.listener()
    async def on_guild_channel_create(self,
                                      channel: discord.abc.GuildChannel):  # Esse evento serve pra aparecer algo quando criar um novo canal
        await channel.send(f"novo canal")

    # @commands.Cog.listener()
    # async def on_message(self, msg: discord.Message):
    #     await self.bot.process_commands(msg)
    #     author = msg.author
    #     if author.bot:
    #         return  # Se for um bot vai parar a aplicação
    #     # await msg.reply("test")

    # COMMANDS
    @commands.command()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(1228809943428370676)
        await channel.send(f"{member.display_name} Entrou\n bons estudos")

    @commands.command()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(1228809943428370676)
        await channel.send(f"{member.display_name} tchau")

    # SLASH COMMANDS
    @app_commands.command()
    async def test(self, interact: discord.Interaction):
        await interact.response.send_message(f"iai, {interact.user.name} ")
        await interact.followup.send("test123")

    @app_commands.command()
    async def talk(self, interact: discord.Interaction, phrase: str):
        await interact.response.send_message(phrase)

    @app_commands.command()
    async def send_messages(self, interact: discord.Interaction, channel: discord.TextChannel):
        await interact.response.send_message(channel.name)


async def setup(bot):
    await bot.add_cog(Message(bot))
