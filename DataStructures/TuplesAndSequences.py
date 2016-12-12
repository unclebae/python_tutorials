t = 12345, 54321, 'hello'

print(t[0])
print(t)

u = t, (1, 2, 3, 4 ,5)
print(t[0])

# t[0]=8080 error occurs
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are access vi unpacking or indexing
# Lists are mutable, and hteir elements are usually homogeneous and are access by iteration over the list

empty = ()
singleton = 'hello'
print(len(empty))
print(singleton)
print(len(singleton))


