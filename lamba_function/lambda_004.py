# Quadratic function using Lambda Expression

def build_quadratic_function(a, b, c):
	"""Returns the function f(x) = ax^2+ bx + c """
	return lambda x: a*x**2 + b*x + c

f= build_quadratic_function(2, 3, -5)

print(f(0))