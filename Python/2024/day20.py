# Day 20 - Advent Of Code 2024

data_file = open("day20.txt","r")

part = 1

def get_path(current, map) :
    i,j = current
    if map[i][j] == 'E' :
        map[i][j] = 'O'
        return [current]
    
    for di, dj in [(-1,0), (0,1), (1,0), (0,-1)] :
        if 1 <= i+di < len(map)-1 and 1 <= j+dj < len(map[0])-1 and map[i+di][j+dj] != '#' and map[i+di][j+dj] != 'X' :
            map[i][j] = 'X'
            next = get_path((i+di,j+dj), map)
            if next is not None :
                map[i][j] = 'O'
                return [current] + next
    map[i][j] = 'X'
    return None

def solve(part) :
    if part == 1 :
        # Part 1
        
        map = []
        start = None
        end = None
        i = 0
        for line in data_file :
            row = []
            j = 0
            for cell in line.strip() :
                row.append(cell)
                if cell == 'S' :
                    start = (i,j)
                if cell == 'E' :
                    end = (i,j)
                j += 1 
            map.append(row)
            i += 1 
        #print('\n'.join([''.join(row) for row in map]))
        print(start)
        print(end)
        
        path = get_path(start, map)
        print(len(path))
        print('\n'.join([''.join(row) for row in map]))
        print()
        
        cheats = {}
        without_cheat = len(path)
        index1 = 0
        for step in path :
            i,j = step
            for di, dj in [(-1,0), (0,1), (1,0), (0,-1)] :
                if 1 <= i+di < len(map)-1 and 1 <= j+dj < len(map[0])-1 and map[i+di][j+dj] == '#' :
                    try :
                        index2 = path.index((i+2*di,j+2*dj))
                    
                        #map[i+di][j+dj] = '1'
                        #map[i+2*di][j+2*dj] = '2'
                        #print('\n'.join([''.join(row) for row in map]))
                        #map[i+di][j+dj] = 'O'
                        #map[i+2*di][j+2*dj] = 'O'
                        
                        picoseconds_saved = without_cheat - (len(path[:index1]) + len(path[index2:])) -2
                        if picoseconds_saved in cheats.keys() :
                            cheats[picoseconds_saved] += 1 
                        else :
                            cheats[picoseconds_saved] = 1
                    except Exception :
                        pass
            index1 += 1
        
        total = 0
        for cheat in cheats.keys() :
            if cheat >= 100 :
                total += cheats[cheat]
        return total

print(solve(part))
