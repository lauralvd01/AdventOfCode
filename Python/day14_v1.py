# Day 14, part 1 of Advent of Code 2023

#data_file = open('./Data/day14_test1.txt', 'r')

data_file = open('./Data/day14.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

HEIGHT = len(data_lines)
WIDTH = len(data_lines[0])

class Map :
    def __init__(self,data) :
        self.rocks = []
        self.map = [['.' for j in range(WIDTH)] for i in range(HEIGHT)]
        for i in range(HEIGHT) :
            for j in range(WIDTH) :
                if data[i][j] == '#' :
                    self.map[i][j] = '#'
                elif data[i][j] == 'O' :
                    self.map[i][j] = 'O'
                    self.rocks.append((i,j))
    
    def __repr__(self) :
        return '\n'.join(''.join(c for c in row) for row in self.map)
    
    def find_in_rocks(self,i,j) :
        for index_rock in range(len(self.rocks)) :
            if self.rocks[index_rock] == (i,j) :
                return index_rock
        return -1
    
    def move_rock(self,rock_i,rock_j,i,j) :
        self.map[rock_i][rock_j] = '.'
        self.map[i][j] = 'O'
    
    def tilt_north(self) :
        for i in range(1,HEIGHT) :
            for j in range(WIDTH) :
                index_rock = self.find_in_rocks(i,j)
                if index_rock != -1 :
                    rock_i, rock_j = self.rocks[index_rock]
                    while rock_i > 0 and self.map[rock_i-1][rock_j] == '.' :
                        self.move_rock(rock_i,rock_j,rock_i-1,rock_j)
                        rock_i -= 1
                    self.rocks[index_rock] = (rock_i,rock_j)
    
    def tilt_west(self) :
        for j in range(1,WIDTH) :
            for i in range(HEIGHT) :
                index_rock = self.find_in_rocks(i,j)
                if index_rock != -1 :
                    rock_i, rock_j = self.rocks[index_rock]
                    while rock_j > 0 and self.map[rock_i][rock_j-1] == '.' :
                        self.move_rock(rock_i,rock_j,rock_i,rock_j-1)
                        rock_j -= 1
                    self.rocks[index_rock] = (rock_i,rock_j)
        
    def tilt_south(self) :
        for i in range(HEIGHT-2,-1,-1) :
            for j in range(WIDTH) :
                index_rock = self.find_in_rocks(i,j)
                if index_rock != -1 :
                    rock_i, rock_j = self.rocks[index_rock]
                    while rock_i < HEIGHT-1 and self.map[rock_i+1][rock_j] == '.' :
                        self.move_rock(rock_i,rock_j,rock_i+1,rock_j)
                        rock_i += 1
                    self.rocks[index_rock] = (rock_i,rock_j)
        
    def tilt_east(self) :
        for j in range(WIDTH-2,-1,-1) :
            for i in range(HEIGHT) :
                index_rock = self.find_in_rocks(i,j)
                if index_rock != -1 :
                    rock_i, rock_j = self.rocks[index_rock]
                    while rock_j < WIDTH-1 and self.map[rock_i][rock_j+1] == '.' :
                        self.move_rock(rock_i,rock_j,rock_i,rock_j+1)
                        rock_j += 1
                    self.rocks[index_rock] = (rock_i,rock_j)
    
    def cycle(self,nb) :
        for i in range(nb) :
            self.tilt_north()
            self.tilt_west()
            self.tilt_south()
            self.tilt_east()
                    
map = Map(data_lines)
map.tilt_north()
#print(map)

print('Result = ',sum([HEIGHT-rock[0] for rock in map.rocks]))
# Answer is 108918
