from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter import scheduler, ADMIN
from mediacenter.scheduler_system.create_jobs import add_job
import mediacenter


async def test_function(client: MediaCenterBot):
    await client.send_message(ADMIN, "something")


if __name__ == '__main__':
    app = MediaCenterBot()

    # Function to add all scheduled jobs to scheduler
    mediacenter.client = app

    add_job(test_function)

    # Start scheduled jobs
    scheduler.start()

    app.run()
