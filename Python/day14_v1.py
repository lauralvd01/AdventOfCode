# Day 14, part 1 of Advent of Code 2023

#data_file = open('./Data/day14_test1.txt', 'r')

data_file = open('./Data/day14.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

MAX_WEIGHT = len(data_lines)
WIDTH = len(data_lines[0])

class Rock :
    def __init__(self,i,j) :
        self.weight = MAX_WEIGHT-i
        self.column = j
    
    def __repr__(self) :
        return f"Rock {MAX_WEIGHT-self.weight},{self.column} : Weight {self.weight}"

class Map :
    def __init__(self,data) -> None:
        self.map = map = [['.' for j in range(WIDTH)] for i in range(MAX_WEIGHT)]
        self.fixed_rocks = []
        self.rocks = []
        for i in range(len(data)) :
            for j in range(len(data[i])) :
                if data[i][j] == '#' :
                    self.fixed_rocks.append((i,j))
                    self.map[i][j] = '#'
                elif data[i][j] == 'O' :
                    self.rocks.append(Rock(i,j))
                    self.map[i][j] = 'O'
    
    def __repr__(self) :
        return '\n'.join([''.join(row) for row in self.map])+'\n'
    
    def move_rock_to(self,rock,i,j) :
        self.map[MAX_WEIGHT-rock.weight][rock.column] = '.'
        self.map[i][j] = 'O'

    def title(self) :
        for r in range(len(self.rocks)) :
            i = MAX_WEIGHT-self.rocks[r].weight
            j = self.rocks[r].column
            if i > 0 :
                while i > 0 and self.map[i-1][j] == '.' :
                    self.move_rock_to(self.rocks[r],i-1,j)
                    self.rocks[r].weight += 1
                    i -= 1
        self.rocks.sort(key=lambda rock: MAX_WEIGHT-rock.weight)

map = Map(data_lines)
#print(map)
map.title()
#print(map)
print('Result = ',sum([rock.weight for rock in map.rocks]))
# Answer is 
