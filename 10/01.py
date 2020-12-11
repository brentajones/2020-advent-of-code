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
    
    numbers = []
    for line in lines:
        numbers.append(int(line))
    
    ones = 0
    threes = 0
    for x in range(len(numbers)):
        if x == 0:
            diff = sorted(numbers)[x] - 0
        else:
            diff = sorted(numbers)[x] - sorted(numbers)[x-1]
        if diff == 1:
            ones += 1
        else:
            threes += 1
    threes += 1
    print(ones, threes, ones * threes)