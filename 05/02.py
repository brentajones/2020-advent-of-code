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


    ids = []
    for line in lines:
        row = [0,127]
        for letter in line[:-3]:
            row = find_row(letter,row)
            final_row = int(row[0])
        
        col = [0,7]
        for letter in line[-3:]:
            col = find_row(letter,col)
            final_col = int(col[0])

        ids.append((final_row*8) + final_col)

    seats = sorted(ids)

    for i in range(len(seats) - 1):
        if seats[i] + 1 != seats[i+1]:
            print(seats[i],seats[i+1])