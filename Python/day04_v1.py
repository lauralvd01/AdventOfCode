# Day 4, part 1 of Advent of Code 2023

#data_file = open('../Data/day04_test1.txt', 'r')

data_file = open('../Data/day04.txt', 'r')
data_lines = []
for line in data_file:
    data = line[:-1].split(':')
    data_lines.append(data[1])
data_file.close()


sum = 0

for line in data_lines :
    parts = line.split('|')
    win_numbers = [number for number in parts[0].split(' ') if number != '']
    play_numbers = [number for number in parts[1].split(' ') if number != '' and number in win_numbers]
    
    if len(play_numbers) > 0 :
        sum += pow(2, len(play_numbers) - 1)

print('Sum = ', sum)
# Answer is 20117