with open ('input.txt') as f:
    data = f.read().splitlines()

length = len(data[0])

def slide(x,y):
    x_position = 0
    trees = 0
    
    slope = iter(data)
    for _ in range(y): 
            next(slope, None)
    for row in slope:
        x_position += x
        if x_position >= 31:
            x_position -= 31
        if row[x_position] == '#':
            trees += 1
        for _ in range(y-1): 
            next(slope, None)
    return trees

routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

total = 1
for route in routes:
    total = total * slide(*route)

print(total)