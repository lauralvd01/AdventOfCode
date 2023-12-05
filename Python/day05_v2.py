# Day 5, part 2 of Advent of Code 2023

#data_file = open('../Data/day05_test1.txt', 'r')
data_file = open('../Data/day05.txt', 'r')

data_lines = [line for line in data_file]
data_file.close()


seed_ranges = [int(num) for num in data_lines[0][7:-1].split(' ')]
seeds = []
for i in range(0,len(seed_ranges),2) :
    for j in range(seed_ranges[i],seed_ranges[i]+seed_ranges[i+1]) :
        seeds.append(j)
print(len(seeds))

l = 3
data_sets = []
while l < len(data_lines):
    transform = []
    i = 0
    while data_lines[l+i] != '\n' :
        transform.append([int(num) for num in data_lines[l+i][:-1].split(' ')])
        i += 1
    data_sets.append(transform)
    l += i+2

def get_transform(seed) :
    location = seed
    global data_sets
    for transform in data_sets :
        i = 0
        while i < len(transform) :
            if transform[i][1] <= location < transform[i][1]+transform[i][2] :
                location += transform[i][0] - transform[i][1]
                break
            i += 1
    return location

seeds_to_location = [get_transform(seed) for seed in seeds]
print('Result = ', min(seeds_to_location))
# Answer is 3374647