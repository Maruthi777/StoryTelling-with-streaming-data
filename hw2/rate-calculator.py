import redis
import json
import time
import sys

connection = redis.Redis()

while 1:

    keys = connection.keys()

    data = connection.mget(keys)

    try:
        time_difference = [float(v) for v in data]
    except TypeError:
        print keys
        continue

    if len(time_difference):
        rate = sum(time_difference)/float(len(time_difference))
    else:
        rate = 0

    print json.dumps({"the rate is":rate})
    sys.stdout.flush()

    time.sleep(0.5)
