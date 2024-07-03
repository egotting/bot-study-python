## Slash Commands

usa ```interact: discord.Interaction``` como parametro e a tag ```bot.tree.command``` e ``` @app_commands.command()```
se usar cogs
ex:

```python
    @app_commands.command()
async def sum_cogs(self, interact: discord.Interaction, n1: float, n2: float):
    await interact.response.send_message(n1 + n2)
```

## Command padrão

- Usar o ```ctx: commands.Context``` como paramentro e a tag ```@bot.commands()``` em cima da funce usando cogs é
  assim ```@commands.command()``` ex:

```python
@bot.command()
async def talk(ctx: commands.Context, *, frase):
    await ctx.send(frase)
```

## Cogs

- Criar uma pasta com o nome que vc quiser e siga a estrutura a baixo

```python
from discord import app_commands
from discord.ext import commands


class(nome da classe)(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    # aqui aonde fica os comandos dentro da classe 
    @app_commands.command()
    async def sum_cogs(self, interact: discord.Interaction, n1: float, n2: float):
        await interact.response.send_message(n1 + n2)


# Aq que faz pra iniciar a cog
async def setup(bot):
    await bot.add_cog((nome da classe)(bot))
```

- Dentro do main coloca essa func pra percorrer o cogs e pega os arquivos

```python
# pegando a pasta cogs e os arquivos que tem la e trasendo pro main
async def carregar_cogs():
    for arquivo in os.listdir("cogs"):
        if arquivo.endswith('.py'):
            await bot.load_extension(
                f"cogs.{arquivo[:-3]}")  # ta pegando o arquivo e tirando os 3 ultimos caracteres pra n ter erro o .py
```

# Events
- Chamar a func dentro do on_ready pra carregar assim que starta

```python
@bot.event
async def on_ready():
    # serve pra sincronizar os slash cogs com o discord
    # recomendado n é por mais pra n precisar ficar syncando toda hr vou por aq
    await bot.tree.sync()
    await carregar_cogs()  # chamar no main a func de percorrer 
    print(f'bot esta online {bot.user}')
```

# Embed
```python 
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

```