# In this program, we first select a random number, say x, from 0-9.
# We then calculate how may times x is selected when a 10-sided dice with values from 0-9
# for infinitely many times. One thing to keep in mind is that as the number of tosses goes up,
# the value of number of times x is obtained to total no: of dice-castings will reach 0.1(which is actual
# probability of getting 1 number from a set of 10) asymptotically.
import numpy as np
import time
import sys
import json
import random
r=np.array(range(0,100)) #initialising some values to keep track of no:of time a number is selected
ratio=np.array(range(0,100))
for i in range(0,100):
        r[i]=0 #initialising all values to 0 because count starts from 0
        ratio[i]=0
total=0
#integer=random.randint(0,99) # a random number from 0-9 is picked
while 1: #repeat forever
        total=total+1 #update number of dice castings
        sel_rand=random.randint(0,99) #the actual casting of the 10-sided dice
        r[sel_rand]=r[sel_rand]+1 # value of integer selected before.
        ratio=float(r[sel_rand])/(total) #ratio of number of time integer is obtained/no:of dice castings
        print json.dumps({"ratio":ratio, "number":sel_rand}) #printing ratio in JSON format
        sys.stdout.flush() #flushing to standard output
        time.sleep(0.125) #sleep for random amount of time
