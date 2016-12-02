def make_incrementor(n):
    return lambda x: x+n
f = make_incrementor(42)

for value in list(range(1, 10)):
    print(f(value))


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
pairs.sort(key = lambda pair: pair[0], reverse=True)

print(pairs)