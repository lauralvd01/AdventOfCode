# Day 9, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day09_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day09.txt", 'r')

part = 2

def get_empty_space(memory, space_required, start_index):
    empty_space = None
    count = 0
    for i in range(start_index) :
        if memory[i] == '.' :
            if empty_space == None :
                empty_space = i
                count = 1
            else :
                count += 1
            if count == space_required :
                return empty_space
        else :
            empty_space = None
            count = 0
    return -1

def solve(part):
    if part == 1:
        # PART 1

        data = data_file.read().strip()
        data_file.close()
        
        blocks = []
        for i in range(len(data)) :
            number_blocks = int(data[i])
            if i % 2 == 0 :
                blocks += [str(i//2) for k in range(number_blocks)]
            else :
                blocks += ['.' for k in range(number_blocks)]
        
        first_empty_place = int(data[0])
        for i in range(len(blocks)-1, 0, -1) :
            if blocks[i] != '.' :
                if first_empty_place > i :
                    break
                blocks[first_empty_place] = blocks[i]
                blocks[i] = '.'
                while blocks[first_empty_place] != '.' :
                    first_empty_place += 1
            
        total = 0
        for i in range(first_empty_place):
            total += int(blocks[i])*i
        return total  # Answer is 6382875730645

    elif part == 2:
        # PART 2

        data = data_file.read().strip()
        data_file.close()
        
        memory = []
        block_id = 0
        blocks = {}
        for i in range(len(data)) :
            number_blocks = int(data[i])
            if number_blocks > 0 :
                if i % 2 == 0 :
                    blocks[block_id] = {"start_index": len(memory), "number_blocks": number_blocks}
                    memory += [str(block_id) for k in range(number_blocks)]
                    block_id += 1
                else:
                    memory += ['.' for k in range(number_blocks)]
        
        for i in range(len(blocks.keys())-1, 0, -1) :
            start_index = blocks[i]["start_index"]
            space_required = blocks[i]["number_blocks"]
            empty_space = get_empty_space(memory, space_required, start_index)
            if empty_space != -1 :
                memory = memory[:empty_space] + [str(i) for k in range(space_required)] + memory[empty_space+space_required:]
                memory = memory[:start_index] + ['.' for k in range(space_required)] + memory[start_index+space_required:]
                blocks[i]["start_index"] = empty_space
        
        total = 0
        for i in range(len(memory)):
            if memory[i] != '.' :
                total += int(memory[i])*i
        return total  # Answer is 6420913943576

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
