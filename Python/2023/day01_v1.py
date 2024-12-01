# Day 1, part 1 of Advent of Code 2023

#data_file = open('../../Data/2023/day01_test1.txt', 'r')

data_file = open('../../Data/2023/day01.txt', 'r')
data_lines = []
for line in data_file:
    data_lines.append(line)
data_file.close()

cifers = ['0','1','2','3','4','5','6','7','8','9']
sum = 0

for line in data_lines :
    start = 0
    end = len(line)-1
    while start < len(line) :
        if line[start] in cifers :
            break
        else :
            start += 1
    while end >= 0 :
        if line[end] in cifers :
            break
        else :
            end -= 1

    if start <= end :
        line = int(line[start]+line[end])
        sum += line
    else :
        print('Error at line : ', line)

print('Sum = ', sum)
# Answer is 53194