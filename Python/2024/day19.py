# Day 19, Advent of Code 2024

import re

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day19_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day19.txt", 'r')

part = 2

def is_possible(design, towels_by_lenght) :
    start_slice_is_possible = [False] * (len(design)+1)
    start_slice_is_possible[0] = True # design[:0] = '' => always possible (no towel)
    
    for i in range(1, len(design)+1) :
        # Test if design[:i] is possible
        for j in [lenght for lenght in towels_by_lenght if lenght <= i] :
            # Check if making design[:i-j] is possible and if design[i-j:i] is a towel
            if start_slice_is_possible[i-j] and design[i-j:i] in towels_by_lenght[j] :
                # Then makng design[:i] is possible
                start_slice_is_possible[i] = True
                break
    # Return if design ( design[:len(design)] ) is possible
    return start_slice_is_possible[-1]

def is_possible2(design, towels_by_lenght) :
    start_slice_is_possible = [[False,[]] for i in range(len(design)+1)]
    start_slice_is_possible[0] = [True,[0]] # design[:0] = '' => always possible (no towel)
    
    for i in range(1, len(design)+1) :
        # Test if design[:i] is possible
        for j in [lenght for lenght in towels_by_lenght if lenght <= i] :
            # Check if making design[:i-j] is possible and if design[i-j:i] is a towel
            if start_slice_is_possible[i-j][0] :
                for towel in towels_by_lenght[j] :
                    if design[i-j:i] == towel :
                        # Then makng design[:i] is possible
                        start_slice_is_possible[i][0] = True
                        start_slice_is_possible[i][1].append(j)
    return start_slice_is_possible

def get_number_of_possibilities(current_index, start_slice_is_possible) :
    if not start_slice_is_possible[current_index][0] :
        return 0
    if current_index == 0 :
        return 1
    
    count = 0
    for lenght in start_slice_is_possible[current_index][1] :
        result = get_number_of_possibilities(current_index-lenght, start_slice_is_possible)
        count += result
    return count

def solve(part):
    
    if part == 1:
        # PART 1
                
        data = data_file.read().split('\n\n')
        data_file.close()
        
        towels_by_lenght = {}
        for towel in data[0].strip().split(', ') :
            if len(towel) not in towels_by_lenght :
                towels_by_lenght[len(towel)] = [towel]
            else :
                towels_by_lenght[len(towel)].append(towel)
                
        designs = data[1].split('\n')
        
        total = 0
        for design in designs :
            if is_possible(design, towels_by_lenght) :
                total += 1
                print(design)
        return total  # Answer is 260
    
    elif part == 2:
        # PART 2
        
        data = data_file.read().split('\n\n')
        data_file.close()
        
        towels_by_lenght = {}
        for towel in data[0].strip().split(', ') :
            if len(towel) not in towels_by_lenght :
                towels_by_lenght[len(towel)] = [towel]
            else :
                towels_by_lenght[len(towel)].append(towel)
                
        designs = data[1].split('\n')
        
        possibilities = []
        for design in designs :
            start_slice_is_possible = is_possible2(design, towels_by_lenght)
            if start_slice_is_possible[-1][0] :
                possibilities.append(start_slice_is_possible)
          
        total = 0
        for possibility in possibilities :
            print(possibility)
            total += get_number_of_possibilities(len(possibility)-1, possibility)
        return total  # Answer is 
    
    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
