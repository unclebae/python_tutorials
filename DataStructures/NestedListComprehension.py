matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

transpose = []
for i in range(4):
    transpose.append([row[i] for row in matrix])

print(transpose)

transpose = []
for i in range(4):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose.append(transpose_row)
print(transpose)

print(list(zip(*matrix)))