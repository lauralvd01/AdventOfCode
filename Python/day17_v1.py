# Day 17, part 1 of Advent of Code 2023

data_file = open('./Data/day17_test1.txt', 'r')

#data_file = open('./Data/day17.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

map = [[[int(num),False] for num in line] for line in data_lines]
WIDTH = len(map[0])
HEIGHT = len(map)

start = [0,0]
end = [HEIGHT-1,WIDTH-1]
max_in_line = 3

def get_neighbors(current) :
    n = [[[i,j] 
          for j in [current[1]-1,current[1],current[1]+1]] 
          for i in [current[0]-1,current[0],current[0]+1] ]
    for k in range(len(n)) :
        for l in range(len(n[0])) :
            if 0 > n[k][l][1] or n[k][l][1]>= WIDTH or 0 > n[k][l][0] or n[k][l][0] >= HEIGHT :
                n[k][l] = None
    #### [ [ top-left    top    top-right ]
    ####   [ left      current      right ]
    ####   [ down-left   down  down-right ]]
    return n

def get_min_path(current,count=0,direction=None) :
    if current == end :
        return map[current[0]][current[1]][0]
    
    if not map[current[0]][current[1]][1] :
        map[current[0]][current[1]][1] = True
        
    neighbors = get_neighbors(current)
    heat_losses = []
    
    down = neighbors[2][1]
    if down is not None and not map[down[0]][down[1]][1] and (direction != 'down' or count < max_in_line) :
        result_down = get_min_path(down,count+1 if direction == 'down' else 1,'down')
        if result_down != (None,None) :
            heat_losses.append(result_down)
            
    right = neighbors[1][2]
    if right is not None and not map[right[0]][right[1]][1] and (direction != 'right' or count < max_in_line) :
        result_right = get_min_path(right,count+1 if direction == 'right' else 1,'right')
        if result_right != (None,None) :
            heat_losses.append(result_right)
    
    top = neighbors[0][1]
    if top is not None and not map[top[0]][top[1]][1] and (direction != 'top' or count < max_in_line) :
        result_top = get_min_path(top,count+1 if direction == 'top' else 1,'top')
        if result_top != (None,None) :
            heat_losses.append(result_top)
    
    left = neighbors[1][0]
    if left is not None and not map[left[0]][left[1]][1] and (direction != 'left' or count < max_in_line) :
        result_left = get_min_path(left,count+1 if direction == 'left' else 1,'left')
        if result_left != (None,None) :
            heat_losses.append(result_left)
    
    if len(heat_losses) == 0 :
        return None,None
    
    return map[current[0]][current[1]][0] + min(heat_losses)

print('Result = ',get_min_path(start)-map[start[0]][start[1]][0])
# Answer is 510801
