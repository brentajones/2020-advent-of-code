with open ('input.txt') as f:
    data = f.read().splitlines()

passwords = []
for line in data:
    pieces = line.split(' ')

    password = {}
    password['low'] = pieces[0].split('-')[0]
    password['high'] = pieces[0].split('-')[1]
    password['letter'] = pieces[1].replace(':','')
    password['password'] = pieces[2]

    passwords.append(password)

def check_password(password):
    count = password['password'].count(password['letter'])

    if int(password['low']) <= count <= int(password['high']):
        return True

count_up = 0
for password in passwords:
    
    if check_password(password):
        count_up += 1

print(count_up)