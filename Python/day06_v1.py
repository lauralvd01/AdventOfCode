# Day 6, part 1 of Advent of Code 2023

#data_file = open('../Data/day06_test1.txt', 'r')

data_file = open('../Data/day06.txt', 'r')

data_lines = [line[9:-1] for line in data_file]
data_file.close()

records = [[int(num) for num in line.split(' ') if num != ''] for line in data_lines]

result = 1
for i in range(len(records[0])) :
    ways_of_win = 0
    race_duration = records[0][i]
    
    for hold_time in range(1,race_duration) :
        speed = hold_time
        distance = speed*(race_duration-hold_time)
        if distance > records[1][i] :
            ways_of_win += 1
    
    result *= ways_of_win

print('Result = ',result)
# Answer is 861300