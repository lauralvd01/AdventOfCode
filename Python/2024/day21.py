# Day 21 - Advent Of Code 2024

from itertools import permutations

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day21_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day21.txt", 'r')

part = 2

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

############################################################################################### # PART 2

def robot_to_numerical_2(code) :
    numerical_tabloid = [['7','8','9'],['4','5','6'],['1','2','3'],['X','0','A']]
    sequences = []
    start_position = numerical_positions['A']
    for button_to_reach in code :
        sequences.append([])
        
        end_position = numerical_positions[button_to_reach]
        di, dj = end_position[0]-start_position[0], end_position[1]-start_position[1]
        sequence = ('v'*di if di >= 0 else '^'*abs(di)) + ('>'*dj if dj >= 0 else '<'*abs(dj))
        
        for seq in permutations(sequence) :
            if (''.join(seq)+'A') not in sequences[-1] :
                current = start_position
                for s in seq :
                    if s == '^' :
                        current = (current[0]-1,current[1])
                    if s == 'v' :
                        current = (current[0]+1,current[1])
                    if s == '>' :
                        current = (current[0],current[1]+1)
                    if s == '<' :
                        current = (current[0],current[1]-1)
                    if not (0 <= current[0] < len(numerical_tabloid) and 0 <= current[1] < len(numerical_tabloid[1])) or numerical_tabloid[current[0]][current[1]] == 'X' :
                        break
                if current == end_position :
                    sequences[-1].append(''.join(seq)+'A')
                    
        start_position = end_position
    return sequences

def robot_to_robot_2(code) :
    robot_tabloid = [['X','^','A'],['<','v','>']]
    sequences = []
    start_position = robot_positions['A']
    for button_to_reach in code :
        sequences.append([])
        
        end_position = robot_positions[button_to_reach]
        di, dj = end_position[0]-start_position[0], end_position[1]-start_position[1]
        sequence = ('v'*di if di >= 0 else '^'*abs(di)) + ('>'*dj if dj >= 0 else '<'*abs(dj))
        
        for seq in permutations(sequence) :
            if (''.join(seq)+'A') not in sequences[-1] :
                current = start_position
                for s in seq :
                    if s == '^' :
                        current = (current[0]-1,current[1])
                    if s == 'v' :
                        current = (current[0]+1,current[1])
                    if s == '>' :
                        current = (current[0],current[1]+1)
                    if s == '<' :
                        current = (current[0],current[1]-1)
                    if not (0 <= current[0] < len(robot_tabloid) and 0 <= current[1] < len(robot_tabloid[1])) or robot_tabloid[current[0]][current[1]] == 'X' :
                        break
                if current == end_position :
                    sequences[-1].append(''.join(seq)+'A')
                    
        start_position = end_position
    return sequences

def count(step_to_perform, robot_repetitions) :
    # step_to_perform = [ possible paths to perform one step of the numerical code or previous robot sequence ]
    # robot_repetitions = number of robots to perform the code or previous robot sequence
    
    counts = [] # [ moves count for each possible path for this step ]
    for sequence in step_to_perform :
        # sequence = one possible path to perform this step
        possible_paths_by_sequence_step = robot_to_robot_2(sequence)
        # [ [ possible robot paths for sequence[0] ], [ possible robot paths for sequence[1] ], ... ]
        
        min_counts = [] # [ min last robot moves count to perform sequence[i] ]
        for sequence_step in possible_paths_by_sequence_step :
            # sequence_step = [ possible robot paths for sequence[i] ]
            if robot_repetitions == 1 :
                # Last robot to perform the sequence
                min_counts.append(min([len(path) for path in sequence_step]))
            else :
                # More robots to perform the sequence
                min_counts.append(count(sequence_step, robot_repetitions-1))
        counts.append(sum(min_counts))
    return min(counts) # Minimum last robot moves count to perform this step

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

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
            
        return total # Answer is 94426
    
    elif part == 2 :
        # Part 2
        
        numerical_codes = data_file.read().split('\n')
        data_file.close()
        
        total = 0
        for code in numerical_codes :
            print(code)
            possible_sequences_by_step = robot_to_numerical_2(code)
            # [ [ possible robot paths for code[0] ], [ possible robot paths for code[1] ], ... ]
            
            counts = [count(step,25) for step in possible_sequences_by_step]
            print(sum(counts))
            total += sum(counts)*int(code[:3])
            print(total)
            print()
        
        return total # Answer is 
    
    else:
        data_file.close()
        return 'Invalid part'

print(solve(part))
