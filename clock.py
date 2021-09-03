from apscheduler.schedulers.blocking import BlockingScheduler
import main 
sched = BlockingScheduler()

@sched.main('interval', minutes=45)
def timed_job():
    print('This job is run every forty five minutes.')

sched.start()