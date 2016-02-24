import json
import sys
import redis
import time

connection=redis.Redis()

while True:
    reading = sys.stdin.readline()
    input = json.loads(reading)
    time_difference = input["delta_time"]
    t = input["time"]
    #print difference," 1 "
    connection.setex(t, time_difference, 120)
    print json.dumps({"time difference":time_difference,"time":t})
    sys.stdout.flush()
