# Day 3, Advent of Code 2024

import re

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day03_test2.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day03.txt", 'r')

part = 2

def solve(part):
    if part == 1:
        # PART 1

        total = 0
        for line in data_file:
            mult = re.findall("mul[(][0-9]+,[0-9]+[)]", line)
            for m in mult:
                parts = re.findall("[0-9]+", m)
                if len(parts) == 2 and 1 <= len(parts[0]) <= 3 and 1 <= len(parts[1]) <= 3:
                    total += int(parts[0]) * int(parts[1])
        data_file.close()

        return total  # Answer is 187194524

    elif part == 2:
        # PART 2

        all = data_file.read()
        data_file.close()

        instructions = []
        do = re.split("do[(][)]", all)
        for d in do:
            s = re.split("don't[(][)]", d)
            instructions.append(s[0])
        
        total = 0
        for i in instructions:
            mult = re.findall("mul[(][0-9]+,[0-9]+[)]", i)
            for m in mult:
                parts = re.findall("[0-9]+", m)
                if len(parts) == 2 and 1 <= len(parts[0]) <= 3 and 1 <= len(parts[1]) <= 3:
                    total += int(parts[0]) * int(parts[1])

        return total  # Answer is 3127092535

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
