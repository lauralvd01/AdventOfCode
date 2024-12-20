# Day 20 - Advent Of Code 2024

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day20_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day20.txt", 'r')


part = 1

def get_path_recursion(current, map) :
    print()
    print('\n'.join([''.join(row) for row in map]))
    i,j = current
    
    if map[i][j] == 'E' :
        map[i][j] = 'O'
        return [current]
    
    for di, dj in [(-1,0), (0,1), (1,0), (0,-1)] :
        if 1 <= i+di < len(map)-1 and 1 <= j+dj < len(map[0])-1 and map[i+di][j+dj] != '#' and map[i+di][j+dj] != 'X' :
            map[i][j] = 'X'
            next = get_path_recursion((i+di,j+dj), map)
            if next is not None :
                map[i][j] = 'O'
                return [current] + next
    map[i][j] = 'X'
    return None

def get_path(start, end, map) :
    i,j = start
    path = [start]
    while (i,j) != end :
        for di, dj in [(-1,0), (0,1), (1,0), (0,-1)] :
            if 1 <= i+di < len(map)-1 and 1 <= j+dj < len(map[0])-1 and map[i+di][j+dj] != '#' and map[i+di][j+dj] != 'O' :
                i += di
                j += dj
                path.append((i,j))
                map[i][j] = 'O'
                break
    return path

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
        print('\n'.join([''.join(row) for row in map]))
        print(start)
        print(end)
        print(len(map),len(map[0]))
        
        map[start[0]][start[1]] = 'O'
        path = get_path(start, end, map)
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
                        elif picoseconds_saved > 0 :
                            cheats[picoseconds_saved] = 1
                    except Exception :
                        pass
            index1 += 1
        
        total = 0
        for cheat in cheats.keys() :
            if cheat >= 100 :
                total += cheats[cheat]
        print(cheats)
        return total

print(solve(part))
