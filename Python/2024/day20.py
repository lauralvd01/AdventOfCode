# Day 20 - Advent Of Code 2024

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day20_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day20.txt", 'r')


part = 2

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

def get_cheatings_from(start,map) :
    new_map = [[cell for cell in row] for row in map] # Copy of the map to avoid modifying the original map
    i,j = start
    new_map[i][j] = 'S' # Start position of the cheat path
    
    cheat_ends_by_lenght = {} # {n : (i,j) list} End positions of correct cheat paths of lenght n, starting from start, passing at least one wall and returning on the original path
    end_positions = [] # List of just the end positions of the cheat paths
    
    # First next steps : pass through a wall
    next = []
    for di, dj in [(-1,0),(0,1),(1,0),(0,-1)] :
        if 1 <= i+di < len(new_map)-1 and 1 <= j+dj < len(new_map[0])-1 and map[i+di][j+dj] == '#' :
            new_map[i+di][j+dj] = '1'
            next.append((i+di,j+dj))
    
    # Next steps : continue cheating (through a wall or not) until the end of the maximum cheating time (20 picoseconds)
    for n in range(2,21) :
        next_next = []
        while len(next) > 0 :
            current_i, current_j = next.pop(0)
            for di, dj in [(-1,0),(0,1),(1,0),(0,-1)] :
                if 1 <= current_i+di < len(new_map)-1 and 1 <= current_j+dj < len(new_map[0])-1 :
                    next_i, next_j = current_i+di, current_j+dj
                    
                    # Continuing with this next position if it is not a wall or a position already visited
                    if new_map[next_i][next_j] == '#' or new_map[next_i][next_j] == 'O' :
                        new_map[next_i][next_j] = f"{n}" # Mark the position as visited
                        next_next.append((next_i,next_j))
                        
                        # If we return on the original path, we have a correct cheat path
                        if map[next_i][next_j] == 'O' :
                            # 2 cheat paths that start from the same position and end at the same position are considered the same
                            if (next_i,next_j) not in end_positions :
                                end_positions.append((next_i,next_j))
                                # We sort the cheat paths by the number of picoseconds used to cheat (between 2 and 20)
                                if n not in cheat_ends_by_lenght.keys() :
                                    cheat_ends_by_lenght[n] = [(next_i,next_j)]
                                else :
                                    cheat_ends_by_lenght[n].append((next_i,next_j))
        next = next_next
    return cheat_ends_by_lenght

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
        
        map[start[0]][start[1]] = 'O'
        path = get_path(start, end, map)
        
        cheats = {}
        without_cheat = len(path)
        index_1 = 0
        for step in path :
            i,j = step
            for di, dj in [(-1,0), (0,1), (1,0), (0,-1)] :
                if 1 <= i+di < len(map)-1 and 1 <= j+dj < len(map[0])-1 and map[i+di][j+dj] == '#' :
                    try :
                        index2 = path.index((i+2*di,j+2*dj))
                        picoseconds_saved = without_cheat - (len(path[:index_1]) + len(path[index2:])) -2
                        if picoseconds_saved in cheats.keys() :
                            cheats[picoseconds_saved] += 1 
                        elif picoseconds_saved > 0 :
                            cheats[picoseconds_saved] = 1
                    except Exception :
                        pass
            index_1 += 1
        
        total = 0
        for cheat in cheats.keys() :
            if cheat >= 100 :
                total += cheats[cheat]
        return total # Answer is 1311
    
    elif part == 2 :
        # Part 2
        
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
        
        map[start[0]][start[1]] = 'O'
        path = get_path(start, end, map)
        
        cheats = {} # {n : number_of_different_cheat_paths_that_save_n_picoseconds}
        index1 = 0  # Start position of the cheat paths
        for step in path :
            # End positions of correct cheat paths starting from step, passing at least one wall and returning on the original path
            cheat_ends = get_cheatings_from(step,map) # {n : (i,j) list} with n the number of picoseconds used to cheat to reach (i,j)
            for lenght in cheat_ends.keys() :
                for cheat_end in cheat_ends[lenght] :
                    try :
                        index_n = path.index(cheat_end)
                        if index_n > index1 :
                            picoseconds_saved = index_n-index1 - lenght
                            if picoseconds_saved in cheats.keys() :
                                cheats[picoseconds_saved] += 1
                            elif picoseconds_saved > 0 :
                                print(f"New cheat path of {picoseconds_saved} picoseconds saved")
                                cheats[picoseconds_saved] = 1
                                    
                    except Exception :
                        pass
            index1 += 1
            
        total = 0
        for cheat in cheats.keys() :
            if cheat >= 100 :
                total += cheats[cheat]
        return total # Answer is not 935834 but more ...
    
    else:
        data_file.close()
        return 'Invalid part'

print(solve(part))
