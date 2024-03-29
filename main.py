from interactions import *
from utils import *
import os

@listen(disable_default_listeners=True)
async def on_command_error(event: errors):
    if isinstance(event.error, errors.CommandOnCooldown):
        temps_restant = round(event.error.cooldown.get_cooldown_time())
        await event.ctx.send(
            f"La commande est sous cooldown ! Réessayes dans {temps_restant} secondes",
            ephemeral=True,
        )
    else:
        await bot.on_command_error(bot, event)

bot = Client(token=os.environ['STOKEN'], intents=Intents.ALL)
bot.load_extension("dare")
bot.load_extension("paranoia")
bot.load_extension("wyr")
bot.load_extension("dilemma")
bot.load_extension("verity")
bot.load_extension("info")
bot.load_extension("listen")
bot.start()

