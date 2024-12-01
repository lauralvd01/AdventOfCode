# Day 3, part 1 of Advent of Code 2023

#data_file = open('../../Data/2023/day03_test1.txt', 'r')

data_file = open('../../Data/2023/day03.txt', 'r')
data_lines = []
for line in data_file:
    #print(line[:-1])
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

def get_symbol(neighbours) :
    for (l,i) in neighbours :
        if data_lines[l][i] not in CIFERS and data_lines[l][i] != '.' :
            return True
    return False

sum = 0

nb_line = 0
numbers_infos = {}
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
        #if nb_line == 119 : 
        #    print(nb_line, ' : ', number, ' : ', neighbours)
        
        if get_symbol(neighbours) :
            #print(nb_line, ' : ', number, ' : ', neighbours)
            #print('Symbol found')
            sum += int(number) 
        #else :
            #print(nb_line, ' : ', number)
            #print('Symbol not found')
    nb_line += 1

print('Sum = ', sum)
# Answer is 554003