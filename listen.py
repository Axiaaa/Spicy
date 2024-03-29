from interactions import *

class Listen(Extension):

    @listen(events.Ready)
    async def on_ready(event) -> None :
        print("Je suis pret !")

    @listen(events.Startup)
    async def on_start(event) -> None:
        print("Je demarre !")

def setup(bot):
    Listen(bot)
