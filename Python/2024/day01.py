# Day 1, Advent of Code 2024

#data_file = open('../../Data/2024/day01_test.txt', 'r')
data_file = open('../../Data/2024/day01.txt', 'r')

part = 2

def solve(part) :
    if part == 1 :
        # PART 1

        left_list = []
        right_list = []
        for line in data_file:
            parts = line.split(' ')
            left_list.append(int(parts[0]))
            right_list.append(int(parts[3].strip()))
        data_file.close()

        left_list.sort()
        right_list.sort()

        total = 0
        for i in range(len(left_list)):
            diff = abs(left_list[i] - right_list[i])
            total += diff

        return total  # Answer is 1660292
    
    elif part == 2 :
        # PART 2

        left_list = []
        right_dict = {}
        for line in data_file:
            parts = line.split(' ')
            left_list.append(int(parts[0]))
            right = int(parts[3].strip())
            if right in right_dict.keys() :
                right_dict[right] += 1
            else :
                right_dict[right] = 1
        data_file.close()

        total = 0
        for i in range(len(left_list)):
            if left_list[i] in right_dict.keys() :
                mult = left_list[i]*right_dict[left_list[i]]
                total += mult

        return total # Answer is 22776016
    
    else :
        return 'Invalid part'
    
print(solve(part))