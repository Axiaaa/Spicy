from interactions import *
from utils import *
import os, logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%H:%M:%S",
                    handlers=[
                        logging.FileHandler("bot.log"),
                        logging.StreamHandler()
                    ])

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

def load_extensions(bot, folder, folder_name="", exclude_files=[]):
    extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
    for ext in extensions:
        logging.debug(f"{ext} a été chargé !")
        bot.load_extension(f"{folder_name}{ext}")

bot = Client(token=os.environ['STOKEN'], intents=Intents.ALL)
load_extensions(bot, "exts", "exts.")
bot.start()

