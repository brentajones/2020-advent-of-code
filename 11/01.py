from itertools import combinations

def read_file(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        yield line

def strip_newline(rows):
    for row in rows:
        yield row.strip("\n")




with open ('input.txt') as f:
    lines = read_file(f)
    lines = strip_newline(lines)
    
    seats = []
    for line in lines:
        seats.append(line)
    
def get_occupied(floorplan,x,y):
    to_check = [(y-1,x),(y-1,x+1),(y,x+1),(y+1,x+1),(y+1,x),(y+1,x-1),(y,x-1),(y-1,x-1)]
    occupied = 0
    for value in to_check:
        if value[0] in range(len(floorplan)) and value[1] in range(len(floorplan[0])):
            if floorplan[value[0]][value[1]] == '#':
                occupied += 1
    return occupied


def simulate(floorplan):
    new_grid = []
    for y in range(len(floorplan)):
        new_grid.append([])
        for x in range(len(floorplan[y])):
            num_occupied = get_occupied(floorplan,x,y)
            if floorplan[y][x] == "L" and num_occupied == 0:
                new_grid[y] += '#'
            elif floorplan[y][x] == "#" and num_occupied >= 4:
                new_grid[y] += 'L'
            else:
                new_grid[y] += floorplan[y][x]
        new_grid[y] = "".join(new_grid[y])
    occupied = 0
    for row in new_grid:
        occupied += row.count('#')
    return [occupied,new_grid]
    

occupied = 0

while simulate(seats)[0] != occupied:
    occupied = simulate(seats)[0]
    seats = simulate(seats)[1]
    print(occupied)
    for row in seats:
        print(row)
print(occupied)