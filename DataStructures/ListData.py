a = [66.25, 333, 333, 1, 1234.5]

# Return the number of times x appears in the list.
print(a.count(333), a.count(66.25), a.count('x'))

# Insert an item at a given position.
# The first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
a.insert(2, -1)
print(a)

# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
a.append(333)
print(a)

# Return the index in the list fo the first item whose value is x.
# It is an error if there is no such itme.
print(a.index(333))

# Reverse the elements of the list in place.
a.reverse()
print(a)

# Sort the items of the list in place (the arguments can be used for sort customization,
# see sorted() for their explanation)
a.sort()
print(a)

a.sort(reverse=True)
print(a)

# Remove the item at the given in the list, and return it.
# If no index is specified, a.pop() removes and return the last item in the list.
# (The square brackets around the i in the method signature denote that the
#   parameter is optional, not that you should type square brackets at that positioin.
#   You will see this notation frequently in the Python Library Reference.)
print(a.pop())

print(a)
