from interactions import *
from utils import *

class Verity(Extension):

    #TODO Handle Multiple choices questions
    @cooldown(Buckets.GUILD, 1, 5)
    @slash_command(
        name="verite",
        description="Propose une vérité",
        nsfw=True,
        dm_permission=False, 
    )
    async def truth(self, ctx : InteractionContext) :
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

def setup(bot):
    Verity(bot)