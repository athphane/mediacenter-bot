from mediacenter.mediacenterbot import MediaCenterBot


async def notify_torrent_complete(client: MediaCenterBot):
    # completed_torrents =
    await client.send_message(352665135, 'something')
