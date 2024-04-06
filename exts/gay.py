from interactions import *
import random, asyncio

class Gay(Extension) : 

    @cooldown(Buckets.GUILD, 1, 5)
    @slash_command(
        name="gay",
        description="Nous avons tous des voisins mais les connnaissons nous vraiment ?",
    )
    async def gay(self, ctx : InteractionContext):
        msg = await ctx.send(embed=Embed(title="Je réfléchis avant de donner mon verdict...", color="#cb1249"),)
        await asyncio.sleep(3)
        await msg.edit(embed=Embed(title=f":rainbow_flag: Tu es {random.randint(0, 100)}% gay !", color="#cb1249"),)

def setup(bot):
    Gay(bot)