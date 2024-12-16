# Day 16, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day16_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day16.txt", 'r')

part = 2

directions = [(-1,0),(0,1),(1,0),(0,-1)] # UP, RIGHT, DOWN, LEFT
# Turn clockwise : new_direction = (direction + 1) % 4
# Turn counter-clockwise : new_direction = (direction - 1) % 4


def solve(part):
    if part == 1:
        # PART 1

        map = []
        for line in data_file :
            map.append([cell for cell in line.strip()])
        data_file.close()
        
        S = len(map)-2, 1       # Start at left bottom corner facing east (right = directions[1])
        E = 1, len(map[0])-2    # End at right top corner
        
        total = float('inf')
        scores = {(S, 1) : 0}  # (i, j, direction) : min_score to reach (i, j) facing this direction
        to_visit = [(S,1)]
        while len(to_visit) > 0 :
            step = to_visit.pop(0)
            score = scores[step]
            i, j = step[0]
            direction = step[1]
            move = directions[direction]
            
            if map[i+move[0]][j+move[1]] == 'E' : # END
                new_score = score + 1
                total = min(total, new_score)
            else :
                if map[i+move[0]][j+move[1]] != '#' : # Move forward, increasing score by 1
                    new_step = ((i+move[0], j+move[1]), direction)
                    new_score = score + 1
                    if new_step not in scores or scores[new_step] > new_score :
                        scores[new_step] = new_score
                        to_visit.append(new_step)
                
                new_direction = (direction + 1) % 4 # Turn clockwise
                new_step = ((i, j), new_direction)
                new_score = score + 1000
                if new_step not in scores or scores[new_step] > new_score :
                    scores[new_step] = new_score
                    to_visit.append(new_step)
                    
                new_direction = (direction - 1) % 4 # Turn counter-clockwise
                new_step = ((i, j), new_direction)
                new_score = score + 1000
                if new_step not in scores or scores[new_step] > new_score :
                    scores[new_step] = new_score
                    to_visit.append(new_step)
                
        return total  # Answer is 104516

    elif part == 2:
        # PART 2
        
        map = []
        for line in data_file :
            map.append([cell for cell in line.strip()])
        data_file.close()
        
        S = len(map)-2, 1       # Start at left bottom corner facing east (right = directions[1])
        E = 1, len(map[0])-2    # End at right top corner
        
        # min_score = 7036 # First example
        # min_score = 11048 # Second example
        min_score = 104516 # Puzzle input
        total = 0
        scores = {(S, 1) : (0,[S])}  # (i, j, direction) : min_score to reach (i, j) facing this direction
        to_visit = [(S,1)]
        while len(to_visit) > 0 :
            step = to_visit.pop(0)
            score = scores[step][0]
            former_steps = scores[step][1]
            i, j = step[0]
            direction = step[1]
            move = directions[direction]
            
            if map[i+move[0]][j+move[1]] == 'E' : # END
                new_score = score + 1
                if new_score <= min_score :
                    min_score = new_score
                    print(min_score)
                    for cell in former_steps :
                        if cell != S and cell != E and map[cell[0]][cell[1]] != 'O' :
                            map[cell[0]][cell[1]] = 'O'
                            total += 1
            else :
                if map[i+move[0]][j+move[1]] != '#' : # Move forward, increasing score by 1
                    new_step = ((i+move[0], j+move[1]), direction)
                    new_score = score + 1
                    if new_step not in scores or scores[new_step][0] > new_score :
                        scores[new_step] = (new_score,former_steps+[new_step[0]])
                        to_visit.append(new_step)
                    elif new_step in scores and scores[new_step][0] == new_score :
                        scores[new_step] = (new_score,scores[new_step][1]+former_steps+[new_step[0]])
                
                new_direction = (direction + 1) % 4 # Turn clockwise
                new_step = ((i, j), new_direction)
                new_score = score + 1000
                if new_step not in scores or scores[new_step][0] > new_score :
                    scores[new_step] = (new_score,former_steps)
                    to_visit.append(new_step)
                elif new_step in scores and scores[new_step][0] == new_score :
                    scores[new_step] = (new_score,scores[new_step][1]+former_steps+[new_step[0]])
                    
                new_direction = (direction - 1) % 4 # Turn counter-clockwise
                new_step = ((i, j), new_direction)
                new_score = score + 1000
                if new_step not in scores or scores[new_step][0] > new_score :
                    scores[new_step] = (new_score,former_steps)
                    to_visit.append(new_step)
                elif new_step in scores and scores[new_step][0] == new_score :
                    scores[new_step] = (new_score,scores[new_step][1]+former_steps+[new_step[0]])
        
        print('\n'.join([''.join(line) for line in map]))
        return total+2  # Answer is 545
    
    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
