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

with open ('input.txt') as f:
    lines = read_file(f)
    lines = strip_newline(lines)
    lines = separate_rows(lines)

    passports = []
    current_passport = {}
    for line in lines:
        if line != '':
            pair = line.split(":")
            current_passport[pair[0]] = pair[1]
        else:
            passports.append(current_passport)
            current_passport = {}
    
    valid = 0
    keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    keys_w_cid = ['cid','byr','iyr','eyr','hgt','hcl','ecl','pid']
    for passport in passports:
        if 'cid' in passport.keys():
            key_test = keys_w_cid
        else:
            key_test = keys
        if sorted(passport.keys()) == sorted(key_test):
            print(passport)
            valid += 1
        print(len(passports))
    print(valid)