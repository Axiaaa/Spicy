from interactions import *
from utils import *

class Dilemma(Extension):
        
    @cooldown(Buckets.GUILD, 1, 5)
    @slash_command(
        name="dilemme",
        description="Propose un dilemme sous forme de \"Tu preferes\"",
        nsfw=True,
        dm_permission=False  
    )
    async def wyr(self, ctx : InteractionContext):
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

def setup(bot):
    Dilemma(bot)