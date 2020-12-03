with open ('input.txt') as f:
    data = f.read().splitlines()

length = len(data[0])

x_position = 0
trees = 0
for row in data[1:]:
    x_position += 3
    if x_position >= 31:
        x_position -= 31
    if row[x_position] == '#':
        trees += 1
print(trees)