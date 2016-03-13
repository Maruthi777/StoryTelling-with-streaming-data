# In this program, we shall check for a condition and calculate the difference in time from when
# that condition was last satisfied to current- if its currently satisfied.
import json
import sys
import time
import numpy as np
import redis

connection=redis.Redis()

prev_time=np.array(range(0,100))
for i in range(0,100):
        prev_time[i]=0 
#prev=0
#initialise value of previous time difference>0.01 as 0
while 1:
        prev_output = sys.stdin.readline()
        input = json.loads(prev_output)
    	x= input["number"]
    	if input["difference in the ratio"]>0.001:
        	if prev_time[x] == 0 : #if its 0, update and continue
            	    	prev_time[x]= input["time"]
                	continue        
        	delta_time = input["time"] - prev_time[x] #calculate difference between now and last time when difference>0.01
        	print json.dumps({"number":input["number"], "difference in ratio":input["difference in the ratio"],"delta_time":delta_time,"actual ratio":input["actual ratio"],"time":input["time"]})
        	t= input["time"]
        	connection.setex(x,delta_time,10)
        	sys.stdout.flush()#flush to stdout
        	prev_time[x] = input["time"]#update previous time this event occurred to current time.