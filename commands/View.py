import discord
import discord.ui
from discord.ext import commands


class View(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    async def table(self, ctx: commands.Context):
        async def select_reponse(interact: discord.Interaction):
            choose = interact.data['values'][0]
            cus = {'1': 'cu1', '2': 'cu1', '3': 'cu1', '4': 'cu1'}
            cu_choosed = cus[choose]
            await interact.response.send_message(f"Voce escolheu o {cu_choosed}")

        menu_select = discord.ui.Select(
            placeholder='Selecione uma opção')  # max_values é o quanto que o usuario vai poder selecionar
        opcoes = [
            discord.SelectOption(label='cu1', value='1'),
            discord.SelectOption(label='cu2', value='2'),
            discord.SelectOption(label='cu3', value='3'),
            discord.SelectOption(label='cu4', value='4'),
        ]
        menu_select.options = opcoes
        menu_select.callback = select_reponse
        view = discord.ui.View()
        view.add_item(menu_select)
        await ctx.send(
            view=view)  # ctx.send ele so escreve oq a função manda ctx.reply ele responde quem fez o comando marcando a pessoa

    async def button(self, ctx: commands.Context):
        async def response_button(interact: discord.Interaction):
            await interact.response.send_message('cu')  # ephemeral=True so a pessoa que clickou no botão ve
            await interact.followup.send('cu 2')  ## followup faz entender q é uma continuação da outra msg

        view = discord.ui.View()
        _button = discord.ui.Button(label='Botão', style=discord.ButtonStyle.green)
        _button.callback = response_button

        url_button = discord.ui.Button(label="url", url="https://github.com/egotting")

        view.add_item(_button)
        view.add_item(url_button)
        await ctx.reply(view=view)

    # slash commands, os commands padroes n precisam de tag dentro do cog
    async def pix(self, ctx: commands.Context):
        my_embed = discord.Embed(title='penes', description='penes ao quadrado')  # start embed

        img = discord.File('src/ascii_icon.jpg', 'icon.jpg')  # img grande que fica no sentro
        my_embed.set_image(url="attachment://icon.jpg")

        thumb_file = discord.File('src/icon.jpg', 'icon_thumb.jpg')  # img icon que fican a esquerda
        my_embed.set_thumbnail(url="attachment://icon_thumb.jpg")
        my_embed.set_footer(text='final')  # o ultimo texto

        my_embed.color = discord.Color.light_gray()  # cor que fica do lado
        img_channel = discord.File('src/a68922bdf4b6850069ccae50b8532190.jpg',
                                   'img_channel.jpg')  # img icon que fican a esquerda
        my_embed.set_author(name='fudido', url='https://github.com/egotting',
                            icon_url='attachment://img_channel.jpg')  # pode por url
        my_embed.add_field(name="Viado1", value=1,
                           inline=False)  # inline false serve pra deixar tudo em uma linha reta "fica melhor pra quem usar celualr"
        my_embed.add_field(name="Viado2", value=123, inline=False)

        await ctx.reply(files=[img, thumb_file, img_channel], embed=my_embed)


async def setup(bot):
    await bot.add_cog(View(bot))
