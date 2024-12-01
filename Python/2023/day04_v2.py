# Day 4, part 1 of Advent of Code 2023

#data_file = open('../../Data/2023/day04_test1.txt', 'r')

data_file = open('../../Data/2023/day04.txt', 'r')
data_lines = []
for line in data_file:
    data = line[:-1].split(':')
    data_lines.append(data[1])
data_file.close()


sum = 0

card = 1
win_scratch = {}
for line in data_lines :
    parts = line.split('|')
    win_numbers = [number for number in parts[0].split(' ') if number != '']
    play_numbers = [number for number in parts[1].split(' ') if number != '' and number in win_numbers]
    
    win_scratch[card] = len(play_numbers)
    card += 1

winning_cards = {}
for card in win_scratch :
    if  card not in winning_cards :
        winning_cards[card] = 1
    else :
        winning_cards[card] += 1
    
    for i in range(1,win_scratch[card]+1) :
        if  card+i not in winning_cards :
            winning_cards[card+i] = winning_cards[card]
        else :
            winning_cards[card+i] += winning_cards[card]
    sum += winning_cards[card]

print('Sum = ', sum)
# Answer is 13768818