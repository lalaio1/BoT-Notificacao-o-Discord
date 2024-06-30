import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'[!] Bot está online :l')

@bot.command()
async def notificar(ctx, *, mensagem: str):
    if not ctx.author.guild_permissions.administrator:
        return await ctx.send('```[!] Você não tem permissão para usar este comando.```')

    log_channel_id = Coloca o ID aqui                # canal ID logs
    log_channel = bot.get_channel(log_channel_id)

    if not log_channel:
        return await ctx.send('```[!] Canal de logs não encontrado.```')

    github_link = "https://github.com/lalaio1/BoT-Notificacao-o-Discord"

    for member in ctx.guild.members:
        if not member.bot:
            try:
                status_color = {
                    discord.Status.online: discord.Color.green(),
                    discord.Status.idle: discord.Color.orange(),
                    discord.Status.dnd: discord.Color.red(),
                    discord.Status.offline: discord.Color.greyple()
                }

                embed = discord.Embed(
                    title="Notificação",
                    description=mensagem,
                    color=status_color.get(member.status, discord.Color.default())
                )
                embed.set_thumbnail(url=member.avatar.url)  

                status = member.status
                activity = member.activity
                if activity:
                    embed.add_field(name="Atividade", value=activity.name, inline=False)
                    if isinstance(activity, discord.Spotify):
                        embed.add_field(name="Artista", value=activity.artist, inline=False)
                        embed.set_thumbnail(url=activity.album_cover_url)
                    elif isinstance(activity, discord.Streaming):
                        embed.add_field(name="Transmitindo", value=activity.name, inline=False)
                        embed.set_thumbnail(url=activity.large_image_url)
                    elif isinstance(activity, discord.Game):
                        embed.add_field(name="Jogando", value=activity.name, inline=False)
                        if activity.small_image_url:
                            embed.set_thumbnail(url=activity.small_image_url)
                else:
                    embed.add_field(name="Atividade", value='Nenhuma', inline=False)

                embed.add_field(name="Usuário", value=member.mention, inline=False)
                embed.add_field(name="Hora da Notificação", value=f'{discord.utils.utcnow()}', inline=False)
                embed.add_field(name="Status", value=status, inline=False)
                
                embed.set_footer(text="GitHub do Bot", icon_url=bot.user.avatar.url)
                embed.url = github_link

                await member.send(mensagem)

                await log_channel.send(embed=embed)

            except discord.Forbidden:
                print(f'[!] Erro ao enviar mensagem para {member}')

    await ctx.send(f'```[!] Notificação enviada com sucesso para todos os membros não-bots:```\n```Fix\n{mensagem}```')
caminho_arquivo = 'AL/token.txt'
with open(caminho_arquivo, 'r') as arquivo:
    token = arquivo.read().strip()  

bot.run(f'{token}')
