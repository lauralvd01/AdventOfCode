# Day 18, Advent of Code 2024

import re

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day18_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day18.txt", 'r')

part = 2

def get_neighbors(i, j, map) :
    neighbors = []
    for di, dj in [(-1,0), (0,1), (1,0), (0,-1)] : # UP, RIGHT, DOWN, LEFT
        if 0 <= i + di < len(map) and 0 <= j + dj < len(map[0]) and map[i + di][j + dj] != '#' :
            neighbors.append((i + di, j + dj))
    return neighbors

def solve(part):
    
    if part == 1:
        # PART 1
                
        start = 0, 0
        # end = 6, 6
        end = 70, 70
        
        map = [['.' for j in range(end[1]+1)] for i in range(end[0]+1)]
        
        pattern = re.compile("(\d+),(\d+)")
        
        count_bytes = 0
        for line in data_file :
            match = pattern.match(line)
            x, y = int(match.group(1)), int(match.group(2))
            map[y][x] = '#'
            count_bytes += 1
            if count_bytes == 1024 :
                break
        data_file.close()
        
        print('\n'.join([''.join(row) for row in map]))
        
        total = float('inf')
        steps = {start : 0}  # steps[(i, j)] : min_scmin_steps to reach (i, j)
        to_visit = [start]
        while len(to_visit) > 0 :
            i, j = to_visit.pop(0)
            number_steps = steps[(i, j)]
            
            neighbors = get_neighbors(i, j, map)
            for neighbor in neighbors :
                if neighbor == end :
                    total = min(total, number_steps+1)
                else :
                    if neighbor not in steps or steps[neighbor] > number_steps + 1 :
                        steps[neighbor] = number_steps + 1
                        to_visit.append(neighbor)

        return total  # Answer is 226
    
    elif part == 2:
        # PART 2
        
        start = 0, 0
        # end = 6, 6
        end = 70, 70
        
        map = [['.' for j in range(end[1]+1)] for i in range(end[0]+1)]
        
        pattern = re.compile("(\d+),(\d+)")
        
        count_bytes = 0
        next_bytes = []
        for line in data_file :
            match = pattern.match(line)
            x, y = int(match.group(1)), int(match.group(2))
            
            if count_bytes < 1024 :
                map[y][x] = '#'
                count_bytes += 1
            else :
                next_bytes.append((x, y))
        data_file.close()
        
        print('\n'.join([''.join(row) for row in map]))
        
        next = 0
        # total = 22
        total = 226
        while next < len(next_bytes) and total < float('inf') :
            map[next_bytes[next][1]][next_bytes[next][0]] = '#'
            next += 1
            
            total = float('inf')
            steps = {start : 0}
            to_visit = [start]
            while len(to_visit) > 0 :
                i, j = to_visit.pop(0)
                number_steps = steps[(i, j)]
                map[i][j] = '0'
                
                neighbors = get_neighbors(i, j, map)
                for neighbor in neighbors :
                    if neighbor == end :
                        total = min(total, number_steps+1)
                    else :
                        if neighbor not in steps or steps[neighbor] > number_steps + 1 :
                            steps[neighbor] = number_steps + 1
                            to_visit.append(neighbor)

        return next_bytes[next-1]  # Answer is 60,46
    
    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
