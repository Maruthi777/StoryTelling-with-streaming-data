# In this program, we will calculate the rate by getting values from Redis

import redis
import json
import time
import sys

connection = redis.Redis() #establish connection

while 1:

    keys = connection.keys() #get keys

    data = connection.mget(keys) #get all data

    try: #so that no unexpected errors arise
        time_difference = [float(v) for v in data] 
    except TypeError: #so that no unexpected errors arise
        print keys
        continue

    if len(time_difference): #calculate rate
        rate = sum(time_difference)/float(len(time_difference))
    else:
        rate = 0

    print json.dumps({"the rate is":rate}) #print rate
    sys.stdout.flush() # flush to stdout
    if rate < 0.622:
	print "LOOKS LIKE UNFAIR DICE"
	sys.stdout.flush()
    time.sleep(0.5) #sleep
