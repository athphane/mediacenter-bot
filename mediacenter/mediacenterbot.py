from configparser import ConfigParser
from pyrogram import Client


class MediaCenterBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        config_file = f"{name}.ini"

        config = ConfigParser()
        config.read(config_file)

        super().__init__(
            name,
            bot_token=config.get(name, "bot_token"),
            config_file=config_file,
            workers=16,
            plugins=dict(root="mediacenter/plugins"),
            workdir="../"
        )

    async def start(self):
        await super().start()
        print(f"{self.__class__.__name__} started. Hi.")

    async def stop(self):
        await super().stop()
        print(f"{self.__class__.__name__} stopped. Bye.")
