# Day 6, Advent Of Code 2024

#data_file = open("day06_test.txt","r")
data_file = open("day06.txt","r")

part = 2

def solve(part):
    if part == 1 :
        # PART 1
        map = []
        start = None
        directions = [(-1,0),(0,+1),(1,0),(0,-1)]
        actual_direction = None
        i = 0
        for line in data_file :
            l = []
            j = 0
            for c in line.strip() :
                l.append(c)
                if c == "^" :
                    start = (i,j)
                    actual_direction = 0
                if c == ">" :
                    start = (i,j)
                    actual_direction = 1
                if c == "v" :
                    start = (i,j)
                    actual_direction = 2
                if c == "<" :
                    start = (i,j)
                    actual_direction = 3
                j += 1
            map.append(l)
            i += 1
        
        total = 0
        i,j = start
        di,dj = directions[actual_direction]
        while 0 <= i+di < len(map) and 0 <= j+dj <= len(map[0]) :
            if map[i][j] != "X" :
                total += 1
                map[i][j] = "X"
            while map[i+di][j+dj] == "#" :
                actual_direction += 1
                actual_direction %= 4
                di,dj = directions[actual_direction]
            i += di
            j += dj
        if map[i][j] != "X" :
            total += 1
            map[i][j] = "X"
        return total # Answer is 5086
    
    elif part == 2 :
        # PART 2
        map = []
        start = None
        directions = [(-1,0),(0,+1),(1,0),(0,-1)]
        start_direction = None
        i = 0
        for line in data_file :
            l = []
            j = 0
            for c in line.strip() :
                l.append(c)
                if c == "^" :
                    start = (i,j)
                    start_direction = 0
                if c == ">" :
                    start = (i,j)
                    start_direction = 1
                if c == "v" :
                    start = (i,j)
                    start_direction = 2
                if c == "<" :
                    start = (i,j)
                    start_direction = 3
                j += 1
            map.append(l)
            i += 1
        
        i,j = start
        actual_direction = start_direction
        di,dj = directions[actual_direction]
        possibilities = []
        while 0 <= i+di < len(map) and 0 <= j+dj <= len(map[0]) :
            if (i,j) not in possibilities :
                possibilities.append((i,j))
            while map[i+di][j+dj] == "#" :
                actual_direction += 1
                actual_direction %= 4
                di,dj = directions[actual_direction]
            i += di
            j += dj
        
        if (i,j) not in possibilities :
            possibilities.append((i,j))
        possibilities.pop(0)
        
        total = 0
        for possibilitie in possibilities :
            old = map[possibilitie[0]][possibilitie[1]]
            map[possibilitie[0]][possibilitie[1]] = "#"
            
            memory = {}
            i,j = start
            actual_direction = start_direction
            di,dj = directions[actual_direction]
            stop = False
            while 0 <= i+di < len(map) and 0 <= j+dj < len(map[0]) and not stop :
                while map[i+di][j+dj] == "#" :
                    actual_direction += 1
                    actual_direction %= 4
                    di,dj = directions[actual_direction]
                    while not (0 <= i+di < len(map) and 0 <= j+dj < len(map[0])) :
                        actual_direction += 1
                        actual_direction %= 4
                        di,dj = directions[actual_direction]
                    
                if (i,j) not in memory.keys() :
                    memory[(i,j)] = [actual_direction]
                elif actual_direction in memory[(i,j)] : # Boucle trouvée !
                    total += 1
                    stop = True
                else :
                    memory[(i,j)].append(actual_direction)
                
                i += di
                j += dj
            
            map[possibilitie[0]][possibilitie[1]] = old
            
        return total # Answer is 1770
    else :
        print("INVALID PART")

print(solve(part))