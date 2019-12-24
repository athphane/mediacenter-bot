from mediacenter.database.torrents import CompletedTorrents
from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter.scheduler_system.create_jobs import add_job


async def notify_torrent_complete(client: MediaCenterBot):
    for torrent in CompletedTorrents().to_be_notified():
        print(torrent)

        # client.send_message()

    # await client.send_message(352665135, "hi")

#
# add_job(
#     notify_torrent_complete,
#     seconds=3
# )
