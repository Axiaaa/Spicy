from interactions import *
from utils import *

class WouldYouRather(Extension):
        
    @cooldown(Buckets.GUILD, 1, 5)
    @slash_command(
        name="n_as_tu_jamais",
        description="Propose une sous forme de \"N'as-tu jamais ...\"",
        nsfw=True,
        dm_permission=False
    )
    async def nhie(self, ctx : InteractionContext):
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

def setup(bot):
    WouldYouRather(bot)