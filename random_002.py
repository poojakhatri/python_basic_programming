# Generate random numbers from interval [3,7]

# Call random():  in interval [0,1)
# scale number by multiply random number with 4 : in [0,4)
# Shift number (add 3) : # in [3,7)


import random

def my_random():
	# Random, scale, shift, return ...
	return 4*random.random()+3

for i in range(10):
	print my_random()