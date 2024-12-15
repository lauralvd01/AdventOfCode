# Day 15, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day15_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day15.txt", 'r')

part = 2

directions = {"^": (-1,0), ">" : (0,1), "v" :(1,0), "<" : (0,-1)} # UP, RIGHT, DOWN, LEFT

def get_to_move1(robot, move, map, foods) :
    i,j = robot
    next_i, next_j = i+move[0], j+move[1]
    if 0 < next_i < len(map)-1 and 0 < next_j < len(map[0])-1 :
        if map[next_i][next_j] == '#' :
            return robot
        if map[next_i][next_j] == '.' :
            return (next_i, next_j)
        if map[next_i][next_j] == 'O' :
            result = get_to_move1((next_i, next_j), move, map, foods)
            if result == (next_i+move[0], next_j+move[1]) :
                map[next_i][next_j] = '.'
                foods.remove((next_i, next_j))
                map[next_i+move[0]][next_j+move[1]] = 'O'
                foods.append((next_i+move[0], next_j+move[1]))
                return (next_i, next_j)
    return robot

def can_move_forward(robot, move, map) :
    i,j = robot
    next_i, next_j = i+move[0], j+move[1]
    if 0 < next_i < len(map)-1 and 1 < next_j < len(map[0])-2 :
        if map[next_i][next_j] == '#' :
            return False
        if map[next_i][next_j] == '.' :
            return True
        if move == (0,-1) or move == (0,1) :
            return can_move_forward((next_i, next_j), move, map)
        if map[next_i][next_j] == '[' :
            return can_move_forward((next_i, next_j), move, map) and can_move_forward((next_i, next_j+1), move, map)
        if map[next_i][next_j] == ']' :
            return can_move_forward((next_i, next_j-1), move, map) and can_move_forward((next_i, next_j), move, map)
    return False

def get_to_move2(robot, move, map) :
    i,j = robot
    next_i, next_j = i+move[0], j+move[1]
    if 0 < next_i < len(map)-1 and 1 < next_j < len(map[0])-2 :
        if map[next_i][next_j] == '#' :
            return robot
        
        if map[next_i][next_j] == '.' :
            return (next_i, next_j)
        
        if move == (0,-1) or move == (0,1) : # LEFT and RIGHT moves don't change
            result = get_to_move2((next_i, next_j), move, map)
            if result == (next_i+move[0], next_j+move[1]) :
                map[next_i+move[0]][next_j+move[1]] = map[next_i][next_j]
                map[next_i][next_j] = '.'
                return (next_i, next_j)
            
        if move == (-1,0) or move == (1,0) : # UP and DOWN update as it may concern more than 1 column
            if map[next_i][next_j] == '[' :
                result_left = get_to_move2((next_i, next_j), move, map)
                result_right = get_to_move2((next_i, next_j+1), move, map)
                if result_left == (next_i+move[0], next_j+move[1]) and result_right == (next_i+move[0], next_j+move[1]+1) :
                    map[next_i+move[0]][next_j+move[1]] = '['
                    map[next_i+move[0]][next_j+move[1]+1] =']'
                    map[next_i][next_j] = '.'
                    map[next_i][next_j+1] = '.'
                    return (next_i, next_j)
            if map[next_i][next_j] == ']' :
                result_left = get_to_move2((next_i, next_j-1), move, map)
                result_right = get_to_move2((next_i, next_j), move, map)
                if result_left == (next_i+move[0], next_j+move[1]-1) and result_right == (next_i+move[0], next_j+move[1]) :
                    map[next_i+move[0]][next_j+move[1]-1] = '['
                    map[next_i+move[0]][next_j+move[1]] =']'
                    map[next_i][next_j-1] = '.'
                    map[next_i][next_j] = '.'
                    return (next_i, next_j)
                
    return robot

def solve(part):
    if part == 1:
        # PART 1

        data = data_file.read().split('\n\n')
        data_file.close()
        
        map = []
        robot = None
        foods = []
        i = 0
        for line in data[0].split('\n') :
            row = []
            j = 0
            for cell in line.strip() :
                row.append(cell)
                if cell == 'O' :
                    foods.append((i,j))
                if cell == '@' :
                    robot = (i,j)
                j += 1
            map.append(row)
            i += 1
            
        print('\n'.join([''.join(row) for row in map]))
        
        moves = []
        for line in data[1].split('\n') :
            for cell in line.strip() :
                moves.append(directions[cell])
        
        for move in moves :
            map[robot[0]][robot[1]] = '.'
            robot = get_to_move1(robot, move, map, foods)
            map[robot[0]][robot[1]] = '@'
        print('\n'.join([''.join(row) for row in map]))
        
        total = 0
        for food in foods :
            total += food[0]*100 + food[1]
        return total  # Answer is 1349898

    elif part == 2:
        # PART 2
        
        data = data_file.read().split('\n\n')
        data_file.close()
        
        map = []
        robot = None
        i = 0
        for line in data[0].split('\n') :
            row = []
            j = 0
            for cell in line.strip() :
                if cell == '#' :
                    row.append('#')
                    row.append('#')
                if cell == '.' :
                    row.append('.')
                    row.append('.')
                if cell == 'O' :
                    row.append('[')
                    row.append(']')
                if cell == '@' :
                    row.append('@')
                    row.append('.')
                    robot = (i,j*2)
                j += 1
            map.append(row)
            i += 1
            
        print('\n'.join([''.join(row) for row in map]))
        
        moves = []
        for line in data[1].split('\n') :
            for cell in line.strip() :
                moves.append(directions[cell])
        
        for move in moves :
            if can_move_forward(robot, move, map) :
                map[robot[0]][robot[1]] = '.'
                robot = get_to_move2(robot, move, map)
                map[robot[0]][robot[1]] = '@'
        print()
        print('\n'.join([''.join(row) for row in map]))
        
        total = 0
        i = 1
        while i < len(map)-1 :
            j = 2
            while j < len(map[0])-2 :
                if map[i][j] == '[' :
                    total += i*100 + j
                j += 1
            i += 1
        return total  # Answer is 1376686
    
    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
