# Fibonacci Program with Memoization
# Memoization :Memoization is saving the result of a function after it's been computed for the first time. 
# 			   The next time you need to compute the function for the same argument,
# 			   You can just look the result up in memory.

# Idea : Cache values
# 1. Implement explicitly
# 2. Use builtin Python tool

# Implementing first Methond - Explicitly
fibonacci_cache = {} # store recent calls

def fibonacci(n):
	# If we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	# Compute the Nth term
	if n == 1 :
		value = 1
	elif n== 2 :
		value = 1
	elif n > 2 :
		value = fibonacci(n-1)+fibonacci(n-2)

	# Cache the value and return it
	fibonacci_cache[n] = value
	return value


for n in range(1, 101):
	print n, ":", fibonacci(n)