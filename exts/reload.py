import os, logging
from interactions import *

class Reload(Extension): 

    is_owner()
    @slash_command(
            name="reload", 
            description="Cette commande permet de recharger les extensions du bot."
            )
    async def reload(self, ctx : InteractionContext):
        def reload_extensions(bot, folder, prefix="", exclude_files=[]):
            extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
            for ext in extensions:
                logging.info(f"{ext} a été rechargé !")
                bot.reload_extension(f"{prefix}{ext}")
        reload_extensions(self.bot, "exts", "exts.")
        await ctx.respond(content="Fait !", ephemeral=True)

def setup(bot): 
    Reload(bot)