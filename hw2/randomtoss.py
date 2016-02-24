import numpy as np
import time
import sys
import json
import random
r=np.array(range(0,10))
for i in range(0,10):
        r[i]=0
total=0
integer=random.randint(0,9)
#print integer
while 1:
        total=total+1
        sel_rand=random.randint(0,9)
        if(sel_rand==integer):
                r[integer]=r[integer]+1
        ratio=float(r[integer])/(total)
        print json.dumps({"ratio":ratio})
        sys.stdout.flush()
        time.sleep(0.05)
