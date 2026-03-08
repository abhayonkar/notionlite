from apscheduler.schedulers.background import BackgroundScheduler
import notify2

scheduler = BackgroundScheduler()
scheduler.start()

notify2.init("Notecon")


def send_notification(title, message):

    n = notify2.Notification(title, message)
    n.show()


def schedule_task(title, time):

    scheduler.add_job(
        send_notification,
        'date',
        run_date=time,
        args=[title, "Task Deadline Reached"]
    )