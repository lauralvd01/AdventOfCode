# Day 9, part 2 of Advent of Code 2023

#data_file = open('./Data/2023/day09_test1.txt', 'r')

data_file = open('./Data/2023/day09.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

def next(history) :
    if len(history) == 2 :
        return history[0][0] - history[1][0]
    else :
        history[-2][0] = history[-2][0] - history[-1][0]
        return next(history[:-1])

result = 0
#predictions = []
for line in data_lines :
    history = [[int(num) for num in line.split(' ') if num != '']]
    i = 0
    while history[i] != [0 for i in range(len(history[i]))] :
        sub = []
        for j in range(len(history[i])-1) :
            sub.append(history[i][j+1] - history[i][j])
        history.append(sub)
        i += 1
    #print(history)
    pred = next(history)
    #predictions.append(pred)
    result += pred
#print(predictions)

print('Result = ',result)
# Answer is 928