def increment(i): 
  
    # Invert bits and 
    # apply negative sign 
    i = -(~ord(i))
    return chr(i) 
  
# Driver code 
n = 'a'
print(increment(n))