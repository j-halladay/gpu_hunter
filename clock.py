from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=45)
def timed_job():
    print('This job is run every forty five minutes.')

sched.start()