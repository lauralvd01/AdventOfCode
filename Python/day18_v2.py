# Day 18, part 2 of Advent of Code 2023

data_file = open('./Data/day18_test1.txt', 'r')

#data_file = open('./Data/day18.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

directions = ['R','D','L','U']

count_LEFT = 0
count_UP = 0
for line in data_lines :
    digits = line.split('#')[1].strip()
    direction = directions[int(digits[-2])]
    nb = int('0x'+digits[:-2],16)
    if direction == 'L' :
        count_LEFT += nb
    if direction == 'U' :
        count_UP += nb

print(count_LEFT,count_UP)

lagoon = [['.' for j in range(count_LEFT+1)] for i in range(count_UP+1)]
result = 0

current = [count_UP,count_LEFT]
for line in data_lines :
    digits = line.split('#')[1].strip()
    direction = directions[digits[-2]]
    nb = int('0x'+digits[:-2],16)
    
    if direction == 'R' :
        for j in range(nb) :
            if current[1] + j + 1 < len(lagoon[current[0]]) :
                lagoon[current[0]][current[1] + j + 1] = '#'
            else :
                lagoon[current[0]].append('#')
            result += 1
        current[1] += j + 1
        
    if direction == 'D' :
        for i in range(nb) :
            if current[0] + i + 1 < len(lagoon) :
                if current[1] >= len(lagoon[current[0] + i + 1]) :
                    for j in range(len(lagoon[current[0] + i + 1]),current[1]+1) :
                        lagoon[current[0] + i + 1].append('.')
            else :
                lagoon.append(['.' for dig in range(len(lagoon[current[0] + i]))])
            lagoon[current[0] + i + 1][current[1]] = '#'
            result += 1
        current[0] += i + 1
    
    if direction == 'L' :
        for j in range(nb) :
            if current[1] - j - 1 < 0 :
                print(current,line)
                raise IndexError
            lagoon[current[0]][current[1] - j - 1] = '#'
            result += 1
        current[1] = current[1] - j - 1
    
    if direction == 'U' :
        for i in range(nb) :
            if current[0] - i - 1 < 0 :
                print(current,line)
                raise IndexError
            if current[1] >= len(lagoon[current[0] - i - 1]) :
                for j in range(len(lagoon[current[0] - i - 1]),current[1]+1) :
                    lagoon[current[0] - i - 1].append('.')
            lagoon[current[0] - i - 1][current[1]] = '#'
            result += 1
        current[0] = current[0] - i - 1


#fill_start = [10,11]
#fill_start = [1012,988]
#file_to_process =[fill_start]
file_to_process = []

def get_neighbors(current) :
    global lagoon
    n = []
    for i in [current[0]-1,current[0],current[0]+1] :
        nn = [[i,j] for j in [current[1]-1,current[1],current[1]+1] if lagoon[i][j] != '#']
        if len(nn) > 0 : 
            for nnn in nn :
                n.append(nnn)
    return n

def fill_area(current) :
    global lagoon
    global result
    global file_to_process
    if lagoon[current[0]][current[1]] != '#' :
        lagoon[current[0]][current[1]] = '#'
        result += 1
    
    neighbors = get_neighbors(current)
    for neighbor in neighbors :
        if neighbor not in file_to_process :
            file_to_process.append(neighbor)
    
    #fill_area(neighbor)
    return 

#fill_area(fill_start)
while len(file_to_process) > 0 :
    print(len(file_to_process))
    next = file_to_process[0]
    file_to_process.remove(next)
    fill_area(next)

#print('\n'.join(''.join(dig for dig in row) for row in lagoon))
print('\nResult = ',result)
# Answer is 

file = open('./Data/day18_test1_result.txt','w')
#file = open('./Data/day18_result.txt','w')
file.write('\n'.join(''.join(dig for dig in row) for row in lagoon))
file.close()