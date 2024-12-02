# Day 2, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day02_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day02.txt", 'r')

part = 2

def solve(part) :
    if part == 1 :
        # PART 1

        safe_count = 0
        for line in data_file:
            report = line.strip().split(' ')
            safe = True
            increasing = (int(report[0]) <= int(report[1]))
            j = 1
            while j < len(report) and safe :
                if increasing :
                    safe = (int(report[j-1]) <= int(report[j]))
                    safe = safe and (1 <= int(report[j]) - int(report[j-1]) <= 3)
                else :
                    safe = (int(report[j-1]) >= int(report[j]))
                    safe = safe and (1 <= int(report[j-1]) - int(report[j]) <= 3)
                j += 1
            if safe : safe_count += 1
        data_file.close()

        return safe_count  # Answer is 314
    
    elif part == 2 :
        # PART 2

        safe_count = 0
        for line in data_file:
            report = line.strip().split(' ')
            safe = True
            increasing = (int(report[0]) <= int(report[1]))
            j = 1
            while j < len(report) and safe :
                if increasing :
                    safe = (int(report[j-1]) <= int(report[j]))
                    safe = safe and (1 <= int(report[j]) - int(report[j-1]) <= 3)
                else :
                    safe = (int(report[j-1]) >= int(report[j]))
                    safe = safe and (1 <= int(report[j-1]) - int(report[j]) <= 3)
                j += 1
            
            if not safe :
                removed_one = 0
                while not safe and removed_one < len(report) :
                    new_report = report[:removed_one] + report[removed_one+1:]
                    new_increasing = (int(new_report[0]) <= int(new_report[1]))
                    j = 1
                    new_safe = True
                    while j < len(new_report) and new_safe :
                        if new_increasing :
                            safe = (int(new_report[j-1]) <= int(new_report[j]))
                            new_safe = new_safe and (1 <= int(new_report[j]) - int(new_report[j-1]) <= 3)
                        else :
                            new_safe = (int(new_report[j-1]) >= int(new_report[j]))
                            new_safe = new_safe and (1 <= int(new_report[j-1]) - int(new_report[j]) <= 3)
                        j += 1
                    removed_one += 1
                    safe = new_safe
            if safe : safe_count += 1
        data_file.close()

        return safe_count  # Answer is 373
    
    else :
        return 'Invalid part'
    
print(solve(part))