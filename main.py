import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# from Http import keep_alive

allowed = discord.Intents.default()
allowed.message_content = True  # consegue ler as mensagens
allowed.members = True  # Consegue ler os membros
allowed.dm_messages = True  # Consegue ler as mensagens na dm
allowed.guilds = True
command = commands.Bot(command_prefix='!', intents=allowed)

load_dotenv()
TOKEN = os.getenv("TOKEN")


# Serve pra synca os slash cogs criados
# @bot.command()
# async def sync(ctx: cogs.Context):
#     if ctx.author.id == 1032779381808046131:  # verificando a role de quem ta usando o slash command
#         # server = discord.Object(id=1228809942690041939) # serve pra dizer que server q eu quero que de sync
#         syncs = await bot.tree.sync()  # coloque dentro do parenteses guild=server # se for vai poder usar
#
#         await ctx.reply(f"{len(syncs)} comandos sincronizados")  # mostrando qauntos comandos foram sincronizados
#     else:
#         await ctx.reply("apenas o fudido do henrique pode usar essa porra")

# pegando a pasta cogs e os arquivos que tem la e trasendo pro main

# Não é bom colocar dentro do on_ready pq pode acabar batendo no limite de trafego do discord e pode dar mt bo ent faça manualmente

async def carregar_cogs():
    for arquivo in os.listdir("cogs"):
        if arquivo.endswith('.py'):
            await command.load_extension(
                f"cogs.{arquivo[:-3]}")  # ta pegando o arquivo e tirando os 3 ultimos caracteres pra n ter erro o .py


@command.event
async def on_ready():
    # serve pra sincronizar os slash cogs com o discord
    # recomendado n é por mais pra n precisar ficar syncando toda hr vou por aq
    await carregar_cogs()
    await command.tree.sync()
    print(f'bot esta online {command.user}')


# @commands.is_owner()
# async def reload(ctx: commands.Context, extension):
#     command.reload_extension(f"cogs.{extension}")
#     embed = discord.Embed(title='Reload', description=f'{extension} hot reload', color=0xff00c8)
#     await ctx.send(embed=embed)
#

# keep_alive()
command.run(TOKEN)
