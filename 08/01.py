def read_file(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        yield line

def strip_newline(rows):
    for row in rows:
        yield row.strip("\n")

def add_index(rows):
    index = 1
    for row in rows:
        yield str(index) + ' ' + row
        index += 1

def exec_inst(inst,index):
    if inst["type"] == 'acc':
        return (int(inst["value"]),index + 1)
    elif inst["type"] == 'jmp':
        return (0,index + int(inst["value"]))
    else:
        return (0, index + 1)

with open ('input.txt') as f:
    lines = read_file(f)
    lines = strip_newline(lines)
    # lines = add_index(lines)

    instructions = []
    for line in lines:
        line = line.split(' ')
        instructions.append({'type':line[0],'value':line[1]})

    executed = []
    next_inst = 0
    acc = 0

    while next_inst not in executed:
        output = exec_inst(instructions[next_inst],next_inst)
        executed.append(next_inst)
        acc += output[0]
        next_inst = output[1]
    print(acc)



    
    