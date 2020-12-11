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

def generate_sequence(numbers,device):
    sequence = [0]

    while numbers:
        valid = [x for x in numbers if x <= max(sequence) + 3]

        if not valid:
            return False
        choice = min(valid)
        sequence.append(choice)
        numbers.remove(choice)

    
    if max(sequence) >= device - 3:
        return True
        


with open ('input.txt') as f:
    lines = read_file(f)
    lines = strip_newline(lines)
    
    numbers = [0]
    for line in lines:
        numbers.append(int(line))


    device = max(numbers) + 3

    numbers.append(device)
    
    
    tree = {}
    current_numbers = sorted(numbers)

    for number in current_numbers:
        valid = [x for x in numbers if number < x <= number + 3]

        tree[number] = valid

    def get_in_paths(key):
        in_paths = []
        for parent,values in tree.items():
            if key in values:
                in_paths.append(parent)
        return in_paths
    

    appearances = {}
    
    for key,value in tree.items():

        appearances[key] = {}
        appearances[key]["paths"] = get_in_paths(key)

        if get_in_paths(key):
            appearances[key]["total"] = 0
        else:
            appearances[key]["total"] = 1
        for parent in appearances[key]["paths"]:
            appearances[key]["total"] += appearances[parent]["total"]
        print("{} is referenced by {} and references {}. It appears {} times.".format(key,appearances[key]["paths"],value,appearances[key]["total"]))
    