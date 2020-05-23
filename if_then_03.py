# Scalene Triangle  : All sides have different lengths.
# Isosceles Triangle : All sides have the same length.
# Equilateral Triangle : All sides are equal.

a = int(raw_input("The length of side a = "))
b = int(raw_input("The length of side b = "))
c =  int(raw_input("The length of side c = "))

if a!= b and b!=c and c!=a :
    print("This is a scalene triangle.")
elif a == b and b ==c :
    print("This is an equilateral triangle.")
else:
    print("This is an Isoscelens triangle.")


