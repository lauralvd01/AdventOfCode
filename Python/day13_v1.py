# Day 13, part 1 of Advent of Code 2023

#data_file = open('./Data/day13_test1.txt', 'r')

data_file = open('./Data/day13.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

patterns = []
i = 0
while i < len(data_lines):
    pattern = [] 
    while i < len(data_lines) and data_lines[i] != '':
        pattern.append(data_lines[i])
        i += 1
    patterns.append(pattern)
    i += 1

def get_reflections(pattern):
    reflections_rows = {}
    i = 0
    while i < len(pattern)-1:
        if pattern[i][:] == pattern[i+1][:] :
            reflections_rows[i] = 1
        i += 1
    for r in reflections_rows :
        length = 1
        while r-length >= 0 and r+length+1 < len(pattern) and pattern[r-length][:] == pattern[r+length+1][:] :
            length += 1
        reflections_rows[r] = length
    #print('Rows',reflections_rows)
    real_ref_rows = {}
    for r in reflections_rows :
        if r+reflections_rows[r] == len(pattern) or r-reflections_rows[r] == 0 :
            real_ref_rows[r] = reflections_rows[r] 
    
    reflections_columns = {}
    j = 0
    while j < len(pattern[0]) -1 :
        if ''.join([pattern[i][j] for i in range(len(pattern))]) == ''.join([pattern[i][j+1] for i in range(len(pattern))]) :
            reflections_columns[j] = 1
        j += 1
    for r in reflections_columns :
        length = 1
        while r-length >= 0 and r+length+1 < len(pattern[0]) and ''.join([pattern[i][r-length] for i in range(len(pattern))]) == ''.join([pattern[i][r+length+1] for i in range(len(pattern))]) :
            length += 1
        reflections_columns[r] = length
    #print("Columns",reflections_columns)
    
    real_ref_columns = {}
    for r in reflections_columns :
        if r+reflections_columns[r] == len(pattern) or r-reflections_columns[r] == 0 :
            real_ref_columns[r] = reflections_columns[r] 
    
    return real_ref_rows, real_ref_columns



m_rows = 100
result = 0
for pattern in patterns :
    reflections_rows, reflections_columns = get_reflections(pattern)
    max_r = 0
    reflection = -1
    column = False
    for r in reflections_rows:
        if reflections_rows[r] > max_r:
            max_r = reflections_rows[r]
            reflection = r
    for r in reflections_columns:
        if reflections_columns[r] > max_r:
            max_r = reflections_columns[r]
            reflection = r
            column = True
    #print('Pattern',p,'Reflection',reflection,'Column',column)
    if column :
        result += reflection + 1
    else :
        result += (reflection + 1) * m_rows
 
print('Result = ',result)
# Answer is not 2442