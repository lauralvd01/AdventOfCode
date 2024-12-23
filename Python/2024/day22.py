# Day 22 - Advent Of Code 2024

# data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day22_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day22.txt", 'r')

part = 2

def process(number) :
    first = ((number*64)^number) % 16777216
    second = (int(first/32)^first) % 16777216
    third = ((second*2048)^second) % 16777216
    return third

def solve(part) :
    if part == 1 :
        # Part 1
        
        secrets_numbers = []
        for line in data_file :
            secrets_numbers.append(int(line.strip()))
        data_file.close()
        
        total = 0
        for i in range(len(secrets_numbers)) :
            secret_number = secrets_numbers[i]
            for n in range(2000) :
                secret_number = process(secret_number)
            total += secret_number
            secrets_numbers[i] = secret_number
        return total # Answer is 14726157693
    
    elif part == 2 :
        # Part 2
        
        secrets_numbers = []
        for line in data_file :
            secrets_numbers.append(int(line.strip()))
        data_file.close()
        
        buyer_sequences = []
        for i in range(len(secrets_numbers)) :
            sequences = {}
            secret_number = secrets_numbers[i]
            last_four_changes = []
            for n in range(2000) :
                # Process the secret number
                new_secret_number = process(secret_number)
                # Calculate the price
                new_price = int(str(new_secret_number)[-1])
                # Calculate the change
                last_four_changes.append(new_price-int(str(secret_number)[-1]))
                # Only keep the last four changes including the current one
                if len(last_four_changes) > 4 :
                    last_four_changes.pop(0)
                # If we have at least four changes, we can calculate the sequence
                if len(last_four_changes) == 4 :
                    sequence = ','.join([str(x) for x in last_four_changes])
                    # If the four changes sequence appear for the first time, it would be the one spoted by the monkey when he searches for it
                    if sequence not in sequences.keys() :
                        sequences[sequence] = new_price
                secret_number = new_secret_number
            buyer_sequences.append(sequences)
        
        
        total = float('-inf')
        possible_sequences = set([sequence for sequences in buyer_sequences for sequence in sequences.keys()])
        for sequence_to_tell in possible_sequences :
            count = 0
            for sequences in buyer_sequences :
                if sequence_to_tell in sequences.keys() :
                    count += sequences[sequence_to_tell]
            if count > total :
                total = count
        
        return total # Answer is 1614
    
    else:
        data_file.close()
        return 'Invalid part'

print(solve(part))
