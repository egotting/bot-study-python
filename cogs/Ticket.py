
import discord
from discord.ext import commands

CATEGORY_NAME: str = 'ticket'
stylebtn = discord.ButtonStyle


class ButtonDeleteChannel(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Close", style=stylebtn.danger)

    async def callback(self, interact: discord.Interaction):

        try:
            await interact.channel.delete()
        except discord.HTTPException as e:
            await interact.response.send_message(f"Ocorreu um erro ao fechar o ticket: {e}", ephemeral=True)


class ButtonTicket(discord.ui.Button):
    def __init__(self):
        super().__init__(label='✰ Click Aqui!', style=stylebtn.success)

    async def callback(self, interact: discord.Interaction):

        guild = interact.guild
        category = discord.utils.get(guild.categories, name=CATEGORY_NAME)

        if category:
            await guild.create_text_channel(name='test', category=category)
            await interact.response.send_message('O ticket foi criado olhe o chat Ticket', ephemeral=True)
        else:
            await interact.response.send_message(f"Não foi possivel criar um novo ticket", ephemeral=True)


# Todas as views vao entrar aq
class CreateChannelButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ButtonTicket())


class DeleteChannelButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ButtonDeleteChannel())


class ViewCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # n funcioanndo resolver isso dps
    @commands.command()
    async def ticket(self, ctx: commands.Context):
        embed = discord.Embed(title='ཻ۪۪♡. COMPRAS & SUPORTE',
                              description='♡**Abra um ticket para**: \n'
                                          '• realizar uma compra \n'
                                          '• tirar alguma dúvida \n',
                              )
        img = discord.File('src/kuromi_ticket_icon.png', 'kuromi_ticket.png')
        embed.set_thumbnail(url='attachment://kuromi_ticket.png')
        embed.color = discord.Color.dark_purple()
        embed.set_footer(text='ᵖᵒʳ ᶠᵃᵛᵒʳ ⁿᵃ̃ᵒ ᵃᵇʳᵃ ᵘᵐ ᵗⁱᶜᵏᵉᵗ ˢᵉᵐ ᶜᵉʳᵗᵉᶻᵃ ᵈᵉ ᶜᵒᵐᵖʳᵃ ᵒᵘ ᵖᵃʳᵃ "ᵗᵉˢᵗᵃʳ"')
        view = CreateChannelButton()

        await ctx.send(files=[img], embed=embed, view=view)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if isinstance(channel, discord.TextChannel):
            if channel.category and channel.category.name == CATEGORY_NAME:
                img = discord.File('src/ticket_channel_created.jpg', 'ticket_channel_created.jpg')
                embed = discord.Embed(
                    description='ཻ۪۪♡. **Obrigada pela preferência!** \n'
                                'Por favor, tire sua dúvida deixando já todos os detalhes e/ou diga qual produto deseja adquirir \n',
                    color=discord.Color.dark_purple()
                )
                view = DeleteChannelButton()
                await channel.send(files=[img], embed=embed, view=view)



async def setup(bot):
    await bot.add_cog(ViewCog(bot))
