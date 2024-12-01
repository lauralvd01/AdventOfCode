# Day 21, part 1 of Advent of Code 2023

data_file = open('./Data/2023/day21_test1.txt', 'r')

#data_file = open('./Data/2023/day21.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

HEIGHT = len(data_lines)
WIDHT = len(data_lines[0])
map = [[['.',False] for j in range(WIDHT)] for i in range(HEIGHT)]
for i in range(HEIGHT):
    for j in range(WIDHT):
        if data_lines[i][j] == 'S' :
            start_S = (i,j)
            map[i][j][1] = True
        if  data_lines[i][j] == '#' :
            map[i][j][0] = '#'

def get_neighbors(i,j) :
    neighbors = []
    if i > 0 :
        neighbors.append((i-1,j))
    if i < HEIGHT-1 :
        neighbors.append((i+1,j))
    if j > 0 :
        neighbors.append((i,j-1))
    if j < WIDHT-1 :
        neighbors.append((i,j+1))
    return neighbors

data = {}
step = 0
data[start_S] = {step : [start_S]}
# data = dict( keys = (i,j), values = 
#              dict( keys = step, values = list of positions reached in {step} steps ) )

next = []
for start in data.keys() :
    if step in data[start].keys() :
        for dest in data[start][step] :
            if dest not in next :
                next.append(dest)

#max_step = 64
max_step = 1
while step < max_step :
    step += 1
    print(step)
    current = next.copy()
    next = []
    while len(current) > 0 :
        (i,j) = current[0]
        map[i][j][1] = False
        data[(i,j)][step] = []
        neighbors = get_neighbors(i,j)
        for neighbor in neighbors :
            if map[neighbor[0]][neighbor[1]][0] != '#' :
                map[neighbor[0]][neighbor[1]][1] = True
                next.append(neighbor)
        current.pop(0)







#max_step = 64
max_step = 1
while step < max_step :
    step += 1
    print(step)
    current = next.copy()
    next = []
    while len(current) > 0 :
        (i,j) = current[0]
        map[i][j][1] = False
        neighbors = get_neighbors(i,j)
        for neighbor in neighbors :
            if map[neighbor[0]][neighbor[1]][0] != '#' :
                map[neighbor[0]][neighbor[1]][1] = True
                next.append(neighbor)
        current.pop(0)

file = open('./Data/2023/day21_test1_result.txt', 'w')
#file = open('./Data/2023/day21_result.txt', 'w')
file.write('\n'.join([''.join(['O' if map[i][j][1] else map[i][j][0] for j in range(WIDHT)]) for i in range(HEIGHT)]))
file.close()

print(f'\nResult = {sum(map[i][j][1] for i in range(HEIGHT) for j in range(WIDHT))}')
# Answer is 825167435
