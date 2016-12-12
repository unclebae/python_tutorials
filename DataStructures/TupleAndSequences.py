t = 12345, 54321, 'hello!'
print(t[0])

print(t)

# As you see, on output tuples are always enclosed in parentheses, so that nested tuples
# are interpreted correctly;

# It is not possible to assign to the individual items of a tuple, however it is possible to
# create tuples which contain mutable objects, such as lists.
u = t, (1, 2, 3, 4, 5)
print(u)

# Though tuple may seem similar to lists, they are often used in different situations and for different purposes.
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking
# (see later in this section) or indexing (or even by attribute in the case of namedtuples).
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

empty = ()
singleton = 'hello',
print(len (empty))

print(len(singleton))

print(singleton)