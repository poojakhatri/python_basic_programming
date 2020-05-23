# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print "Age - ", age
print "Country - ", country
print "Knows_python ? ", knows_python

# Another method to assign
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2

print "Age - ", age
print "Country - ", country
print "Knows_python ? ", knows_python