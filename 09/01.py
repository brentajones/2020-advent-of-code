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

def check_num(numbers,index):
    target = numbers[index]

    for combo in list(combinations(numbers[index-25:index],2)):
        if sum(combo) == target:
            return True
    return False



with open ('input.txt') as f:
    lines = read_file(f)
    lines = strip_newline(lines)
    
    numbers = []
    for line in lines:
        numbers.append(int(line))

    x = 25
    while x < len(numbers):
       
        if check_num(numbers,x):
            x += 1
        else:
            print(numbers[x])
            break