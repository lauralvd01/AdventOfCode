# Day 2, part 1 of Advent of Code 2023

#data_file = open('../Data/day02_test1.txt', 'r')

data_file = open('../Data/day02.txt', 'r')
data_lines = []
for line in data_file:
    data_lines.append(line)
data_file.close()

colors = {'red':12, 'green':13, 'blue':14}
sum = 0

for line in data_lines :
    line = line.split('\n')[0]
    game = line.split(':')
    nbr = int(game[0][5:])
    max_red = -1
    max_green = -1
    max_blue = -1
    
    parts = game[1].split(';')
    for part in parts :
        packs = part.split(',')
        for pack in packs :
            info = pack.split(' ')
            #print(info)
            if info[2] == 'red' :
                max_red = max(max_red, int(info[1]))
            elif info[2] == 'green' :
                max_green = max(max_green, int(info[1]))
            elif info[2] == 'blue' :
                max_blue = max(max_blue, int(info[1]))
        #print('Max red = ', max_red, 'Max green = ', max_green, 'Max blue = ', max_blue)
    if max_red <= colors['red'] and max_green <= colors['green'] and max_blue <= colors['blue'] :
        #print(line)
        sum += nbr
        
print('Sum = ', sum)
# Answer is 2162