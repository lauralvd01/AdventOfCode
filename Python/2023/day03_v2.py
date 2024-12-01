# Day 3, part 2 of Advent of Code 2023

#data_file = open('../../Data/2023/day03_test1.txt', 'r')

data_file = open('../../Data/2023/day03.txt', 'r')
data_lines = []
for line in data_file:
    data_lines.append(line[:-1])
data_file.close()

CIFERS = ['0','1','2','3','4','5','6','7','8','9']

def get_numbers(line) :
    numbers = []
    i = 0
    while i < len(line) :
        if line[i] in CIFERS :
            start = i
            while i < len(line) :
                if line[i] not in CIFERS :
                    break
                else :
                    i += 1
            numbers.append((line[start:i],start))
        else :
            i += 1
    return numbers

def get_stars(neighbours) :
    stars = []
    for (l,i) in neighbours :
        if data_lines[l][i] == '*' :
            stars.append((l,i))
    return stars

sum = 0

nb_line = 0
numbers_foreach_stars = {}
for line in data_lines :
    numbers = get_numbers(line)
    
    for (number,start) in numbers :
        n = len(number)
        
        neighbours = {}
        if nb_line == 0 :
            if start == 0 :
                neighbours[(nb_line,start+n)] = data_lines[nb_line][start+n]
                for j in range(n+1) :
                    neighbours[(nb_line+1,start+j)] = data_lines[nb_line+1][start+j]
            elif start+n == len(line) :
                neighbours[(nb_line,start-1)] = data_lines[nb_line][start-1]
                for j in range(n+1) :
                    neighbours[(nb_line+1,start-1+j)] = data_lines[nb_line+1][start-1+j]
            else :
                neighbours[(nb_line,start-1)] = data_lines[nb_line][start-1]
                neighbours[(nb_line,start+n)] = data_lines[nb_line][start+n]
                for j in range(n+2) :
                    neighbours[(nb_line+1,start-1+j)] = data_lines[nb_line+1][start-1+j]
        elif nb_line+1 == len(data_lines) :
            if start == 0 :
                neighbours[(nb_line,start+n)] = data_lines[nb_line][start+n]
                for j in range(n+1) :
                    neighbours[(nb_line-1,start+j)] = data_lines[nb_line-1][start+j]
            elif start+n == len(line) :
                neighbours[(nb_line,start-1)] = data_lines[nb_line][start-1]
                for j in range(n+1) :
                    neighbours[(nb_line-1,start-1+j)] = data_lines[nb_line-1][start-1+j]
            else :
                neighbours[(nb_line,start-1)] = data_lines[nb_line][start-1]
                neighbours[(nb_line,start+n)] = data_lines[nb_line][start+n]
                for j in range(n+2) :
                    neighbours[(nb_line-1,start-1+j)] = data_lines[nb_line-1][start-1+j]
        else :
            if start == 0 :
                neighbours[(nb_line,start+n)] = data_lines[nb_line][start+n]
                for j in range(n+1) :
                    neighbours[(nb_line-1,start+j)] = data_lines[nb_line-1][start+j]
                    neighbours[(nb_line+1,start+j)] = data_lines[nb_line+1][start+j]
            elif start+n == len(line) :
                neighbours[(nb_line,start-1)] = data_lines[nb_line][start-1]
                for j in range(n+1) :
                    neighbours[(nb_line-1,start-1+j)] = data_lines[nb_line-1][start-1+j]
                    neighbours[(nb_line+1,start-1+j)] = data_lines[nb_line+1][start-1+j]
            else :
                neighbours[(nb_line,start-1)] = data_lines[nb_line][start-1]
                neighbours[(nb_line,start+n)] = data_lines[nb_line][start+n]
                for j in range(n+2) :
                    neighbours[(nb_line-1,start-1+j)] = data_lines[nb_line-1][start-1+j]
                    neighbours[(nb_line+1,start-1+j)] = data_lines[nb_line+1][start-1+j]
        
        stars = get_stars(neighbours)
        for (l,i) in stars :
            if (l,i) not in numbers_foreach_stars :
                numbers_foreach_stars[(l,i)] = [number]
            else :
                numbers_foreach_stars[(l,i)].append(number)
                sum += int(numbers_foreach_stars[(l,i)][0]) * int(number)
    nb_line += 1

#print(numbers_foreach_stars)
print('Sum = ', sum)
# Answer is 554003