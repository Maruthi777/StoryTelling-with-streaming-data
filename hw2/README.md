#Homework 2

If we toss a dice, the probability of getting any face is 1/6. But if we actually take a dice and toss it and calculate probability of getting a face based on the outcome, the ratio for one face will be 1 and all other faces will be 0.
Similarly, if we toss the dice for a second time and calculate probability, the probability for at least four faces will be 0. 

However, it is interesting to note that if we continue this experiment long enough, the probability of getting any face will reach 1/6. 

In this we shall calculate a stream based on this distribution of probability.

Firstly, we calculate the probabilities for a 10-faced dice by tossing the dice and counting no: of time a number was obtained and dividing it with the number of dice castings.

Next, we calculate difference between actual and expected probabilities and check if the difference is greater than a certain threshold.

If the difference is greater than the specific threshold, then it means that the number of is biased positively or negatively in the dice. At the start, we expect this threshold to be crossed very often, but as the number of castings increase, it will get harder to cross the threshold value.

We note the time when the threshold value was crossed and calculate difference between last time the threshold was crossed and now. 

The difference, as a result, keeps getting bigger and bigger as the number of castings increases. We store value of difference and time in Redis database.

The rate is the rate at which these difference and times are obtained and stored in the database. If the rate is high, then it is interesting becuase it means that the dice is biased.

The randomtoss.py file deals with generating a random number in range of 0 to 9 for infinitely many times. Then, it calculates the number of times a particular number was obtained divided by the number of dice-castings. This gives us the probability of seeing that number.

Next, we pipeline randomtoss.py to diff-calculate.py by using the command 
		
		python randomtoss.py | python diff-calculate.py

The diff-calculate calculates the difference between the ratio from randomtoss.py and the actual probability of getting a number from 10 numbers( i.e, 0.1).

We now pipe the output from diff-calculate.py to rate-gen.py file. The function of the rate-gen is to calculate the time difference between when the differences(say, time-delta) were above  certain threshold. We do this by following command

		python randomtoss.py | python diff-calculate.py | python rate-gen.py
		
the output from previous step is flushed to std in of pipe-to-redis.py. This file connects to the Redis database and stores the contents of the time-delta and the time at which this time-delta was obtained. For this, we use setex(x,y,z) which sets the name of key to x, value as y and time for which it is stored as z(z in seconds).

To do this, we need to pipe output of previous step to pipe-to-redis.py. We can do this by 

		python randomtoss.py | python diff-calculate.py | python rate-gen.py | python pipe-to-redis.py
		
Finally to calculate the rate, we call the program rate-calculator.py. It gets its values from the redis database and calculates the rate of the messages(ie, delta-time which satisfy the condition). 