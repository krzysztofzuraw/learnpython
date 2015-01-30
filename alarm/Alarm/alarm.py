"""
Alarm Clock - A simple clock where it plays a sound after X number of 
minutes/seconds or at a particular time.
"""

import datetime
import sys
import time

def alarm(hours, minutes, seconds):
    now = datetime.datetime.now()
    alarm_time = now.replace(hour=hours, minute=minutes, second=seconds)
    if alarm_time < now:
        print ("Wrong time, set time after {0}".format(now))
        return
    delta = alarm_time - now
    for i in reversed(range(int(delta.total_seconds()))):
        time.sleep(1)
        m, s = divmod(i, 60)
        h, m = divmod(m, 60)
        print ('Alarm in {0:.0f}h:{1:.0f}m:{2}s \r'.format(h,m,s), end='')
    print ("\nEnd of time")
          
    
if __name__ == ("__main__"):
    h = int(input("Give hours >> "))
    m = int(input("Give minutes >> "))
    s = int(input("Give seconds >> "))
    print ("Alarm set to {0}h:{1}m:{2}s".format(h,m,s))
    alarm(h, m, s)
