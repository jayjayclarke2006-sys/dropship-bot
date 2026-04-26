import schedule
import time
from app.config import settings
from app.jobs import run_all_jobs

def start_scheduler():
    print("Starting automation scheduler...")
    run_all_jobs()

    schedule.every(settings.check_interval_minutes).minutes.do(run_all_jobs)

    while True:
        schedule.run_pending()
        time.sleep(5)
