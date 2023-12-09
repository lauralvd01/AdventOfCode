# Day 8, part 2 of Advent of Code 2023

#data_file = open('./Data/day08_test3.txt', 'r')

data_file = open('./Data/day08.txt', 'r')

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
nexts = []
for line in data_lines[2:] :
    nodes[line[:3]] = Node(line)
    if line[2] == 'A' :
        nexts.append(line[:3])

counts = []
for next in nexts :
    instructions = data_lines[0]
    i = 0
    while next[-1] != 'Z' :
        next = nodes[next].go_next(instructions[i])
        if next[-1] != 'Z' :
            i += 1
            if i == len(instructions) :
                instructions += instructions[:length]
    counts.append(i+1)

def ppcm(a,b):
    p=a*b
    while(a!=b):
        if (a<b): b-=a
        else: a-=b
    return p/a

def ppcm_tab(tab) :
    p = 1
    for e in tab :
        p = int(ppcm(p,e))
    return p

print('Result = ',ppcm_tab(counts))
# Answer is 21083806112641