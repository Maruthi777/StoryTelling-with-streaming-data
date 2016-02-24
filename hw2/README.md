#Homework 2

In this we shall calculate a stream based on distribution of probability.

In this we shall consider a 10-sided dice with value from 0 to 9. The randomtoss.py file deals with generating a random number in range of 0 to 9 for infinitely many times. Then, it calculates the number of times a particular number was obtained divided by the number of dice-castings. This gives us the probability of seeing that number.

Next, we pipeline randomtoss.py to diff-calculate.py by using the command 
		
		python randomtoss.py | python diff-calcualte.py

The diff-calcualte calculates the difference between the ratio from randomtoss.py and the actual probability of getting a number from 10 numbers( i.e, 0.1).