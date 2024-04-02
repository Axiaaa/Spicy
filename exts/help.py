from interactions import *

class Help(Extension):


    @slash_command(
        name="help",
        description="Envoie une liste des commandes disponible"
    )
    async def help(self, ctx : InteractionContext):
        embed = Embed(
            title="Liste des mes commandes",
            description="Si vous voyez :underage: devant une commande, c'est qu'elle doit être éxécutée dans un salon NSFW",
        )
        embed.add_field(name="`/help`", value="Affiche cette liste", inline=False)
        embed.add_field(name="`/info`", value="Affiche certaines informations sur le bot", inline=False)
        embed.add_field(name="`/ping`", value="Ping le bot", inline=False)
        embed.add_field(name=":underage: `/verite`", value="Propose une vérité", inline=False)
        embed.add_field(name=":underage: `/action`", value="Propose un gage. Certaines actions marchent mieux si vous jouer avec vos amis autours de vous", inline=False)
        embed.add_field(name=":underage: `/dilemme`", value="Propose un dilemme", inline=False)
        embed.add_field(name=":underage: `/n_as_tu_jamais`", value="Propose une quesions sous forme de \"N'as tu jamais ...\" avec des réactions pour réagir", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    Help(bot)