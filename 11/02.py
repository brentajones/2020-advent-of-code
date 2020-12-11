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
    
def get_seats_to_check(floorplan,x,y):

    values = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    seats = []

    def find_seat(floorplan,x,y,direction):
        radius = 1
        while True:
            new_y = y + (direction[0] * radius)
            new_x = x + (direction[1] * radius)
            if new_y in range(len(floorplan)) and new_x in range(len(floorplan[0])):
                if floorplan[new_y][new_x] == 'L' or floorplan[new_y][new_x] == '#':
                    seat = (new_y,new_x)
                    return seat
                else:
                    radius += 1
            else:
                return None


    while len(seats)<8:
        for direction in values:
            seat = find_seat(floorplan,x,y,direction)
            seats.append(seat)
    return seats


def get_occupied(floorplan,x,y):
    to_check = get_seats_to_check(floorplan,x,y)
    to_check = [seat for seat in to_check if seat is not None]
    
    # to_check = [(y-1,x),(y-1,x+1),(y,x+1),(y+1,x+1),(y+1,x),(y+1,x-1),(y,x-1),(y-1,x-1)]
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
            elif floorplan[y][x] == "#" and num_occupied >= 5:
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