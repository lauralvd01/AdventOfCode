# Day 11, Advent of Code 2024

from collections import Counter

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day11_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day11.txt", 'r')

part = 2

def get_new_stones(stones):
    new_stones = Counter()
    for stone, count in stones.items():
        if stone == "0":
            new_stones["1"] += count
        else:
            if len(stone) % 2 == 0:
                first = int(stone[:len(stone)//2])
                second = int(stone[len(stone)//2:])
                new_stones[str(first)] += count
                new_stones[str(second)] += count
            else:
                new_stones[str(int(stone)*2024)] += count
    return new_stones

def solve(part):
    if part == 1:
        # PART 1

        data = data_file.read().strip()
        data_file.close()
        
        stones  = data.split(' ')
        blink = 0
        while blink < 25 :
            new_stones = []
            for stone in stones :
                if int(stone) == 0 :
                    new_stones.append(str(1))
                elif len(stone) % 2 == 0 :
                    first = int(stone[:len(stone)//2])
                    second = int(stone[len(stone)//2:])
                    new_stones.append(str(first))
                    new_stones.append(str(second))
                else :
                    new_stones.append(str(int(stone)*2024))
            blink += 1
            stones = new_stones
        
        total = len(stones)
        return total  # Answer is 216996

    elif part == 2:
        # PART 2
        
        # "No matter how the stones change, their **order is preserved**, and they stay on their perfectly straight line."
        # BUT in conclusion, the order doesn't matter !! => We can can each value of the stones 
        # and perform the rules on "each of them at the same time" instead of perform the rules on 
        # every each of the stones ==> use less memory & less time to compute
        
        # Tips discovered : Counter package from collection

        data = data_file.read().strip()
        data_file.close()
        
        stones = Counter(data.split(' '))
        blink = 0
        while blink < 75 :
            new_stones = get_new_stones(stones)
            blink += 1
            stones = new_stones

        total = sum(stones.values())
        return total  # Answer is 

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
