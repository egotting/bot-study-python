import discord
from discord.ext import commands

CATEGORY_NAME: str = 'ticket'


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def reset(self, ctx: commands.Context):
        guild = ctx.guild
        category = discord.utils.get(guild.categories, name=CATEGORY_NAME)

        try:
            if category:
                for channel in guild.text_channels:
                    if channel.category == category:
                        await channel.delete()
                await ctx.send("Canal ticket limpo")
        except discord.HTTPException as e:
            await ctx.send(f"N foi encontrado nenhum canal {e}")


async def setup(bot):
    await bot.add_cog(CommandCog(bot))
