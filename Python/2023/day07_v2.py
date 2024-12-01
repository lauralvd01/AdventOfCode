# Day 7, part 2 of Advent of Code 2023

#data_file = open('./Data/2023/day07_test1.txt', 'r')

data_file = open('./Data/2023/day07.txt', 'r')

data_lines = [line[:-1].strip() for line in data_file]
data_file.close()

class Hand :
    
    CARDS = {'J':-1,'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'Q':10,'K':11,'A':12}
    TYPES = {'none':0,'one':1,'two':3,'three':4,'full':5,'four':6,'five':7}
    
    def __init__(self, hand) :
        self.hand = hand
        
        counts = {}
        for c in hand :
            if c in counts :
                counts[c] += 1
            else :
                counts[c] = 1
        
        if 'J' not in counts.keys() :
            if len(counts) == 1 :
                self.type = 'five'
            elif len(counts) == 2 :
                if 4 in counts.values() :
                    self.type = 'four'
                else :
                    self.type = 'full'
            elif len(counts) == 3 :
                if 3 in counts.values() :
                    self.type = 'three'
                else :
                    self.type = 'two'
            elif len(counts) == 4 :
                self.type = 'one'
            else :
                self.type = 'none'
        
        elif counts['J'] == 1 :
            if len(counts) == 2 :
                self.type = 'five'
            elif len(counts) == 3 :
                if 3 in counts.values() :
                    self.type = 'four'
                else :
                    self.type = 'full'
            elif len(counts) == 4 :
                if 2 in counts.values() :
                    self.type = 'three'
                else :
                    self.type = 'two'
            else :
                self.type = 'one'
            
        elif counts['J'] == 2 :
            counts_J = {}
            for card in counts :
                if card != 'J' :
                    counts_J[card] = counts[card]
            if len(counts) == 2 :
                self.type = 'five'
            elif len(counts) == 3 :
                if 2 in counts_J.values() :
                    self.type = 'four'
                else :
                    self.type = 'full'
            else :
                self.type = 'three'
        
        elif counts['J'] == 3 :
            if len(counts) == 2 :
                self.type = 'five'
            else :
                self.type = 'four'
        
        else :
            self.type = 'five'
    
    def __lt__(self,hand2) :
        if self.type != hand2.type :
            return self.TYPES[self.type] < self.TYPES[hand2.type]
        else :
            for i in range(5) :
                if self.hand[i] != hand2.hand[i] :
                    return self.CARDS[self.hand[i]] < self.CARDS[hand2.hand[i]]
            

hands = {}
for line in data_lines :
    hands[int(line.split(" ")[1])] = Hand(line.split(" ")[0])

ranked = dict(sorted(hands.items(), key= lambda item : item[1]))

result = 0
rank = 1
for hand in ranked.keys() :
    result += rank*hand
    rank += 1

print('Result = ',result)
# Answer is 248256639