# Does every function need a name?
# There are functions they dont have name at all.
# These nameless functions are callled as Anonymous functions or Lambda functions

# Write function to compute 3x+1

def f(x):
	return 3*x+1

print f(3) #output: 10

# With lambda Expression

lambda x: 3*x + 1 # we can't use this function because this does not have any name.

# Lets give new name to this lambda function

g = lambda x: 3*x + 1

print g(3) # Output: 10