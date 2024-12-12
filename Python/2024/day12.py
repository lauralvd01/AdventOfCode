# Day 12, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day12_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day12.txt", 'r')

part = 2

def get_neighbors(map, current):
    i, j = current
    neighbors = [-1,-1,-1,-1]
    if i > 0 :
        neighbors[0] = (i-1,j) #UP
    if j < len(map[i])-1 :
        neighbors[1] = (i,j+1) #RIGHT
    if i < len(map)-1 :
        neighbors[2] = (i+1,j) #DOWN
    if j > 0 :
        neighbors[3] = (i,j-1) #LEFT
    return neighbors

def create_region(map, current, region):
    i,j = current
    region["area"] += 1
    map[i][j] += "X"
    neighbors = get_neighbors(map, current)
    d = 0
    for n in neighbors :
        if n == -1 :
            region["perim"] += 1
            region["edges"].append((current, d))
        else :
            if map[n[0]][n[1]][0] != map[i][j][0] :
                region["perim"] += 1
                region["edges"].append((current, d))
            elif len(map[n[0]][n[1]]) == 1 :
                region = create_region(map, n, region)
        d += 1
    return region

def count_sides(edges) :
    count = 0
    while len(edges) >= 1 :
        current = edges.pop(0)
        i,j = current[0]
        direction = current[1]
        count += 1 # Count the delimitation of the region at current plant in that direction
        
        # Then remove other edges that build the same side, pointing to the same direction, to avoid counting this side again
        # Edges that build the same side are either in direction +1 or -1 (modulo 4)
        direction_moves = [(-1,0),(0,1),(1,0),(0,-1)] # Moving UP, RIGHT, DOWN, LEFT
        
        right_next_edge = (i + direction_moves[(direction+1)%4][0], j + direction_moves[(direction+1)%4][1])
        while (right_next_edge,direction) in edges :
            edges.remove((right_next_edge,direction))
            right_next_edge = (right_next_edge[0] + direction_moves[(direction+1)%4][0], right_next_edge[1] + direction_moves[(direction+1)%4][1])
            
        left_next_edge = (i + direction_moves[(direction-1)%4][0], j + direction_moves[(direction-1)%4][1])
        while (left_next_edge,direction) in edges :
            edges.remove((left_next_edge,direction))
            left_next_edge = (left_next_edge[0] + direction_moves[(direction-1)%4][0], left_next_edge[1] + direction_moves[(direction-1)%4][1])
        
    return count

def solve(part):
    if part == 1:
        # PART 1

        map = []
        plants = {}
        i = 0
        for line in data_file:
            s = []
            j = 0
            for c in line.strip() :
                s.append(c)
                if c not in plants.keys() :
                    plants[c] = [(i,j)]
                else :
                    plants[c].append((i,j))
                j += 1
            map.append(s)
            i += 1
        data_file.close()
        
        regions = []
        for type_of_plant in plants.keys() :
            for i,j in plants[type_of_plant] :
                if map[i][j] == type_of_plant :
                    region = create_region(map, (i,j), {"area": 0, "perim": 0, "edges": []})
                    regions.append(region)
        
        total = 0
        for region in regions :
            total += region["area"] * region["perim"]
        return total  # Answer is 1449902

    elif part == 2:
        # PART 2
        
        map = []
        plants = {}
        i = 0
        for line in data_file:
            s = []
            j = 0
            for c in line.strip() :
                s.append(c)
                if c not in plants.keys() :
                    plants[c] = [(i,j)]
                else :
                    plants[c].append((i,j))
                j += 1
            map.append(s)
            i += 1
        data_file.close()
        
        regions = []
        for type_of_plant in plants.keys() :
            for i,j in plants[type_of_plant] :
                if map[i][j] == type_of_plant :
                    region = create_region(map, (i,j), {"area": 0, "perim": 0, "edges": []})
                    regions.append(region)
        
        total = 0
        for region in regions :
            sides = count_sides(region["edges"])
            total += region["area"] * sides
        return total  # Answer is 908042

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
