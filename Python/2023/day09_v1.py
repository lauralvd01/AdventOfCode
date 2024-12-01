# Day 9, part 1 of Advent of Code 2023

#data_file = open('./Data/2023/day09_test1.txt', 'r')

data_file = open('./Data/2023/day09.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

result = 0
#predictions = []
for line in data_lines :
    history = [[int(num) for num in line.split(' ') if num != '']]
    next = history[0][-1]
    i = 0
    while history[i] != [0 for i in range(len(history[i]))] :
        sub = []
        for j in range(len(history[i])-1) :
            sub.append(history[i][j+1] - history[i][j])
        history.append(sub)
        next += sub[-1]
        i += 1
    #print(history)
    #predictions.append(next)
    result += next
#print(predictions)

print('Result = ',result)
# Answer is 1974232246