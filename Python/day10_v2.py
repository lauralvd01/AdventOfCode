# Day 10, part 2 of Advent of Code 2023

data_file = open('./Data/day10_test3.txt', 'r')
#data_file = open('./Data/day10_test4.txt', 'r')

#data_file = open('./Data/day10.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

i = 0
while i < len(data_lines) :
    j = data_lines[i].find('S')
    if j > -1 :
        start = (i,j)
        break
    i += 1
#print(start)

def get_pipe_neighbors(current,before=None) :
    (i,j) = current
    north = (i-1,j) if i > 0 and data_lines[i-1][j] in ['|','7','F'] else None
    east = (i,j+1) if j < len(data_lines[i])-1 and data_lines[i][j+1] in ['-','J','7'] else None
    south = (i+1,j) if i < len(data_lines)-1  and data_lines[i+1][j] in ['|','L','J'] else None
    west = (i,j-1) if j > 0 and data_lines[i][j-1] in ['-','F','L'] else None
    return [neighbor for neighbor in [north,east,south,west] if neighbor != None and neighbor != before]

loop = ['S']
loop_ind = [start]
neighbors = get_pipe_neighbors(start)
nexts = [neighbor for neighbor in neighbors if neighbor != None]
#print(nexts)
#print([data_lines[next[0]][next[1]] for next in nexts])

def get_next(current,before) :
    instruction = data_lines[current[0]][current[1]]
    neighbors = get_pipe_neighbors(current,before)
    if instruction == '|' :
        return (current[0]+1,current[1]) if (current[0]+1,current[1]) in neighbors else (current[0]-1,current[1])
    elif instruction == '-' :
        return (current[0],current[1]+1) if (current[0],current[1]+1) in neighbors else (current[0],current[1]-1)
    elif instruction == 'L' :
        return (current[0],current[1]+1) if (current[0],current[1]+1) in neighbors else (current[0]-1,current[1])
    elif instruction == 'J' :
        return (current[0],current[1]-1) if (current[0],current[1]-1) in neighbors else (current[0]-1,current[1])
    elif instruction == '7' :
        return (current[0]+1,current[1]) if (current[0]+1,current[1]) in neighbors else (current[0],current[1]-1)
    elif instruction == 'F' :
        return (current[0]+1,current[1]) if (current[0]+1,current[1]) in neighbors else (current[0],current[1]+1)
    else :
        return None

loop.append(data_lines[nexts[0][0]][nexts[0][1]])
loop_ind.append(nexts[0])
while loop[-1] != 'S' :
    current = loop_ind[-1]
    before = loop_ind[-2]
    next = get_next(current,before)
    if next != None :
        loop.append(data_lines[next[0]][next[1]])
        loop_ind.append(next)
        #print(loop[-1],next)
    else :
        print('ERROR')
        break

#print(loop)
#print(len(loop))
print('Result = ',int(len(loop)/2))
# Answer is 6768