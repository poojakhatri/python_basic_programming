# Write random walk  function
# v1) Simple 
# v2) Short

# v1:
import random 

def  random_walk(n):
	"""Rreturn coordinates after 'n' block ranodm walk."""
	x = 0
	y = 0
	for i in range(n):
		step = random.choice(['N', 'S', 'E', 'N'])

		if step == 'N':
			y = y + 1
		elif step == "S":
			y =y - 1
		elif step == 'E':
			x = x + 1
		else:
			x = x - 1

	return (x,y)

for i in range(25):
	walk =  random_walk(10)
	print walk, "Distance From home :", abs(walk[0]) +abs(walk[1])