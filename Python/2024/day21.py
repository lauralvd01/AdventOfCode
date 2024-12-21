# Day 21 - Advent Of Code 2024

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day21_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day21.txt", 'r')

part = 1

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

directions = {'^' : (-1,0), '>' : (0,1), 'v' : (1,0), '<' : (0,-1)}
numerical_positions = {'7' : (0,0), '8' : (0,1), '9' : (0,2), '4' : (1,0), '5' : (1,1), '6' : (1,2), '1' : (2,0), '2' : (2,1), '3' : (2,2), 'X': (3,0), '0' : (3,1), 'A' : (3,2)}

def get_shortest_numerical_path(current, end, numerical_tabloid=None) :
    if numerical_tabloid is None :
        numerical_tabloid = [['7','8','9'],['4','5','6'],['1','2','3'],['X','0','A']]
        
    if current == end :
        return ['A']
    
    i,j = current
    path = []
    for k in directions.keys() :
        di, dj = directions[k]
        if 0 <= i+di < len(numerical_tabloid) and 0 <= j+dj < len(numerical_tabloid[0]) and numerical_tabloid[i+di][j+dj] != 'X' :
            old = numerical_tabloid[i][j]
            numerical_tabloid[i][j] = 'X'
            next_path = get_shortest_numerical_path((i+di,j+dj), end, numerical_tabloid)
            for next in next_path :
                if len(next) == abs(current[0]-end[0]) + abs(current[1]-end[1]) :
                    path.append(k + next)
            numerical_tabloid[i][j] = old
    return path

def robot_to_numerical(code) :
    sequences = ['']
    start_position = numerical_positions['A']
    for button_to_reach in code :
        end_position = numerical_positions[button_to_reach]
        next_paths = get_shortest_numerical_path(start_position, end_position)
        for s in range(len(sequences)) :
            sequence = sequences.pop(0)
            for path in next_paths :
                sequences.append(sequence + path)
        start_position = end_position
    return sequences


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

robot_positions = {'X': (0,0), '^' : (0,1), 'A': (0,2), '<' : (1,0), 'v' : (1,1), '>' : (1,2)}

def get_shortest_robot_path(current, end, robot_tabloid=None) :
    if robot_tabloid is None :
        robot_tabloid = [['X','^','A'],['<','v','>']]
        
    if current == end :
        return ['A']
    
    i,j = current
    path = []
    for k in directions.keys() :
        di, dj = directions[k]
        if 0 <= i+di < len(robot_tabloid) and 0 <= j+dj < len(robot_tabloid[0]) and robot_tabloid[i+di][j+dj] != 'X' :
            old = robot_tabloid[i][j]
            robot_tabloid[i][j] = 'X'
            next_path = get_shortest_numerical_path((i+di,j+dj), end, robot_tabloid)
            for next in next_path :
                if len(next) == abs(current[0]-end[0]) + abs(current[1]-end[1]) :
                    path.append(k + next)
            robot_tabloid[i][j] = old
    return path

def robot_to_robot(code) :
    sequences = ['']
    start_position = robot_positions['A']
    for button_to_reach in code :
        end_position = robot_positions[button_to_reach]
        next_paths = get_shortest_robot_path(start_position, end_position)
        for s in range(len(sequences)) :
            sequence = sequences.pop(0)
            for path in next_paths :
                sequences.append(sequence + path)
        start_position = end_position
    return sequences

def solve(part) :
    global directions
    
    if part == 1 :
        # Part 1
        
        numerical_codes = data_file.read().split('\n')
        data_file.close()
        
        total = 0
        for code in numerical_codes :
            print(code)
            min_lenght = float('inf')
            
            sequences_robot1 = robot_to_numerical(code)
            for s1 in sequences_robot1 :
                sequences_robot2 = robot_to_robot(s1)
                for s2 in sequences_robot2 :
                    sequences_robot3 = robot_to_robot(s2)
                    for s3 in sequences_robot3 :
                        if len(s3) < min_lenght :
                            min_lenght = len(s3)
            print(min_lenght)
            total += min_lenght*int(code[:3])
            print(total)
            
        return total # Answer is 
    
    elif part == 2 :
        # Part 2
        
        total = 0
        return total # Answer is 
    
    else:
        data_file.close()
        return 'Invalid part'

print(solve(part))
