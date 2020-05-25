# List: [1, 2, "a", "45", "3.14"]
# List Comprehensions :
#				[expr for val in collection]
#				[expr for val in collection if <test]
#				[expr for val in collection if  <test1> and <test2]
#				[expr for val1 in collection1 and val2 in collection2]


# List with if 
# single line
# movies with year date
# dummy year

# Find movies released before 2000
movies= [("Shawshank Redemption", 1931), ("Godfather",2006), ("The Godfather: Part II", 1941), ("The Dark Knight",2000), ("12 Angry Men",1989), ("Schindler's List",2014) ,(" Lord of the Rings: The Return of the King",2004),( "Pulp Fiction",2018), ("Good",2016), ("the Bad and the Ugly",2010), ("The Lord of the Rings: The Fellowship of the Ring",2002)]
#movies = [("Citizen kane", 1941), ("Good", 1930), ("Mon", 2000)]
pre2k = [title for (title,year) in movies if year < 2000]

print (pre2k)