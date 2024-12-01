# Day 5, part 2 of Advent of Code 2023

#data_file = open('../../Data/2023/day05_test1.txt', 'r')
data_file = open('../../Data/2023/day05.txt', 'r')

data_lines = [line for line in data_file]
data_file.close()

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

def get_inverse_transform(location) :
    seed = location
    global data_sets
    for t in range(len(data_sets)-1,-1,-1) :
        transform = data_sets[t]
        i = 0
        while i < len(transform) :
            if transform[i][0] <= seed < transform[i][0]+transform[i][2] :
                seed += transform[i][1] - transform[i][0]
                break
            i += 1
    return seed


seed_ranges = [int(num) for num in data_lines[0][7:-1].split(' ')]

location = 0
a = 0
while a == 0 :
    seed = get_inverse_transform(location)
    for i in range(0,len(seed_ranges),2) :
        if seed_ranges[i] <= seed and seed < seed_ranges[i]+seed_ranges[i+1] :
            a = 1
            break
    location += 1
    
print('Result = ', location-1)
# Answer is 6082852
# Too long