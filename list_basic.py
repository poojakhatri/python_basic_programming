v = [2, -3, 1]
print 4*v

#output: [2, -3, 1, 2, -3, 1, 2, -3, 1, 2, -3, 1]

l1 = [2, 4, 6] 
l2 = [1, 3]
print l1+l2

#output : [2, 4, 6, 1, 3]

# We can achieve Scalar Multiplication wtih list Comprehension
w = [4*x for x in v]

print w

