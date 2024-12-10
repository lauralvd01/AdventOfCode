# Day 5, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day05_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day05.txt", 'r')

part = 2

def check_order(update, rules) :
    right = True
    to_check = 1
    to_put_after = None
    while to_check < len(update) :
        if update[to_check] in rules.keys() :
            for number in rules[update[to_check]] :
                j = 0
                while j < to_check :
                    if number == update[j] :
                        to_put_after = j
                        return (to_check, to_put_after)
                    j += 1
        to_check += 1
    return True

def solve(part):
    if part == 1:
        # PART 1

        parts = data_file.read().split('\n\n')
        data_file.close()
        
        rules = {}
        updates = []
        for line in parts[0].split('\n') :
            numbers = line.split('|')
            first = int(numbers[0])
            second = int(numbers[1])
            if first not in rules.keys() :
                rules[first] = [second]
            else :
                rules[first].append(second)
        
        for line in parts[1].split('\n') :
            pages = line.split(',')
            updates.append([int(page) for page in pages])
    
        total = 0
        for update in updates :
            right = True
            i = 1
            while right and i < len(update) :
                if update[i] in rules.keys() :
                    for number in rules[update[i]] :
                        if number in update[:i] :
                            right = False
                            break
                i += 1
                
            if right :
                total += update[len(update)//2]
                
        return total  # Answer is 4996

    elif part == 2:
        # PART 2

        parts = data_file.read().split('\n\n')
        data_file.close()
        
        rules = {}
        updates = []
        for line in parts[0].split('\n') :
            numbers = line.split('|')
            first = int(numbers[0])
            second = int(numbers[1])
            if first not in rules.keys() :
                rules[first] = [second]
            else :
                rules[first].append(second)
        
        for line in parts[1].split('\n') :
            pages = line.split(',')
            updates.append([int(page) for page in pages])
    
        total = 0
        for update in updates :
            if check_order(update, rules) != True :
                while check_order(update, rules) != True :
                    to_check, to_put_after = check_order(update, rules)
                    to_put_before = update.pop(to_check)
                    update.insert(to_put_after, to_put_before)
                
                total += update[len(update)//2]
        
        return total  # Answer is 6311

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
