#

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adamas", "H. G. Wells"]

# scifi_athors.sort(key = lambda name: name.split(" ")[-1].lowwer())
# help(scifi_authors.sort)
scifi_authors.sort( key=lambda name: name.split(" ")[-1].lower())
print scifi_authors