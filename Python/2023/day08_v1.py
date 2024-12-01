# Day 8, part 1 of Advent of Code 2023

#data_file = open('./Data/2023/day08_test1.txt', 'r')
#data_file = open('./Data/2023/day08_test2.txt', 'r')

data_file = open('./Data/2023/day08.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

instructions = data_lines[0]
length = len(instructions)

class Node :
    
    def __init__(self,line) :
        self.name = line[:3]
        self.left = line[7:10]
        self.right = line[12:15]
    
    def __repr__(self) :
        return self.name + " = (" + self.left + ", " + self.right + ")"
    
    def go_next(self,instruction) :
        #print(self," -> ",instruction)
        if instruction == 'L' :
            return self.left
        if instruction == 'R' :
            return self.right

nodes = {}
for line in data_lines[2:] :
    nodes[line[:3]] = Node(line)

i = 0
next = 'AAA'
while next != 'ZZZ' :
    next = nodes[next].go_next(instructions[i])
    if next != 'ZZZ' :
        i += 1
        if i == len(instructions) :
            instructions += instructions[:length]

print('Result = ',len(instructions))
# Answer is 21389