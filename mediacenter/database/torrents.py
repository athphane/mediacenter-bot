# TODO: Implement Database queries for qbittorrent notification system..
from mediacenter.database import database


class CompletedTorrents:
    def __init__(self):
        self.completed_torrents = database()['completed_torrents']

    def all_torrents(self):
        torrents = self.completed_torrents.find({}, {'_id': False})

        return torrents

    def all_torrents_by_category(self, category):
        torrents = self.completed_torrents.find(
            {
                'category': category
            },
            {'_id': False}
        )
        return torrents

    def to_be_notified(self):
        return self.completed_torrents.find(
            {
                'notified': False
            }
        )

    def mark_as_notified(self, torrent):
        query = {
            "_id": torrent['_id'],
        }

        data = {
            "notified": True
        }

        new_values = {"$set": data}

        self.completed_torrents.update_one(query, new_values)

