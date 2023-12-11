# Day 11, part 1 of Advent of Code 2023

#data_file = open('./Data/day11_test1.txt', 'r')

data_file = open('./Data/day11.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

EXPAND = 1000000-1

empty_rows = []
empty_colums = []
for i in range(len(data_lines)):
    if data_lines[i] == '.'*len(data_lines[i]) :
        empty_rows.append(i)
for j in range(len(data_lines[0])):
    if ''.join([data_lines[i][j] for i in range(len(data_lines))]) == '.'*len(data_lines):
        empty_colums.append(j)

galaxies = []
pairs = []
for i in range(len(data_lines)):
    for j in range(len(data_lines[i])):
        if data_lines[i][j] == '#':
            new = (i+EXPAND*len([row for row in empty_rows if row < i]),j+EXPAND*len([col for col in empty_colums if col < j]))
            #print('i = ',i,' j = ',j,' new = ',new)
            for galaxie in galaxies :
                pairs.append((galaxie,new))
            galaxies.append(new)

#print(galaxies)

result = 0
for pair in pairs :
    #print(pair,' = ',abs(pair[0][0]-pair[1][0]) + abs(pair[0][1]-pair[1][1]))
    result += abs(pair[0][0]-pair[1][0]) + abs(pair[0][1]-pair[1][1])

print('Result = ',result)
# Answer is 406725732046