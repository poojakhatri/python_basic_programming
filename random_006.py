# Random element from a list
# Random selection from a list of values which are not values
# for ex- Rock Paper Scissors Game

import random

outcomes = ['rock', 'paper', 'scissors']

for i in range(20):
	print random.choice(outcomes)