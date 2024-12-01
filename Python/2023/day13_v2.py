# Day 13, part 1 of Advent of Code 2023

data_file = open('./Data/2023/day13_test1.txt', 'r')

#data_file = open('./Data/2023/day13.txt', 'r')

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
    
    return reflections_rows, reflections_columns

def get_real_reflections(pattern,reflections,column=False) :
    real_ref = {}
    for r in reflections :
        if column :
            if r+reflections[r] == len(pattern[0])-1 or r-reflections[r]+1 == 0 :
                real_ref[r] = reflections[r]
        else :
            if r+reflections[r] == len(pattern)-1 or r-reflections[r]+1 == 0 :
                real_ref[r] = reflections[r]
    return real_ref

def get_longer_reflections(pattern,reflections,column=False) :
	for r in reflections :
		if column :
		# if increasing the reflection is possible
			if r+reflections[r] < len(pattern[0])-1 and r-reflections[r]+1 > 0 :
				smugle = None
				i = 0
				while i < len(pattern) :
					if pattern[i][r+reflections[r]+1] != pattern[i][r-reflections[r]] :
						if smugle is not None :
							smugle = i
						else :
						# more than one characters need to change to increase the reflection
							i = len(pattern)+1
					i += 1
				# for reflections where changing one and only one characters of increasing lines would allow to increase the reflection
				if smugle is not None and i == len(pattern) :
					# test each one of the four possible combinaisons 
					if pattern[i][r+reflections[r]+1] == '.' :
					# test 1 : forward column character to change is a dot ==> changing it to #
						pattern[i][r+reflections[r]+1] = '#'
						new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[1],True) if ref not in reflections] # get the new reflection created and keep it if it's a real one
						print(len(new))
						if new == [] :
						# the new reflection is not a real one
						# test 2 : forward column character to change is a dot => changing backward character to a dot
							pattern[i][r-reflections[r]] = '.'
							new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[1],True) if ref not in reflections]
							print(len(new))
							if new != [] :
							# the new reflection is a real one !
								return new[0]
						else :
							return new[0]
					else :
					# test 3 : forward column character to change is #  => changing it to a dot
						pattern[i][r+reflections[r]+1] = '.'
						new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[1],True) if ref not in reflections]
						print(len(new))
						if new == [] :
						# test 4 : forward column character to change is # => changing backward character to #
							pattern[i][r-reflections[r]] = '#'
							new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[1],True) if ref not in reflections]
							print(len(new))
							if new != [] :
								return new[0]
						else :
							return new[0]
		else :
		# if increasing the reflection is possible
			if r+reflections[r] < len(pattern)-1 and r-reflections[r]+1 > 0 :
				smugle = None
				j = 0
				while j < len(pattern[0]) :
					if pattern[r+reflections[r]+1][j] != pattern[r-reflections[r]][j] :
						if smugle is not None :
							smugle = j
						else :
						# more than one characters need to change to increase the reflection
							j = len(pattern[0])+1
					j += 1
				# for reflections where changing one and only one characters of increasing lines would allow to increase the reflection
				if smugle is not None and j == len(pattern[0]) :
					# test each one of the four possible combinaisons 
					if pattern[r+reflections[r]+1][j] == '.' :
					# test 1 : forward line character to change is a dot ==> changing it to #
						pattern[r+reflections[r]+1][j] = '#'
						new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[0],False) if ref not in reflections] # get the new reflection created and keep it if it's a real one
						print(len(new))
						if new == [] :
						# the new reflection is not a real one
						# test 2 : forward line character to change is a dot => changing backward character to a dot
							pattern[r-reflections[r]][j] = '.'
							new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[0],False) if ref not in reflections]
							print(len(new))
							if new != [] :
							# the new reflection is a real one !
								return new[0]
						else :
							return new[0]
					else :
					# test 3 : forward line character to change is #  => changing it to a dot
						pattern[r+reflections[r]+1][j] = '.'
						new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[0],False) if ref not in reflections]
						print(len(new))
						if new == [] :
						# test 4 : forward line character to change is # => changing backward character to #
							pattern[r-reflections[r]][j] = '#'
							new = [ref for ref in get_real_reflections(pattern,get_reflections(pattern)[0],False) if ref not in reflections]
							print(len(new))
							if new != [] :
								return new[0]
						else :
							return new[0]
	return []
	

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
    if column :
        result += reflection + 1
    else :
        result += (reflection + 1) * m_rows
 
print('Result = ',result)
# Answer is not 2442