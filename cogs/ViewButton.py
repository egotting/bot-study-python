import discord
from discord.ext import commands

CATEGORY_NAME: str = 'ticket'


# Todas as views vao entrar aq
class ViewButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='✰ Click Aqui!', custom_id='button_ticket', style=discord.ButtonStyle.green)
    async def button_ticket(self, interact: discord.Interaction, button: discord.ui.Button):
        guild = interact.guild

        category = discord.utils.get(guild.categories, name=CATEGORY_NAME)

        if category:
            await guild.create_text_channel(name='test', category=category)
            await interact.response.send_message('O ticket foi criado olhe o chat Ticket')
        else:
            print('Error create channel')


class ViewCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def pix(self, ctx: commands.Context):
        my_embed = discord.Embed(title='Test', description='Test ao quadrado')  # start embed

        img = discord.File('src/ascii_icon.jpg', 'icon.jpg')  # img grande que fica no sentro
        my_embed.set_image(url="attachment://icon.jpg")

        thumb_file = discord.File('src/icon.jpg', 'icon_thumb.jpg')  # img icon que fican a esquerda
        my_embed.set_thumbnail(url="attachment://icon_thumb.jpg")
        my_embed.set_footer(text='final')  # o ultimo texto

        my_embed.color = discord.Color.light_gray()  # cor que fica do lado
        img_channel = discord.File('src/a68922bdf4b6850069ccae50b8532190.jpg',
                                   'img_channel.jpg')  # img icon que fican a esquerda
        my_embed.set_author(name='Test1', url='https://github.com/egotting',
                            icon_url='attachment://img_channel.jpg')  # pode por url
        my_embed.add_field(name="Test2", value=1,
                           inline=False)  # inline false serve pra deixar tudo em uma linha reta "fica melhor pra quem usar celualr"
        my_embed.add_field(name="Test3", value=123, inline=False)

        await ctx.reply(files=[img, thumb_file, img_channel], embed=my_embed)

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

        view = ViewButton()
        await ctx.send(files=[img], embed=embed)
        await ctx.send(view=view)

    # n funcioanndo resolver isso dps
    @commands.Cog.listener()
    async def on_text_channel_created(self, ctx: commands.Context):
        embed = discord.Embed(
            description='ཻ۪۪♡. **Obrigada pela preferência!**'
                        'Por favor, tire sua dúvida deixando já todos os detalhes e/ou diga qual produto deseja adquirir',
            color=discord.Color.dark_purple()
        )
        await ctx.reply(embed=embed)


async def setup(bot):
    bot.add_view(ViewButton())
    await bot.add_cog(ViewCog(bot))
