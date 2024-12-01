# Day 1, part 2 of Advent of Code 2023

#data_file = open('../../Data/2023/day01_test2.txt', 'r')

data_file = open('../../Data/2023/day01.txt', 'r')
data_lines = []
for line in data_file:
    data_lines.append(line)
data_file.close()

cifers = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
sum = 0

for line in data_lines :
    start = 0
    first = ''
    end = len(line)-1
    second = ''
    while start < len(line) :
        if line[start] in cifers.values() :
            first = line[start]
            break
        else :
            if line[start:min(start+5,len(line))] in cifers.keys() :
                first = cifers[line[start:min(start+5,len(line))]]
                break
            elif line[start:min(start+4,len(line))] in cifers.keys() :
                first = cifers[line[start:min(start+4,len(line))]]
                break
            elif line[start:min(start+3,len(line))] in cifers.keys() :
                first = cifers[line[start:min(start+3,len(line))]]
                break
            start += 1
    while end >= 0 :
        if line[end] in cifers.values() :
            second = line[end]
            break
        else :
            if line[max(end-4,0):end+1] in cifers.keys() :
                second = cifers[line[max(end-4,0):end+1]]
                break
            elif line[max(end-3,0):end+1] in cifers.keys() :
                second = cifers[line[max(end-3,0):end+1]]
                break
            elif line[max(end-2,0):end+1] in cifers.keys() :
                second = cifers[line[max(end-2,0):end+1]]
                break
            end -= 1

    if start <= end :
        line = int(first+second)
        sum += line
    else :
        print('Error at line : ', line)

print('Sum = ', sum)
# Answer is 54249