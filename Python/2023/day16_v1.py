# Day 16, part 1 of Advent of Code 2023

data_file = open('./Data/2023/day16_test1.txt', 'r')

#data_file = open('./Data/2023/day16.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

map = [[(c,False) for c in line] for line in data_lines]
beams = []

class Beam :
    def __init__(self,i,j,direction) :
        self.i = i
        self.j = j
        self.direction = direction
        if 0 <= self.i and self.i < len(map) and 0 <= self.j and self.j < len(map[0]) :
            self.alive = True
        else :
            self.alive = False
        if self.alive : map[self.i][self.j] = (map[self.i][self.j][0],True)
    
    def __repr__(self) :
        return f'Beam({self.i},{self.j},{self.direction},{self.alive})'

    def go_next(self) :
        assert self.alive
        map[self.i][self.j] = (map[self.i][self.j][0],True)
        if self.direction == 'right' :
            if self.j+1 < len(map[0]) :
                next = map[self.i][self.j+1][0]
                map[self.i][self.j+1] = (next,True)
                self.j += 1
                if next == '/' :
                    self.direction = 'up'
                elif next == '\\' :
                    self.direction = 'down'
                elif next == '|' :
                    self.direction = 'up'
                    beams.append(Beam(self.i,self.j,'down'))
            else :
                self.alive = False
        elif self.direction == 'left' :
            if self.j > 0 :
                next = map[self.i][self.j-1][0]
                map[self.i][self.j-1] = (next,True)
                self.j -= 1
                if next == '/' :
                    self.direction = 'down'
                elif next == '\\' :
                    self.direction = 'up'
                elif next == '|' :
                    self.direction = 'down'
                    beams.append(Beam(self.i,self.j,'up'))
            else :
                self.alive = False
        elif self.direction == 'up' :
            if self.i > 0 :
                next = map[self.i-1][self.j][0]
                map[self.i-1][self.j] = (next,True)
                self.i -= 1
                if next == '/' :
                    self.direction = 'right'
                elif next == '\\' :
                    self.direction = 'left'
                elif next == '-' :
                    self.direction = 'left'
                    beams.append(Beam(self.i,self.j,'right'))
            else :
                self.alive = False
        elif self.direction == 'down' :
            if self.i+1 < len(map) :
                next = map[self.i+1][self.j][0]
                map[self.i+1][self.j] = (next,True)
                self.i += 1
                if next == '/' :
                    self.direction = 'left'
                elif next == '\\' :
                    self.direction = 'right'
                elif next == '-' :
                    self.direction = 'left'
                    beams.append(Beam(self.i,self.j,'right'))
            else :
                self.alive = False

beams.append(Beam(0,0,'right'))
while len(beams) > 0 :
    beam = beams[0]
    if beam.alive :
        beam.go_next()
    if not beam.alive :
        beams.remove(beam)
    print('\n'.join([''.join(['#' if bool else c for (c,bool) in line]) for line in map]))
    print()

print('Result = ',sum([sum([1 for (c,bool) in line if bool]) for line in map]))
# Answer is 510801
