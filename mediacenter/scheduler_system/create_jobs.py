import mediacenter
from mediacenter import scheduler


def set_client(new_client):
    mediacenter.client = new_client


def add_job(function):
    scheduler.add_job(function, 'interval', seconds=3, args=[mediacenter.client])
