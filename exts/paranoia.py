from interactions import *
from utils import *

class Paranoia(Extension):

    @cooldown(Buckets.GUILD, 1, 5)
    @slash_command(
        name="paranoia",
        description="Pose une question pour mettre mal à l'aise",
        nsfw=True,
        dm_permission=False
    )
    async def paranoia(self, ctx : InteractionContext):
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

def setup(bot):
    Paranoia(bot)