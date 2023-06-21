import datetime
import time

while True:
    x = datetime.datetime.now()
    now=(x.strftime("%I:%M:%S"))
    print(now)
    time.sleep(1)
