# Classes in Python

class User:
	pass

user1 = User() # user1 is an "instance" of User or user1 is an "object"
user1.first_name  = "Pooja"
user1.last_name  = "Khatri" # Field: Data attached to an object

print (user1.first_name)
print (user1.last_name)

# Style guide for Pytohn (PEP 8) "... lowercase with words separated by underscores as necessary to improve readability"

first_name = "Arthur"
last_name = "Clarke"

print (first_name, last_name) # Output : Arthur Clarke

print( user1.first_name, user1.last_name) # Output : Pooja Khatri