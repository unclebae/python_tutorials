# Dictionaries are sometimes found in other languages as "associative memories" or "associative arrays"
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys,
# which can be any immutable type;
# strings and numbers can always be keys

tel = {'jack':4098, 'sape':4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel ['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))
print(tel.values())
print(list(tel.values()))
print(sorted(tel.keys()))

print('guido' in tel)
print('sape' in tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs.
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(a)

print({x: x**2 for x in (2, 5, 6)})

b = dict(shape=4139, guido=4127, jack=4098)
print(b)

# When looping throught dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad':'the_pure', 'robin':'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping throught a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questiongs = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questiongs, answers) :
    print('What is your {0}? It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first sepcify the sequence in a forward direction and then call the reversed() function/
for i in reversed(range(1, 10, 2)):
    print(i)

# The loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'oragne', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)


