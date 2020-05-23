# Fibonacci Program with Memoization
# Memoization :Memoization is saving the result of a function after it's been computed for the first time. 
# 			   The next time you need to compute the function for the same argument,
# 			   You can just look the result up in memory.

# Idea : Cache values
# 1. Implement explicitly
# 2. Use builtin Python tool

#Implementing Second method Built in Python tool

ef fibonacci(n):
	if n ==1:
		return 1
	elif n==2:
		return 1
	elif n >2 :
		return fibonacci(n-1)+fibonacci(n-2) # repeating multiple time

for n in range(1, 11):
	print n, ":", fibonacci(n)