# Day 12, part 1 of Advent of Code 2023

#data_file = open('./Data/2023/day12_test1.txt', 'r')

data_file = open('./Data/2023/day12.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

def get_all_possibilities(springs) :
    if len(springs) == 1 :
        if springs[0] != '?' :
            return [springs]
        else :
            return ['.','#']
    else :
        next = get_all_possibilities(springs[1:])
        possibilities = []
        for i in range(len(next)) :
            if springs[0] != '?' :
                possibilities.append(springs[0] + next[i])
            else :
                possibilities.append('.' + next[i])
                possibilities.append('#' + next[i])
        return possibilities
    
result = 0
for line in data_lines :
    springs = line.split(' ')[0].strip()
    groups = [int(num) for num in line.split(' ')[1].strip().split(',')]
    #print(springs,groups)
    
    possibilities = get_all_possibilities(springs)
    permutations = len(possibilities)
    for possibility in possibilities :
        damaged_groups = []
        i = 0
        while i < len(possibility) :
            if possibility[i] == '#' :
                length = 1
                i += 1
                while i < len(possibility) and possibility[i] == '#' :
                    length += 1
                    i += 1
                damaged_groups.append(length)
            else :
                i += 1
        #print(possibility,damaged_groups)
        
        if damaged_groups != groups :
            permutations -= 1
    
    result += permutations
    
print('Result = ',result)
# Answer is 7286