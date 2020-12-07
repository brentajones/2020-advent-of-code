def read_file(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        yield line

def strip_newline(rows):
    for row in rows:
        yield row.strip("\n")


def parse_bags(line):
    bag = {}
    
    outer = line.split('contain')[0].split(' ')[0:2]
    inner = line.split('contain')[1][:-1].split(',')

    bag['pattern'] = outer[0]
    bag['color'] = outer[1]
    

    bag['contents'] = []

    for in_bag in inner:
        in_bag = in_bag.strip()
        quantity = in_bag.split(' ')[0]
        pattern = in_bag.split(' ')[1]
        color = in_bag.split(' ')[2]

        if in_bag == "no other bags":
            bag['contents'] = None
        else:
            bag['contents'].append({"quantity":quantity,"pattern":pattern,"color":color})
    
    return bag

def search_bag(bag, all_bags):
    found = next(item for item in all_bags if item['pattern'] == bag['pattern'] and item['color'] == bag['color'])
    return found['contents']


with open ('input.txt') as f:
    lines = read_file(f)
    lines = strip_newline(lines)

    all_bags = []
    for line in lines:
        all_bags.append(parse_bags(line))

    total_bags = 0

    bags_to_search = [{"pattern":"shiny","color":"gold"}]

    while bags_to_search:
        searching = bags_to_search.pop()
        contents = search_bag(searching,all_bags)

        if contents is not None:
            for in_bag in contents:
                for x in range(int(in_bag['quantity'])):
                    bags_to_search.append(in_bag)
                total_bags += int(in_bag['quantity'])
    print(total_bags)
    # for bag in all_bags:




    #     possible_bags = []
    #     bags_to_search = [bag]
    #     bags_searched = []
        
    #     while bags_to_search:
    
    #         if contents is not None:
    #             for in_bag in contents:
    #                 if in_bag not in possible_bags:
    #                     possible_bags.append(in_bag)
    #                 if in_bag not in bags_searched:
    #                     bags_to_search.append(in_bag)
    #                 bags_searched.append(in_bag)

    #     gold = next((item for item in possible_bags if item['pattern'] == 'shiny' and item['color'] == 'gold'),None)
    #     if gold is not None:
    #         shiny_gold += 1
    # print(shiny_gold)