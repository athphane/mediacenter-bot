import os
import re
import sys
import uuid
from configparser import ConfigParser
from typing import Union
from typing.io import BinaryIO

import psutil
import requests
from pyrogram import Client
from pyrogram import types
from pyrogram.errors import MessageNotModified
from pyrogram.raw.all import layer
from pyrogram.types import InputMediaPhoto, Message


class MediaCenterBot(Client):
    def __init__(self, version='0.0.0'):
        name = self.__class__.__name__.lower()
        config_file = f"{name}.ini"
        self.version = version

        config = ConfigParser()
        config.read(config_file)

        super().__init__(
            name,
            bot_token=config.get(name, "bot_token"),
            config_file=config_file,
            # workers=16,
            plugins=dict(root="mediacenter/plugins"),
            workdir="../"
        )

    def __str__(self):
        """
        String representation of the class object
        """
        return self.__class__.__name__

    async def start(self):
        """
        Start function
        """
        await super().start()
        me = await self.get_me()
        print(f"{self.__class__.__name__} v{self.version} (Layer {layer}) started on @{me.username}.\n"
              f"Lets start managing your media server!")

    async def stop(self, *args):
        """
        Stop function
        :param args:
        """
        await super().stop()
        print(f"{self.__class__.__name__} stopped. Bye.")

    async def restart(self, git_update=False, pip=False, *args):
        """
        Restart the bot for reals.
        :return:
        """
        await self.stop()

        try:
            c_p = psutil.Process(os.getpid())
            for handler in c_p.open_files() + c_p.connections():
                os.close(handler.fd)
        except Exception as c_e:
            print(c_e)

        if git_update:
            os.system('git pull')
        if pip:
            os.system('pip install -r requirements.txt')

        os.execl(sys.executable, sys.executable, '-m', self.__class__.__name__.lower())
        sys.exit()

    @staticmethod
    def save_link_to_file(link):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        # If is valid photo
        file_name = f'downloads/{uuid.uuid4()}.jpg'
        if re.match(regex, link) is not None:
            response = requests.get(link)
            file = open(file_name, 'wb')
            file.write(response.content)
            file.close()

        return file_name

    async def send_photo(
            self,
            chat_id: Union[int, str],
            photo: Union[str, BinaryIO],
            file_ref: str = None,
            caption: str = "",
            parse_mode: Union[str, None] = object,
            ttl_seconds: int = None,
            disable_notification: bool = None,
            reply_to_message_id: int = None,
            schedule_date: int = None,
            reply_markup: Union[
                "types.InlineKeyboardMarkup",
                "types.ReplyKeyboardMarkup",
                "types.ReplyKeyboardRemove",
                "types.ForceReply"
            ] = None,
            progress: callable = None,
            progress_args: tuple = ()
    ) -> Union["types.Message", None]:
        """
        Send photo function that downloads the photo before it sends the photo.
        :return: types.Message or None
        """
        photo = self.save_link_to_file(photo)

        msg = await super().send_photo(chat_id, photo, file_ref=file_ref, parse_mode=parse_mode,
                                       ttl_seconds=ttl_seconds,
                                       caption=caption, disable_notification=disable_notification,
                                       reply_to_message_id=reply_to_message_id,
                                       schedule_date=schedule_date, reply_markup=reply_markup, progress=progress,
                                       progress_args=progress_args)

        try:
            os.remove(photo)
        except:
            print("Error removing file")
        finally:
            return msg

    async def edit_message_photo(
            self,
            message: Message,
            media: str,
    ) -> "types.Message":
        """
        Edit photo function that downloads the photo before photo gets edited.
        :return: types.Message
        """
        media = self.save_link_to_file(media)

        msg = types.Message
        try:
            msg = await super().edit_message_media(
                message.chat.id,
                message.message_id,
                InputMediaPhoto(media, caption=message.caption),
                reply_markup=message.reply_markup,
            )
        except MessageNotModified:
            pass

        try:
            os.remove(media)
        except:
            print("Error removing file")

        return msg
