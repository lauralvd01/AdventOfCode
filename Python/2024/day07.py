# Day 7, Advent of Code 2024

import itertools

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day07_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day07.txt", 'r')

part = 2

def evaluate(equation, operators) :
    result = int(equation[0])
    for i in range(1, len(equation)) :
        if operators[i-1] == '0' :
            result += int(equation[i])
        elif operators[i-1] == '1' :
            result *= int(equation[i])
        elif operators[i-1] == '2' :
            result = int(str(result)+equation[i])
    return result

def solve(part):
    if part == 1:
        # PART 1

        equations = []
        for line in data_file :
            parts = line.strip().split(':')
            value = int(parts[0])
            equation = parts[1].strip().split(' ')
            equations.append((value, equation))
        data_file.close()
        
        total = 0
        for equation in equations :
            accepted = False
            n_possibilities = 2 ** (len(equation[1])-1) # 2 possibilities for each operator, 1 operator between each number => 2^(n-1) possibilities
            for i in range(n_possibilities) :
                binaire = bin(i)[2:]
                binaire = '0' * (len(equation[1])-1 - len(binaire)) + binaire # add 0s to the left to have the right length
                result = evaluate(equation[1], binaire) # evaluate the equation with the current operators (0 = +, 1 = *)
                if result == equation[0] :
                    #print(equation[1], binaire, result)
                    accepted = True
                    break
            if accepted :
                total += equation[0]
            
        return total  # Answer is 1545311493300

    elif part == 2:
        # PART 2

        equations = []
        for line in data_file :
            parts = line.strip().split(':')
            value = int(parts[0])
            equation = parts[1].strip().split(' ')
            equations.append((value, equation))
        data_file.close()
        
        total = 0
        for equation in equations :
            accepted = False
            for ops in itertools.product(["0","1","2"], repeat=len(equation[1]) - 1) : # 3 possibilities for each operator, 1 operator between each number => 3^(n-1) possibilities
                result = evaluate(equation[1], ops) # evaluate the equation with the current operators (0 = +, 1 = *, 2 = concatenation)
                if result == equation[0] :
                    #print(equation[1], ops, result)
                    accepted = True
                    break
            if accepted :
                total += equation[0]
            
        return total  # Answer is 169122112716571

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
