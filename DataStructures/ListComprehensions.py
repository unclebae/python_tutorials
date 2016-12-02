from math import pi

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# using lambda
squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

# for if  clause
squares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y ]
print(squares)

# it's equivalent to upper codes
squares = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            squares.append((x, y))
print(squares)

# etcs lists comprehension
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x > 0])
print([abs(x) for x in vec])

freshfruit = ['   banana', '   loganberry ', 'passion fruit   ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])

# print([x, x**2 for x in range(6)]) errors occur

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

print([str(round(pi, i)) for i in range(1, 6)])