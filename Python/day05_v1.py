# Day 5, part 1 of Advent of Code 2023

#data_file = open('../Data/day05_test1.txt', 'r')

data_file = open('../Data/day05.txt', 'r')

data_lines = [line for line in data_file]
data_file.close()


seeds = [int(num) for num in data_lines[0][7:-1].split(' ')]

def generate(transform) :
    dataset = {}
    for trans in transform :
        for i in range(trans[2]) :
            dataset[trans[1]+i] = trans[0]+i
    return dataset

l = 3
data_sets = []
while l < len(data_lines):
    transform = []
    i = 0
    while data_lines[l+i] != '\n' :
        transform.append([int(num) for num in data_lines[l+i][:-1].split(' ')])
        i += 1
    data_sets.append(generate(transform))
    l += i+2


def get_transform(seed) :
    location = seed
    global data_sets
    for i in range(len(data_sets)) :
        if location in data_sets[i] :
            location = data_sets[i][location]
    return location

seeds_to_location = [get_transform(seed) for seed in seeds]
print('Result = ', min(seeds_to_location))
# Answer is 