# List example
prime_numbers = [2,3,5,7,11,13,17]

# Tuple example
perfect_squares = [1,4,9,16,25,36]

# Display lengths
print "# Primes = ", len(prime_numbers)
print "# Squares = ", len(perfect_squares)

# Iterates over both sequences
for p in prime_numbers:
	print "Primes:",p

for n in perfect_squares:
	print "Squares:",n

print "List Methods"
print dir(prime_numbers)
print 80*"-"

print "Tuple methods"
print dir(perfect_squares)

