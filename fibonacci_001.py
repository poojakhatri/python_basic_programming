# fibonacci program using recursion
# when n becomes large this program will run slow like dead
def fibonacci(n):
	if n ==1:
		return 1
	elif n==2:
		return 1
	elif n >2 :
		return fibonacci(n-1)+fibonacci(n-2) # repeating multiple time

for n in range(1, 11):
	print n, ":", fibonacci(n)

# simple solution to this problem is Memoization
# can check another program of fibonacci_002.py