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

def valid_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True

def valid_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True

def valid_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True

def valid_hgt(hgt):
    if hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            return True
    else:
        if 150 <= int(hgt[:-2]) <= 193:
            return True

def valid_hcl(hcl):
    allowed = '0123456789abcdef'
    if hcl[0] == "#" and len(hcl) == 7:
        for char in hcl[1:]:
            if char not in allowed:
                return False
            else:
                return True


def valid_ecl(ecl):
    allowed = ['amb','blu','brn','gry','grn','hzl','oth']
    if ecl in allowed:
        return True

def valid_pid(pid):
    if len(pid) == 9:
        print(pid)
        return True

def validate(passport):
    if valid_byr(passport['byr']) and valid_iyr(passport['iyr']) and valid_eyr(passport['eyr']) and valid_hgt(passport['hgt']) and valid_hcl(passport['hcl']) and valid_ecl(passport['ecl']) and valid_pid(passport['pid']):
        return True

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
            if validate(passport):
                valid += 1
    print(valid)