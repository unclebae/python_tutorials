# Python also includes a data type for sets.
# A set is an unordered collection with no duplicate elements.
# Set objects also support mathematical operations like union, interseciton, difference and symmetric difference

basket = {'apple', 'oragne', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('oragne' in basket)
print('crabgrass' in basket)

a = set('abracadbra')
b = set('alacazam')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in 'abracadbra' if x not in 'abc'}
print(a)