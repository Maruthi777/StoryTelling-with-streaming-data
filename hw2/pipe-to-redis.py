# In this program, we will connect to the Redis database and load values in the database
import json
import sys
import redis
import time

connection=redis.Redis() #establish connection. 

while True:
    reading = sys.stdin.readline()
    input = json.loads(reading)
    time_difference = input["delta_time"] #obtain values of delta_time and 
    t = input["time"] # time
    connection.setex(t, time_difference, 100) # setting value of t to be time_difference for 100 seconds.
    print json.dumps({"time difference":time_difference,"time":t}) #print difference and time.
    sys.stdout.flush() #flush to stdout
