# List: [1, 2, "a", "45", "3.14"]
# List Comprehensions :
#				[expr for val in collection]
#				[expr for val in collection if <test]
#				[expr for val in collection if  <test1> and <test2]
#				[expr for val1 in collection1 and val2 in collection2]


# List with if 
movies= ["Shawshank Redemption", "Godfather", "The Godfather: Part II", "The Dark Knight", "12 Angry Men, Schindler's List" ," Lord of the Rings: The Return of the King", "Pulp Fiction", " Good", "the Bad and the Ugly", "The Lord of the Rings: The Fellowship of the Ring"]

gmovies = []
for title in movies:
	if title.startswith("G"):
		gmovies.append(title)

print gmovies