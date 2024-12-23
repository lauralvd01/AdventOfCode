# Day 23 - Advent Of Code 2024

from itertools import permutations

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day23_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day23.txt", 'r')

part = 1

def solve(part) :
    global directions
    
    if part == 1 :
        # Part 1
        
        computers = {}
        for line in data_file :
            c1 = line[:2]
            c2 = line[3:5]
            if c1 not in computers :
                computers[c1] = [c2]
            else :
                computers[c1].append(c2)
            if c2 not in computers :
                computers[c2] = [c1]
            else :
                computers[c2].append(c1)
        data_file.close()
        
        total = 0
        three_sets = []
        for c1 in computers.keys() :
            for c2 in computers[c1] :
                for c3 in computers[c2] :
                    if c1 in computers[c3] :
                        new = True
                        for p in permutations((c1, c2, c3)) :
                            if p in three_sets :
                                new = False
                                break
                        if new :
                            three_sets.append((c1, c2, c3))
                            print(c1, c2, c3)
                            if 't' in [c1[0], c2[0], c3[0]] :
                                total += 1
        return total # Answer is 1083
    
    elif part == 2 :
        # Part 2
        
        computers = {}
        for line in data_file :
            c1 = line[:2]
            c2 = line[3:5]
            if c1 not in computers :
                computers[c1] = [c2]
            else :
                computers[c1].append(c2)
            if c2 not in computers :
                computers[c2] = [c1]
            else :
                computers[c2].append(c1)
        data_file.close()
        
        total = 0        
        return total # Answer is 
    
    else:
        data_file.close()
        return 'Invalid part'

print(solve(part))
