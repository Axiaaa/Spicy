from interactions import InteractionContext
from requests import get

FOOTER_TEXT = "La question peut parfois être en anglais ou mal traduite, désolé pour la gêne occasionée !"

async def api_request(str, ctx : InteractionContext):
    try:
        r = get("https://api.truthordarebot.xyz/v1/" + str, params="rating=R")
        if r.status_code == 200:
            return r.json()
        else :
            await ctx.send(f"Erreur avec la requete API. ``Code : {r.status_code}", ephemeral=True)
    except Exception as e:
        await ctx.send(f"Erreur ! {e}", ephemeral=True)
