# Day 6, part 2 of Advent of Code 2023

#data_file = open('./Data/2023/day06_test1.txt', 'r')

data_file = open('./Data/2023/day06.txt', 'r')

data_lines = [line[9:-1].replace(" ","") for line in data_file]
data_file.close()

records = [int(line) for line in data_lines]

ways_of_win = 0
race_duration = records[0]
    
for hold_time in range(1,race_duration) :
    speed = hold_time
    distance = speed*(race_duration-hold_time)
    if distance > records[1] :
        ways_of_win += 1

print('Result = ',ways_of_win)
# Answer is 28101347