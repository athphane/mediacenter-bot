# """
# Experimental file
# """
#
# if __name__ == '__main__':
#     print(None)
#
#
# import time
# import logging
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from pyrogram import Client, Filters
#
# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)
#
# scheduler = AsyncIOScheduler()
# scheduler.start()
# job_id = None
# @Client.on_message(Filters.command("schedule_start"))
# async def schedule_handler(client, message):
#     global scheduler, job_id
#     job = scheduler.add_job(task, "interval", seconds=30, args=[client, message.chat.id])
#     job_id = job.id
#     await message.reply(f"Schedule added:\nJob_id:{job_id}")
#
#
# @Client.on_message(Filters.command("stop_job"))
# async def schedule_stop_handler(client, message):
#     global scheduler
#     if len(message.text.split()) == 2:
#         stop_job_id = message.text.split()[1]
#         scheduler.remove_job(f'{stop_job_id}')
#
#         await message.reply("The job has been stopped")
#
#
# async def task(client, chat_id):
#     await client.send_message(chat_id, f"schedule_message sent at: <b>{time.ctime(time.time())}</b>")


"""This is the Welcome Bot in @PyrogramChat.

It uses the Emoji module to easily add emojis in your text messages and Filters
to make it only work for specific messages in a specific chat.
"""

from pyrogram import Client, Message, Filters


app = Client(
    "my_account",
    api_id = 882795,
    api_hash = "015e55ee3053d899bfaf945544f48e95",
    bot_token = "756448342:AAHbIhFkRoDfE3L667F4PValFe47xSsSgUc",
)


# Filter in only new_chat_members updates generated in TARGET chat
@app.on_message(Filters.command('log'))
async def welcome(client, message: Message):
    await app.send_document(chat_id=message.chat.id, document='mediacenter.log')


app.run()  # Automatically start() and idle()
