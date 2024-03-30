from interactions import *

class Help(Extension):


    @slash_command(
        name="help",
        description="Envoie une liste des commandes disponible"
    )
    async def help(self, ctx : InteractionContext):
        embed = Embed(
            None
        )
        await ctx.send(embed=embed)

def setup(bot):
    Help(bot)