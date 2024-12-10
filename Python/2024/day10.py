# Day 10, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day10_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day10.txt", 'r')

part = 2

def get_neighbors(map, current):
    i, j = current
    step = int(map[i][j])
    neighbors = []
    if i > 0 and int(map[i-1][j]) == step + 1 :
        neighbors.append((i-1,j)) #UP
    if j < len(map[i])-1 and int(map[i][j+1]) == step + 1 :
        neighbors.append((i,j+1)) #RIGHT
    if i < len(map)-1 and int(map[i+1][j]) == step + 1 :
        neighbors.append((i+1,j)) #DOWN
    if j > 0 and int(map[i][j-1]) == step + 1 :
        neighbors.append((i,j-1)) #LEFT
    return neighbors

def solve(part):
    if part == 1:
        # PART 1

        map = []
        trailheads = {}
        i = 0
        for line in data_file:
            s = []
            j = 0
            for c in line.strip() :
                s.append(c)
                if int(c) == 0 :
                    trailheads[(i, j)] = 0
                j += 1
            map.append(s)
            i += 1
        data_file.close()
        
        for trailhead in trailheads.keys() :
            current = trailhead
            possibilities = get_neighbors(map, current)
            ends = []
            while possibilities != [] :
                current = possibilities.pop()
                if map[current[0]][current[1]] == '9' :
                    if current not in ends :
                        ends.append(current)
                possibilities += get_neighbors(map, current)
            trailheads[trailhead] = len(ends)
        
        total = 0
        for trailhead in trailheads.keys() :
            total += trailheads[trailhead]
        return total  # Answer is 688

    elif part == 2:
        # PART 2

        map = []
        trailheads = {}
        i = 0
        for line in data_file:
            s = []
            j = 0
            for c in line.strip() :
                s.append(c)
                if int(c) == 0 :
                    trailheads[(i, j)] = None
                j += 1
            map.append(s)
            i += 1
        data_file.close()
        
        for trailhead in trailheads.keys() :
            current = trailhead
            possibilities = get_neighbors(map, current)
            ends = {}
            while possibilities != [] :
                current = possibilities.pop()
                if map[current[0]][current[1]] == '9' :
                    if current not in ends.keys() :
                        ends[current] = 1
                    else :
                        ends[current] += 1
                possibilities += get_neighbors(map, current)
            trailheads[trailhead] = sum([ends[i] for i in ends.keys()])
        
        total = 0
        for trailhead in trailheads.keys() :
            total += trailheads[trailhead]
        return total  # Answer is 1459

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
