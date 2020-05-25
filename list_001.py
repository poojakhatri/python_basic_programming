# List: [1, 2, "a", "45", "3.14"]
# List Comprehensions :
#				[expr for val in collection]
#				[expr for val in collection if <test]
#				[expr for val in collection if  <test1> and <test2]
#				[expr for val1 in collection1 and val2 in collection2]


# List of squares 
#Without list comprehension
squares = []

for i in range(1,101):
	squares.append(i**2)

print squares