from mediacenter.mediacenterbot import MediaCenterBot
from mediacenter import scheduler, ALLOWED_USERS
from mediacenter.scheduler_system.create_jobs import set_client, add_job
import mediacenter


async def test_function(client: MediaCenterBot):
    await client.send_message(ALLOWED_USERS, "something")


if __name__ == '__main__':
    app = MediaCenterBot()

    # Function to add all scheduled jobs to scheduler
    mediacenter.client = app

    add_job(test_function)

    # Start scheduled jobs
    scheduler.start()

    app.run()
