# In this file, we get the std out that has been flushed from randomtoss.py. The std out is 
# in JSON format and contains information regarding obtained ratio. We use this information to 
# calculate diff between actual and expected ratios and flush it to std out.
import json
import sys
import time

while 1: #repeat forever
    prev_output = sys.stdin.readline() #read from stdin
    input = json.loads(prev_output) #load data in "input"
    difference = abs(input["ratio"] - 0.1) #calculate the difference
    t = time.time()
    print json.dumps({"difference in the ratio":difference,"actual ratio":input["ratio"],"time":t}) #print in JSON format the difference in ratios, actual ratio and timestamp at which it was obtained
    sys.stdout.flush() #flush to std out
    
