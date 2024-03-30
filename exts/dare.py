from interactions import *
from utils import *

class Action(Extension):

    @cooldown(Buckets.GUILD, 1, 5)
    @slash_command(
        name="action",
        description="Propose une action",
        nsfw=True,
        dm_permission=False  
    )
    async def dare(self, ctx : InteractionContext):
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
                embed.description = f"{r['question']}\n:warning: Cette question n'a pas pu être traduite."
            await ctx.send(embed=embed)

def setup(bot):
    Action(bot)