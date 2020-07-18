# Program to find the ASCII value of the given character

char_ = 'F'

def increment(i): 
    i = -(~ord(i))
    return chr(i) 

while ord(char_) <=ord('P'):
	print(ord(char_))
	char_= increment(char_)
	