# In this program, we shall check for a condition and calculate the difference in time from when
# that condition was last satisfied to current- if its currently satisfied.
import json
import sys
import time

prev_time = 0 #initialise value of previous time difference>0.01 as 0
while 1:
        prev_output = sys.stdin.readline()
        input = json.loads(prev_output)
        if input["difference in the ratio"]> 0.01: #check for the condition
                if prev_time == 0 : #if its 0, update and continue
                        prev_time = input["time"]
                        continue
                delta_time = input["time"] - prev_time #calculate difference between now and last time when difference>0.01
                print json.dumps({"difference in ratio":input["difference in the ratio"],"delta_time":delta_time,"actual ratio":input["actual ratio"],"time":input["time"]})
                sys.stdout.flush()#flush to stdout
                prev_time = input["time"]#update previous time this event occurred to current time.

