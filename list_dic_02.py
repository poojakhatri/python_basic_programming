import sys

list_eg = [1,2,3, "a", "b", "c", True, 23.3222]
tuple_eg = (1,2,3, "a", "b", "c", True, 23.3222)

print "List size = ", sys.getsizeof(list_eg)
print " Tuple size = ", sys.getsizeof(tuple_eg)
