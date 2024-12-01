# Day 15, part 2 of Advent of Code 2023

#data_file = open('./Data/2023/day15_test1.txt', 'r')

data_file = open('./Data/2023/day15.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

def HASH(string) :
    current_value = 0
    for c in string :
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

steps = [x for x in data_lines[0].split(',') if x != '']
boxes = []

def remove_lens(boxe,label) :
    new_boxe = []
    for cur_label,cur_focal in boxe :
        if cur_label != label :
            new_boxe.append([cur_label,cur_focal])
    return new_boxe

def dash(box,label) :
    global boxes
    if box < len(boxes) :
        boxes[box] = remove_lens(boxes[box],label)

def equals(box,label,new_focal) :
    global boxes
    if box < len(boxes) :
        index = 0
        while index < len(boxes[box]) and boxes[box][index][0] != label :
            index += 1
        if index != len(boxes[box]) :
            boxes[box][index][1] = new_focal
        else :
            boxes[box].append([label,new_focal])
    else :
        for i in range(box-len(boxes)+1) :
            boxes.append([])
        boxes[box].append([label,new_focal])

for step in steps :
    i = 0
    while i < len(step) and step[i] != '=' and step[i] != '-' :
        i += 1
    label = step[:i]
    box = HASH(label)
    operation = step[i]
    #print(box,' -> ',label,operation,step[i+1:])
    if operation == '=' :
        new_focal = step[i+1:]
        equals(box,label,new_focal)
    else :
        dash(box,label)
    #print(boxes)
    
result = 0
for box in range(len(boxes)) :
    slot = 1
    for lens in boxes[box] :
        result += (1+box)*slot*int(lens[1])
        slot += 1
print('Result = ',result)
# Answer is 212763
