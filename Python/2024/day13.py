# Day 13, Advent of Code 2024

import re
import sympy

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day13_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day13.txt", 'r')

part = 2

def solve(part):
    if part == 1:
        # PART 1

        machines = data_file.read()
        data_file.close()
        
        pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
        
        total = 0
        for match in pattern.finditer(machines) :
            A_x, A_y, B_x, B_y, P_x, P_y = match.group(1,2,3,4,5,6)
            number_of_B = 100
            current_x = number_of_B * int(B_x)
            current_y = number_of_B * int(B_y)
            while number_of_B >= 0 :
                if (int(P_x)-current_x) % int(A_x) == 0 and (int(P_y)-current_y) % int(A_y) == 0 and (int(P_x)-current_x) // int(A_x) == (int(P_y)-current_y) // int(A_y) and (int(P_x)-current_x) // int(A_x) >= 0 :
                    break
                else :
                    current_x -= int(B_x)
                    current_y -= int(B_y)
                    number_of_B -= 1
            if number_of_B >= 0 :
                number_of_A = (int(P_x)-current_x) // int(A_x)
                print(f"Number of A: {number_of_A}, Number of B: {number_of_B}\nTotal: {number_of_A*int(A_x) + number_of_B*int(B_x)}X + {number_of_A*int(A_y) + number_of_B*int(B_y)}Y = {int(P_x)}X + {int(P_y)}Y")
                total += number_of_A*3 + number_of_B
        return total  # Answer is 28059

    elif part == 2:
        # PART 2
        
        machines = data_file.read()
        data_file.close()
        
        pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
        
        # Define variables for calculations
        N_A, N_B = sympy.symbols('N_A N_B', integer=True)
        
        total = 0
        for match in pattern.finditer(machines) :
            A_x, A_y, B_x, B_y, P_x, P_y = match.group(1,2,3,4,5,6)
            P_x = str(int(P_x) + 10000000000000)
            P_y = str(int(P_y) + 10000000000000)
            
            # Solve the system of equations
            eq1 = sympy.Eq(N_A * int(A_x) + N_B * int(B_x), int(P_x))
            eq2 = sympy.Eq(N_A * int(A_y) + N_B * int(B_y), int(P_y))
            solutions = sympy.solve((eq1, eq2), (N_A,N_B), dict=True)
            valid_solutions = [
                (sol[N_A], sol[N_B]) for sol in solutions if sol[N_A] >= 0 and sol[N_B] >= 0
            ]
            
            # Find the minimum token cost
            min_cost = float('inf')
            best_sol = None
            for sol_a, sol_b in valid_solutions:
                cost = 3 * sol_a + sol_b
                if cost < min_cost:
                    min_cost = cost
                    best_sol = (sol_a, sol_b)
            if best_sol:
                number_of_A, number_of_B = best_sol
                total += 3 * number_of_A + number_of_B
                #print(f"Number of A: {number_of_A}, Number of B: {number_of_B}\nTotal: {number_of_A*int(A_x) + number_of_B*int(B_x)}X + {number_of_A*int(A_y) + number_of_B*int(B_y)}Y = {int(P_x)}X + {int(P_y)}Y")
            
            # number_of_B = min(int(P_x) // int(B_x), int(P_y) // int(B_y)) + 1
            # current_x = number_of_B * int(B_x)
            # current_y = number_of_B * int(B_y)
            # print(number_of_B, int(P_x) // int(B_x), int(P_y) // int(B_y))
            # print(current_x, P_x, current_y, P_y)
            # while number_of_B >= 0 :
            #     if (int(P_x)-current_x) % int(A_x) == 0 and (int(P_y)-current_y) % int(A_y) == 0 and (int(P_x)-current_x) // int(A_x) == (int(P_y)-current_y) // int(A_y) and (int(P_x)-current_x) // int(A_x) >= 0 :
            #         break
            #     else :
            #         current_x -= int(B_x)
            #         current_y -= int(B_y)
            #         number_of_B -= 1
            # if number_of_B >= 0 :
            #     number_of_A = (int(P_x)-current_x) // int(A_x)
            #     total += number_of_A*3 + number_of_B
        return total  # Answer is 102255878088512

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
