# Day 19, Advent of Code 2024

import re

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day19_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day19.txt", 'r')

part = 1

def get_one_possibility(design, current_design, towels_by_first) :
    print(design, current_design)
    
    if len(design) == 0 :
        return current_design
    
    if design[0] in towels_by_first :
        for towel in towels_by_first[design[0]] :
            if len(design) >= len(towel) and design[:len(towel)] == towel :
                result = get_one_possibility(design[len(towel):], current_design + towel, towels_by_first)
                if result is not None :
                    return result
    return None

def solve(part):
    
    if part == 1:
        # PART 1
                
        data = data_file.read().split('\n\n')
        data_file.close()
        
        towels_by_first = {}
        for towel in data[0].strip().split(', ') :
            if towel[0] not in towels_by_first :
                towels_by_first[towel[0]] = [towel]
            else :
                towels_by_first[towel[0]].append(towel)
                
        designs = data[1].split('\n')
        
        total = 0
        for design in designs :
            result = get_one_possibility(design, '', towels_by_first)
            if result is not None :
                total += 1
                print(result)
                print()
            
            # possibilities = []
            # if design[0] in towels_by_first :
            #     for towel in towels_by_first[design[0]] :
            #         if len(design) >= len(towel) and design[:len(towel)] == towel :
            #             possibilities.append(towel)
                
            #     while len(possibilities) > 0 :
            #         print(len(possibilities))
            #         start = possibilities.pop(0)
            #         if len(start) == len(design) :
            #             total += 1
            #             print(design)
            #             break
            #         else :
            #             for towel in towels_by_first[design[len(start)]] :
            #                 if len(design) >= len(start) + len(towel) and design[len(start):len(start)+len(towel)] == towel :
            #                     possibilities.append(start + towel)
        return total  # Answer is 
    
    elif part == 2:
        # PART 2
        
        total = 0
        return total  # Answer is 
    
    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
