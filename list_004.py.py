# List: [1, 2, "a", "45", "3.14"]
# List Comprehensions :
#				[expr for val in collection]
#				[expr for val in collection if <test]
#				[expr for val in collection if  <test1> and <test2]
#				[expr for val1 in collection1 and val2 in collection2]


# List of remainders, when you divide first 100 squares by 5

remainders11 = [x**2 % 11 for x in range(1,101)] 

print remainders11

# p_remainders = [ x**2 %p for x in range(0,p)]
# len(p_remainders) = (p + 1) / 2