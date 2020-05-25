# Write random walk  function
# v1) Simple 
# v2) Short

# v2:

import random

def random_walk_2(n):
	"""Return coordinates after 'n' block random walk."""
	x,y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx
		y += dy
	return (x, y)

for i in range(25):
	walk =  random_walk_2(10)
	print walk, "Distance From home :", abs(walk[0]) +abs(walk[1])

# What is the longest random wlak you can take so that on average you will end up 4 blocks or fewer from home?

#Monte Carlo
