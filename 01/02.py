from itertools import combinations

with open ('input.txt') as f:
    data = f.read().splitlines()

comb = combinations(data,3)


for combo in comb:
    if int(combo[0]) + int(combo[1]) + int(combo[2]) == 2020:
        print('{} * {} * {} = {}'.format(combo[0],combo[1],combo[2],int(combo[0]) * int(combo[1]) * int(combo[2])) )
    