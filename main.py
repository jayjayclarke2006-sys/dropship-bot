from app.db import init_db
from app.scheduler import start_scheduler

if __name__ == "__main__":
    init_db()
    start_scheduler()
