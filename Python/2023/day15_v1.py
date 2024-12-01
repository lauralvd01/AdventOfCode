# Day 15, part 1 of Advent of Code 2023

#data_file = open('./Data/2023/day15_test1.txt', 'r')

data_file = open('./Data/2023/day15.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

def HASH(string) :
    current_value = 0
    for c in string :
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

steps = [x for x in data_lines[0].split(',') if x != '']
result = 0
for step in steps :
    #print(step,' -> ',HASH(step))
    result += HASH(step)
    
print('Result = ',result)
# Answer is 510801
