# A Set is an unordered collection with no duplicate elements

basket = {'apple', 'orange', 'apple', 'pear', 'orangle', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

a = {x for x in 'abracadarba' if x not in 'abc'}
print(a)