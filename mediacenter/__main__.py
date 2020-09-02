from mediacenter import MediaCenterBot
from mediacenter import scheduler
import mediacenter

if __name__ == '__main__':
    app = MediaCenterBot

    # Assign app to variable in __init__
    mediacenter.client = app

    scheduler.start()
    app.run()
