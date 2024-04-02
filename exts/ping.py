
from interactions import *

class Ping(Extension):


    @slash_command(
        name="ping",
        description="Ping le bot",
    )
    async def ping(self, ctx : InteractionContext):
        await ctx.respond(f":ping_pong: Pong en {round(self.bot.latency * 100)} ms !", ephemeral=True)



def setup(bot):
    Ping(bot)