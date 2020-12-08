import copy

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

    
    target = len(instructions)

    for x in range(len(instructions)):
        modified_instructions = copy.deepcopy(instructions)
        if instructions[x]["type"] == 'jmp':
            modified_instructions[x]["type"] = 'nop'
        elif instructions[x]["type"] == 'nop':
            modified_instructions[x]["type"] = 'jmp'

        print(x, instructions[x],modified_instructions[x])
        executed = []
        next_inst = 0
        acc = 0
        while next_inst not in executed:
            # print(next_inst)
            output = exec_inst(modified_instructions[next_inst],next_inst)
            executed.append(next_inst)
            acc += output[0]
            next_inst = output[1]
            if next_inst == target:
                print(acc)
