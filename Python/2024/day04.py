# Day 4, Advent of Code 2024

import re

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day04_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day04.txt", 'r')

part = 2

def get_neighbors(map, start):
    i, j = start
    neighbors = [-1,-1,-1,-1,-1,-1,-1,-1] # up, up-right, right, down-right, down, down-left, left, up-left
    if i > 0 :
        neighbors[0] = (i-1,j) #UP
        if j < len(map[i])-1 :
            neighbors[1] = (i-1,j+1) #UP-RIGHT
        if j > 0 :
            neighbors[7] = (i-1,j-1) #UP-LEFT
    if i < len(map)-1 :
        neighbors[4] = (i+1,j) #DOWN
        if j < len(map[i])-1 :
            neighbors[3] = (i+1,j+1) #DOWN-RIGHT
        if j > 0 :
            neighbors[5] = (i+1,j-1) #DOWN-LEFT
    if j < len(map[i])-1 :
        neighbors[2] = (i,j+1) #RIGHT
    if j > 0 :
        neighbors[6] = (i,j-1) #LEFT
    return neighbors

def solve(part):
    if part == 1:
        # PART 1

        map = []
        starts = []
        i = 0
        for line in data_file:
            map_line = []
            j = 0
            for c in line.strip() :
                map_line.append(c)
                if c == 'X' :
                    starts.append((i,j))
                j += 1
            map.append(map_line)
            i += 1
        data_file.close()
        
        xmas_count = 0
        for start in starts :
            X_neighbors = get_neighbors(map, start)
            if X_neighbors[0] != -1 : #UP
                next = X_neighbors[0]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[0] != -1 :
                        next = M_neighbors[0]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[0] != -1 :
                                next = A_neighbors[0]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
            if X_neighbors[1] != -1 : #UP-RIGHT
                next = X_neighbors[1]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[1] != -1 :
                        next = M_neighbors[1]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[1] != -1 :
                                next = A_neighbors[1]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
            if X_neighbors[2] != -1 : #RIGHT
                next = X_neighbors[2]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[2] != -1 :
                        next = M_neighbors[2]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[2] != -1 :
                                next = A_neighbors[2]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
            if X_neighbors[3] != -1 : #DOWN-RIGHT
                next = X_neighbors[3]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[3] != -1 :
                        next = M_neighbors[3]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[3] != -1 :
                                next = A_neighbors[3]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
            if X_neighbors[4] != -1 : #DOWN
                next = X_neighbors[4]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[4] != -1 :
                        next = M_neighbors[4]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[4] != -1 :
                                next = A_neighbors[4]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
            if X_neighbors[5] != -1 : #DOWN-LEFT
                next = X_neighbors[5]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[5] != -1 :
                        next = M_neighbors[5]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[5] != -1 :
                                next = A_neighbors[5]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
            if X_neighbors[6] != -1 : #LEFT
                next = X_neighbors[6]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[6] != -1 :
                        next = M_neighbors[6]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[6] != -1 :
                                next = A_neighbors[6]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
            if X_neighbors[7] != -1 : #UP-LEFT
                next = X_neighbors[7]
                if map[next[0]][next[1]] == 'M' :
                    M_neighbors = get_neighbors(map, next)
                    if M_neighbors[7] != -1 :
                        next = M_neighbors[7]
                        if map[next[0]][next[1]] == 'A' :
                            A_neighbors = get_neighbors(map, next)
                            if A_neighbors[7] != -1 :
                                next = A_neighbors[7]
                                if map[next[0]][next[1]] == 'S' :
                                    xmas_count += 1
                
        return xmas_count  # Answer is 2370

    elif part == 2:
        # PART 2

        map = []
        starts = []
        i = 0
        for line in data_file:
            map_line = []
            j = 0
            for c in line.strip() :
                map_line.append(c)
                if c == 'A' :
                    starts.append((i,j))
                j += 1
            map.append(map_line)
            i += 1
        data_file.close()
        
        xmas_count = 0
        for start in starts :
            A_neighbors = get_neighbors(map, start)
            if A_neighbors[1] != -1 and A_neighbors[3] != -1 and A_neighbors[5] != -1 and A_neighbors[7] != -1 : #UP-RIGHT, DOWN-RIGHT, DOWN-LEFT and UP-LEFT
                up_right = A_neighbors[1]
                down_right = A_neighbors[3]
                down_left = A_neighbors[5]
                up_left = A_neighbors[7]
                right = False
                left = False
                if map[up_right[0]][up_right[1]] == 'M' and map[down_left[0]][down_left[1]] == 'S' :
                    right = True
                if map[down_left[0]][down_left[1]] == 'M' and map[up_right[0]][up_right[1]] == 'S' :
                    right = True
                if map[up_left[0]][up_left[1]] == 'M' and map[down_right[0]][down_right[1]] == 'S' :
                    left = True
                if map[down_right[0]][down_right[1]] == 'M' and map[up_left[0]][up_left[1]] == 'S' :
                    left = True
                if right and left :
                    xmas_count += 1
        
        return xmas_count  # Answer is 1908

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
