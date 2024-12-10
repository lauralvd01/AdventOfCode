# Day 8, Advent of Code 2024

import itertools

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day08_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day08.txt", 'r')

part = 2

def get_antinodes1(node1, node2, n, m) :
    diff = (node2[0] - node1[0], node2[1] - node1[1])
    first = (node2[0] + diff[0], node2[1] + diff[1])
    second = (node1[0] - diff[0], node1[1] - diff[1])
    antinodes = [antinode for antinode in [first, second] if 0 <= antinode[0] < n and 0 <= antinode[1] < m]
    return antinodes

def get_antinodes2(node1, node2, n, m) :
    diff = (node2[0] - node1[0], node2[1] - node1[1])
    antinodes = [node2]
    while True :
        first = (antinodes[-1][0] + diff[0], antinodes[-1][1] + diff[1])
        if 0 <= first[0] < n and 0 <= first[1] < m :
            antinodes.append(first)
        else :
            break
    antinodes.append(node1)
    while True :
        second = (antinodes[-1][0] - diff[0], antinodes[-1][1] - diff[1])
        if 0 <= second[0] < n and 0 <= second[1] < m :
            antinodes.append(second)
        else :
            break
    return antinodes

def solve(part):
    if part == 1:
        # PART 1

        map = []
        frequences = {}
        i = 0
        for line in data_file :
            s = []
            for j in range(len(line.strip())) :
                s.append(line[j])
                if line[j] != '.' :
                    if line[j] not in frequences :
                        frequences[line[j]] = [(i,j)]
                    else :
                        frequences[line[j]].append((i,j))
            map.append(s)
            i += 1
        data_file.close()
        
        total = 0
        for frequency in frequences.keys() :
            for pair in itertools.combinations(frequences[frequency], r=2) :
                antinodes = get_antinodes1(pair[0], pair[1], len(map), len(map[0]))
                for antinode in antinodes :
                    if len(map[antinode[0]][antinode[1]]) == 1 :
                        total += 1
                        map[antinode[0]][antinode[1]] += '#'
        
        return total  # Answer is 244

    elif part == 2:
        # PART 2

        map = []
        frequences = {}
        i = 0
        for line in data_file :
            s = []
            for j in range(len(line.strip())) :
                s.append(line[j])
                if line[j] != '.' :
                    if line[j] not in frequences :
                        frequences[line[j]] = [(i,j)]
                    else :
                        frequences[line[j]].append((i,j))
            map.append(s)
            i += 1
        data_file.close()
        
        total = 0
        for frequency in frequences.keys() :
            if len(frequences[frequency]) > 1 :
                for pair in itertools.combinations(frequences[frequency], r=2) :
                    antinodes = get_antinodes2(pair[0], pair[1], len(map), len(map[0]))
                    for antinode in antinodes :
                        if len(map[antinode[0]][antinode[1]]) == 1 :
                            total += 1
                            map[antinode[0]][antinode[1]] += '#'
            
        return total  # Answer is 912

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
