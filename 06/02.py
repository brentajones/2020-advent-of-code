def read_file(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        yield line

def strip_newline(rows):
    for row in rows:
        yield row.strip("\n")

def separate_rows(rows):
    for row in rows:
        new_rows = row.split(' ')
        for row in new_rows:
            yield row


def find_row(letter,row):
    num_rows = (row[1] - row[0] + 1) / 2
    if letter in ['F','L']:
        row[1] = row[0] + num_rows - 1
        return row
    if letter in ['B','R']:
        row[0] = row[1] - num_rows + 1
        return row

with open ('input.txt') as f:
    lines = read_file(f)
    lines = strip_newline(lines)
    lines = separate_rows(lines)


    groups = []
    cur_group = []
    for line in lines:
        if line == '':
            groups.append(cur_group)
            cur_group = []
        else:
            cur_group.append(line)
        
    total = 0
    for group in groups:
        # print(group)
        letters = {}
        for ans in group:
            for letter in ans:
                if letter not in letters.keys():
                    letters[letter] = 1
                else:
                    letters[letter] += 1
    
        total += list(letters.values()).count(len(group))

        
    print(total)