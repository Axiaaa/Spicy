from interactions import *
from requests import get
import os

FOOTER_TEXT = "La question peut parfois être en anglais ou mal traduite, désolé pour la gêne occasionée !"

async def api_request(str, ctx : InteractionContext):
    try:
        r = get("https://api.truthordarebot.xyz/v1/" + str, params="rating=R")
        if r.status_code == 200:
            return r.json()
        else :
            await ctx.send(f"Erreur avec la requete API", ephemeral=True)
    except Exception as e:
        await ctx.send(f"Erreur ! {e}", ephemeral=True)

@listen(events.Ready)
async def on_ready(event) -> None :
    print("Je suis pret !")

@listen(events.Startup)
async def on_start(event) -> None:
    print("Je demarre !")

#TODO Handle Multiple choices questions
@cooldown(Buckets.GUILD, 1, 5)
@slash_command(
    name="verite",
    description="Propose une vérité",
    nsfw=True,
    dm_permission=False, 
)
async def truth(ctx : InteractionContext) :
    r = await api_request("truth", ctx)
    if (r): 
        embed = Embed(
            title="Vérité",
            color= (237, 127, 16),
            footer=EmbedFooter(FOOTER_TEXT),
            author=EmbedAuthor(ctx.author.display_name, icon_url=ctx.author.avatar_url)
        )
        if (r['translations']['fr']):
            embed.description = r['translations']['fr']
            embed.add_field(name="Anglais", value=r['question'], inline=False)
        else :
            embed.description = f"{r['question']}\n:warning: Cette question n'a pas pu être traduite.";
        await ctx.send(embed=embed)

@cooldown(Buckets.GUILD, 1, 5)
@slash_command(
    name="action",
    description="Propose une action",
    nsfw=True,
    dm_permission=False  
)
async def dare(ctx : InteractionContext):
    r = await api_request("dare", ctx)
    if (r):
        embed = Embed(
            title="Action",
            color=(127, 16, 237),
            footer=EmbedFooter(FOOTER_TEXT),
            author=EmbedAuthor(ctx.author.display_name, icon_url=ctx.author.avatar_url)  
        )
        if (r['translations']['fr']):
            embed.description = r['translations']['fr']
            embed.add_field(name="Anglais", value=r['question'], inline=False)
        else :
            embed.description = f"{r['question']}\n:warning: Cette question n'a pas pu être traduite.";
        await ctx.send(embed=embed)

@cooldown(Buckets.GUILD, 1, 5)
@slash_command(
    name="dilemme",
    description="Propose un dilemme sous forme de \"Tu preferes\"",
    nsfw=True,
    dm_permission=False
    
)
async def wyr(ctx : InteractionContext):
    r = await api_request("wyr", ctx)
    if (r):
        embed = Embed(
            title="Tu péfères ?",
            color=(255, 255, 0),
            footer=EmbedFooter(FOOTER_TEXT),
            author=EmbedAuthor(ctx.author.display_name, icon_url=ctx.author.avatar_url)  
        )
        if (r['translations']['fr']):
            embed.description = r['translations']['fr']
            embed.add_field(name="Anglais", value=r['question'], inline=False)
        else :
            embed.description = f"{r['question']}\n:warning: Ce dilemme n'a pas pu être traduit.";
        await ctx.send(embed=embed)

@cooldown(Buckets.GUILD, 1, 5)
@slash_command(
    name="n_as_tu_jamais",
    description="Propose une sous forme de \"N'as-tu jamais ...\"",
    nsfw=True,
    dm_permission=False
)
async def nhie(ctx : InteractionContext):
    r = await api_request("nhie", ctx)
    if (r):
        embed = Embed(
            title="N'as-tu jamais ?",
            color=(255, 0, 0),
            footer=EmbedFooter(FOOTER_TEXT),
            author=EmbedAuthor(ctx.author.display_name, icon_url=ctx.author.avatar_url)  
        )
        if (r['translations']['fr']):
            embed.description = r['translations']['fr']
            embed.add_field(name="Anglais", value=r['question'], inline=False)
        else :
            embed.description = f"{r['question']}\n:warning: Cette question n'a pas pu être traduite.";
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(":white_check_mark:")
        await msg.add_reaction(":x:")

@cooldown(Buckets.GUILD, 1, 5)
@slash_command(
    name="paranoia",
    description="Pose une question pour mettre mal à l'aise",
    nsfw=True,
    dm_permission=False
)
async def paranoia(ctx : InteractionContext):
    r = await api_request("paranoia", ctx)
    if (r):
        embed = Embed(
            title="Paranoia",
            color=(255, 0, 255),
            footer=EmbedFooter(FOOTER_TEXT),
            author=EmbedAuthor(ctx.author.display_name, icon_url=ctx.author.avatar_url)  
        )
        if (r['translations']['fr']):
            embed.description = r['translations']['fr']
            embed.add_field(name="Anglais", value=r['question'], inline=False)
        else :
            embed.description = f"{r['question']}\n:warning: Cette question n'a pas pu être traduite.";
        await ctx.send(embed=embed)


@slash_command(name="info", description="Affiche les informations du bot")
async def info(ctx : InteractionContext):
        try : 
            embed = Embed(title="Informations du bot", color=Color.from_hex("#FF0000"))
            embed.add_field(name="Développé en", value="Python, avec [interactions.py (v5)](https://github.com/interactions-py/interactions.py)", inline=True)
            embed.add_field(name="Créé le", value=f"{bot.app.created_at}", inline=False)
            embed.add_field(name="Créé par", value=f"<@{bot.owner.id}>", inline=False)
            embed.add_field(name="Serveurs", value=len(bot.guilds), inline=True)
            embed.add_field(name="Latence", value=f"{round(bot.latency * 100)} ms", inline=True)
            embed.set_footer(text=bot.app.name, icon_url=bot.user.avatar_url)
            await ctx.send(embed=embed)
        except OverflowError : 
            await ctx.send("La commande est indisponible pour le moment. Réessayes dans quelques minutes.", ephemeral=True)

@listen(disable_default_listeners=True)
async def on_command_error(event: errors):
    if isinstance(event.error, errors.CommandOnCooldown):
        temps_restant = round(event.error.cooldown.get_cooldown_time())
        await event.ctx.send(
            f"La commande est sous cooldown ! Réessayes dans {temps_restant} secondes",
            ephemeral=True,
        )
    else:
        await bot.on_command_error(bot, event)

bot = Client(token=os.environ['STOKEN'], intents=Intents.ALL)
bot.start()

