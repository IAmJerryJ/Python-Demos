# Runde Jia
# Sydeney
# 2021/11/24 1:11
import schedule
import time


def job():
    print('haha---')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)