# Day 19, part 1 of Advent of Code 2023

#data_file = open('./Data/day19_test1.txt', 'r')

data_file = open('./Data/day19.txt', 'r')

data_lines = [line.strip() for line in data_file]
data_file.close()

class Rule :
    def __init__(self, rule) :
        if len(rule.split(':')) > 1 :
            self.attribute = rule[0]
            self.test_sign = rule[1]
            self.compare = int(rule.split(':')[0].split(self.test_sign)[1])
            self.destination = rule.split(':')[1]
        else :
            self.attribute = None
            self.test_sign = None
            self.compare = None
            self.destination = rule
    
    def __repr__(self) :
        if self.attribute == None :
            return f' => {self.destination}'
        return f'if {self.attribute} {self.test_sign} {self.compare} => {self.destination}'
    
    def test(self, rating) :
        if self.attribute == None :
            return True
        if self.test_sign == '>' :
            if self.attribute == 'x' :
                return rating.x > self.compare
            if self.attribute == 'm' :
                return rating.m > self.compare
            if self.attribute == 'a' :
                return rating.a > self.compare
            if self.attribute == 's' :
                return rating.s > self.compare
        if self.test_sign == '<' :
            if self.attribute == 'x' :
                return rating.x < self.compare
            if self.attribute == 'm' :
                return rating.m < self.compare
            if self.attribute == 'a' :
                return rating.a < self.compare
            if self.attribute == 's' :
                return rating.s < self.compare
        return False


class Workflow :
    def __init__(self, line) :
        self.name = line.split('{')[0]
        self.rules = []
        for rule in line.split('{')[1].split('}')[0].split(',') :
            self.rules.append(Rule(rule))
    
    def __repr__(self) :
        return f'{self.name} : {self.rules}'

workflows = {}
l = 0
while data_lines[l] != '' :
    wk = Workflow(data_lines[l])
    workflows[wk.name] = wk
    l += 1


class Rating :
    def __init__(self, line) :
        attributes = line.split('{')[1].split('}')[0].split(',')
        self.x = int(attributes[0].split('=')[1])
        self.m = int(attributes[1].split('=')[1])
        self.a = int(attributes[2].split('=')[1])
        self.s = int(attributes[3].split('=')[1])
        self.state = 'in'
    
    def __repr__(self) :
        return f'(x={self.x}, m={self.m}, a={self.a}, s={self.s}) => {self.state}'
    
    def __eq__(self, other) :
        return self.x == other.x and self.m == other.m and self.a == other.a and self.s == other.s
    
    def score(self) :
        return self.x + self.m + self.a + self.s
    
    def sort(self) :
        rules = workflows[self.state].rules
        for rule in rules :
            if rule.test(self) :
                self.state = rule.destination
                break

ratings = []
l += 1
while l < len(data_lines) :
    ratings.append(Rating(data_lines[l]))
    l += 1

A = []
for rating in ratings :
    while rating.state != 'A' and rating.state != 'R' :
        rating.sort()
        #print(rating)
    if rating.state == 'A' :
        A.append(rating)


print('\nResult = ',sum([rating.score() for rating in A]))
# Answer is 495298
