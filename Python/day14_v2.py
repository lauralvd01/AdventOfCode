# Day 14, part 2 of Advent of Code 2023

#data_file = open('./Data/day14_test1.txt', 'r')

data_file = open('./Data/day14.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

HEIGHT = len(data_lines)
WIDTH = len(data_lines[0])


class Map :
    def __init__(self,data) -> None:
        self.map = map = [['.' for j in range(WIDTH)] for i in range(HEIGHT)]
        self.rocks = []
        for i in range(len(data)) :
            for j in range(len(data[i])) :
                if data[i][j] == '#' :
                    self.map[i][j] = '#'
                elif data[i][j] == 'O' :
                    self.rocks.append((i,j))
                    self.map[i][j] = 'O'
    
    def __repr__(self) :
        return '\n'.join([''.join(row) for row in self.map])+'\n'
    
    def move_rock_to(self,previous_i,previous_j,i,j) :
        self.map[previous_i][previous_j] = '.'
        self.map[i][j] = 'O'

    def find_in_rocks(self,i,j) :
        for index in range(len(self.rocks)) :
            if self.rocks[index] == (i,j) :
                return index
        return -1
        
    def tilt_north(self) :
        index_r = 0
        for i in range(1,HEIGHT) :
            for j in range(WIDTH) :
                index = self.rocks.find(i,j)
                if index > 0 :
                    rock_i = i
                    while rock_i > 0 and self.map[rock_i-1][j] == '.' :
                        self.move_rock_to(rock_i,j,i-1,j)
                        rock_i -= 1
                    self.rocks[index] = (rock_i,j)
    
    
    def cycle(self) :
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

map = Map(data_lines)
#print(map)
for i in range(1000000000) :
    map.cycle()
print(map)
print('Result = ',sum([rock.weight for rock in map.rocks]))
# Answer is 
