with open ('input.txt') as f:
    data = f.read().splitlines()

passwords = []
for line in data:
    pieces = line.split(' ')

    password = {}
    password['low'] = int(pieces[0].split('-')[0]) - 1
    password['high'] = int(pieces[0].split('-')[1]) - 1
    password['letter'] = pieces[1].replace(':','')
    password['password'] = pieces[2]

    passwords.append(password)

def check_password(password):
    count = password['password'].count(password['letter'])

    if (password['password'][password['low']] == password['letter']) ^ (password['password'][password['high']] == password['letter']):
        return True

count_up = 0

for password in passwords:
    
    if check_password(password):
        count_up += 1

print(count_up)