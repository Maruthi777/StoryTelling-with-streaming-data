import json
import sys
import time

last = 0
while 1:
    prev = sys.stdin.readline()
    input = json.loads(prev)
    difference = abs(input["ratio"] - 0.1)
    t = time.time()
    print json.dumps({"difference in the ratio":difference,"actual ratio":input["ratio"],"time":t})
    sys.stdout.flush()
