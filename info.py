from interactions import *

class Info(Extension):
     
    @slash_command(name="info", description="Affiche les informations du bot")
    async def info(self, ctx : InteractionContext):
            try : 
                embed = Embed(title="Informations du bot", color=Color.from_hex("#FF0000"))
                embed.add_field(name="Développé en", value="Python, avec [interactions.py (v5)](https://github.com/interactions-py/interactions.py)", inline=True)
                embed.add_field(name="Créé le", value=f"{self.bot.app.created_at}", inline=False)
                embed.add_field(name="Créé par", value=f"<@{self.bot.owner.id}>", inline=False)
                embed.add_field(name="Serveurs", value=len(self.bot.guilds), inline=True)
                embed.add_field(name="Latence", value=f"{round(self.bot.latency * 100)} ms", inline=True)
                embed.set_footer(text=self.bot.app.name, icon_url=self.bot.user.avatar_url)
                await ctx.send(embed=embed)
            except OverflowError : 
                await ctx.send("La commande est indisponible pour le moment. Réessayes dans quelques minutes.", ephemeral=True)

def setup(bot):
    Info(bot)