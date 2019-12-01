import mediacenter
from mediacenter import scheduler


def set_client(new_client):
    print(mediacenter.client)
    mediacenter.client = new_client
    print("from the setter")
    print(mediacenter.client)


def add_job(function):
    scheduler.add_job(function, 'interval', seconds=3, args=[mediacenter.client])
