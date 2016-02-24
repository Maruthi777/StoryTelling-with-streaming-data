import json
import sys
import time

prev_time = 0
while 1:
        prev = sys.stdin.readline()
        input = json.loads(prev)
        if input["difference in the ratio"]> 0.01:
                if prev_time == 0 :
                        prev_time = input["time"]
                        continue
                delta_time = input["time"] - prev_time
                print json.dumps({"delta_time":delta_time,"actual ratio":input["actual ratio"],"time":input["time"]})
                sys.stdout.flush()
                prev_time = input["time"]

