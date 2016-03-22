from linbot import updateStatus
from rq import Queue
from worker import conn

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    q = Queue(connection=conn)
    result = q.enqueue(updateStatus)

sched.start()