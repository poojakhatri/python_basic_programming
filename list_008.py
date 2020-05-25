# Cartesian Product Using List Comprehension

A = [1, 3, 5, 7] 
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print cartesian_product