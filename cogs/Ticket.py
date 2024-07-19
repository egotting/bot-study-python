import discord
from discord.ext import commands

CATEGORY_HELP_TICKET: str = "ticket"
CATEGORY_CLOUTHS_TICKET: str = "Roupas"
CATEGORY_KITCHEN_TICKET: str = "Cozinha"
CATEGORY_ACTION_FIGURE_TICKET: str = "Action Figures"
CATEGORY_BOOKS_TICKET: str = "Livros"
stylebtn = discord.ButtonStyle


class ViewCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def ticket(self, ctx: commands.Context):
        embed = discord.Embed(
            title="ཻ۪۪♡. COMPRAS & SUPORTE",
            description="♡**Abra um ticket para**: \n"
            "• realizar uma compra \n"
            "• tirar alguma dúvida \n",
        )
        img = discord.File("src/kuromi_ticket_icon.png", "kuromi_ticket.png")
        embed.set_thumbnail(url="attachment://kuromi_ticket.png")
        embed.color = discord.Color.dark_purple()
        embed.set_footer(
            text='ᵖᵒʳ ᶠᵃᵛᵒʳ ⁿᵃ̃ᵒ ᵃᵇʳᵃ ᵘᵐ ᵗⁱᶜᵏᵉᵗ ˢᵉᵐ ᶜᵉʳᵗᵉᶻᵃ ᵈᵉ ᶜᵒᵐᵖʳᵃ ᵒᵘ ᵖᵃʳᵃ "ᵗᵉˢᵗᵃʳ"'
        )

        view = CreateTicket()
        await ctx.send(files=[img], embed=embed, view=view)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if isinstance(channel, discord.TextChannel):
            if channel.category and channel.category.name == CATEGORY_HELP_TICKET:
                img = discord.File(
                    "src/ticket_channel_created.jpg", "ticket_channel_created.jpg"
                )
                embed = discord.Embed(
                    description="ཻ۪۪♡. **Obrigada pela preferência!** \n"
                    "Por favor, tire sua dúvida deixando já todos os detalhes e/ou diga qual produto deseja adquirir \n",
                    color=discord.Color.dark_purple(),
                )
                view = DeleteChannelButton()
                await channel.send(files=[img], embed=embed, view=view)


# class que chama a view do button que cria ticket pros commands
class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ButtonTicket())
        self.add_item(SelectMenuInput())


# class que chama a view do button de fechar os tickets pros commands
class DeleteChannelButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(DeleteTicket())


class SelectMenuInput(discord.ui.Select):
    def __init__(self):
        opcoes = [
            discord.SelectOption(label="camisas", description="sla fds", value=1),
            discord.SelectOption(label="cozinha", description="sla fds", value=2),
            discord.SelectOption(
                label="action figures", description="sla fds", value=3
            ),
            discord.SelectOption(label="mangas", description="sla fds", value=4),
            discord.SelectOption(label="Ajuda", description="sla fds", value=5),
        ]
        super().__init__(placeholder="Escolha as opcoes", options=opcoes)

    async def callback(self, interaction: discord.Interaction):
        request = self.values[0]

        await interaction.response.send_message(request)


# Button que cria o ticket
class ButtonTicket(discord.ui.Button):
    def __init__(self):
        super().__init__(label="✰ Click Aqui!", style=stylebtn.success)

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user

        existing_channel = discord.utils.get(
            guild.text_channels, name=f"chat-{user.name.lower()}-{user.discriminator}"
        )
        if existing_channel:
            await interaction.response.send_message(
                "seu ticket ja foi criado", ephemeral=True
            )
            return
        category = discord.utils.get(guild.categories, name=CATEGORY_HELP_TICKET)
        if not category:
            await interaction.response.send_message(
                "seu ticket ja foi criado", ephemeral=True
            )
            return

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                read_messages=False, send_messages=False
            ),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        }

        channel = await guild.create_text_channel(
            f"chat-{user.name.lower()}-{user.discriminator}",
            overwrites=overwrites,
            category=category,
        )
        await interaction.response.send_message(
            f"Chat privado criado: {channel.mention}", ephemeral=True
        )


# Button que fecha o ticket
class DeleteTicket(discord.ui.Button):
    def __init__(self):
        super().__init__(label="✰ Fechar Ticket!", style=stylebtn.danger)

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild

        get_category = discord.utils.get(guild.categories, name=CATEGORY_HELP_TICKET)
        if not get_category:
            await interaction.response.send_mmesage(
                f"Categoria '{CATEGORY_NAME}' não encontrada.", ephemeral=True
            )
            return

        user = interaction.user.guild_permissions.administrator
        if user:
            try:
                channel = interaction.channel.delete()
                await channel
            except Exception as e:
                await interaction.response.send_message(f"N foi possivel exclui {e}")


async def setup(bot):
    await bot.add_cog(ViewCog(bot))
