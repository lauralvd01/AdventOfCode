# Day 17, Advent of Code 2024

#data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day17_test.txt", 'r')
data_file = open("C:\\Users\\LauraLvd\\Documents\\PRO\\AdventOfCode\\Data\\2024\\day17.txt", 'r')

part = 2

A = None
B = None
C = None

def get_combo_operand(number) :
    if 0 <= number <= 3 :
        return number
    if number == 4 :
        return A
    if number == 5 :
        return B
    if number == 6 :
        return C
    if number == 7 :
        print('ERROR: Trying to access operand 7')
        return None
    
    print('ERROR: Trying to access operand', number)
    return None

def adv(operand) :
    global A
    numerator = A
    denominator = 2**get_combo_operand(operand)
    A = numerator // denominator
    return None

def bxl(operand) :
    global B
    first = B
    second = operand
    B = first ^ second
    return None

def bst(operand) :
    global B
    B = get_combo_operand(operand) % 8
    return None

def jnz(operand, instruction_pointer) :
    global A
    if A == 0 :
        return None, instruction_pointer+2
    return None, operand

def bxc() :
    global B
    global C
    B = B ^ C
    return None

def out(operand) :
    return get_combo_operand(operand) % 8

def bdv(operand) :
    global A
    global B
    numerator = A
    denominator = 2**get_combo_operand(operand)
    B = numerator // denominator
    return None

def cdv(operand) :
    global A
    global C
    numerator = A
    denominator = 2**get_combo_operand(operand)
    C = numerator // denominator
    return None

def perform_instruction(opcode, operand, instruction_pointer) :
    if opcode == 0 :
        return adv(operand), instruction_pointer+2
    if opcode == 1 :
        return bxl(operand), instruction_pointer+2
    if opcode == 2 :
        return bst(operand), instruction_pointer+2
    if opcode == 3 :
        return jnz(operand, instruction_pointer)
    if opcode == 4 :
        return bxc(), instruction_pointer+2
    if opcode == 5 :
        return out(operand), instruction_pointer+2
    if opcode == 6 :
        return bdv(operand), instruction_pointer+2
    if opcode == 7 :
        return cdv(operand), instruction_pointer+2
    
    print('ERROR: Unknown opcode ', opcode, ' at position ', instruction_pointer)
    return None, instruction_pointer+2

def solve(part):
    global A
    global B
    global C
    
    if part == 1:
        # PART 1
        
        data = data_file.read().split('\n\n')
        data_file.close()
        A = int(data[0].split('\n')[0][12:])
        B = int(data[0].split('\n')[1][12:])
        C = int(data[0].split('\n')[2][12:])
        
        program = data[1][9:].split(',')

        instruction_pointer = 0
        ouputs = []
        while instruction_pointer < len(program) :
            opcode = int(program[instruction_pointer])
            operand = int(program[instruction_pointer+1])
            output, instruction_pointer = perform_instruction(opcode, operand, instruction_pointer)
            if output != None :
                ouputs.append(output)
        
        total = ','.join([str(ouput) for ouput in ouputs])
        return total  # Answer is 7,6,5,3,6,5,7,0,4

    elif part == 2:
        # PART 2
        
        data = data_file.read().split('\n\n')
        data_file.close()
        A = int(data[0].split('\n')[1][12:])
        B = int(data[0].split('\n')[1][12:])
        C = int(data[0].split('\n')[2][12:])
        
        program = data[1][9:].split(',')

        #################################################################### WORKS WITH THE EXAMPLE
        # ouputs = []
        # a = 0
        # while ','.join([str(ouput) for ouput in ouputs]) != ','.join(program) :
        #     A = a
        #     instruction_pointer = 0
        #     ouputs = []
        #     while instruction_pointer < len(program) :
        #         opcode = int(program[instruction_pointer])
        #         operand = int(program[instruction_pointer+1])
        #         output, instruction_pointer = perform_instruction(opcode, operand, instruction_pointer)
        #         if output != None :
        #             ouputs.append(output)
        #     print(a, ','.join([str(ouput) for ouput in ouputs]))
        #     a += 1
        
        # total = a
        

        #################################################################### FOR THE PUZZLE INPUT
        # A = ?, B = 0, C = 0
        # Program: 2,4, 1,2, 7,5, 0,3, 1,7, 4,1, 5,5, 3,0
        # 
        # One jump instruction : 3,0 => The program will repeat entirely until A = 0 at the end
        # One out intruction : 5,5 => One and only one output will be generated at each iteration
        # ==> To ouput an exact copy of the program, A must be set so that the program iterate exactly len(program) times
        # ==> A must be set so that the program iterate 16 times and terminates with A = 0
        #
        # One instruction that modifies A : 0,3 => A = A // 2**3 = A // 8
        # ==> If A = a15 + 8 * a14 + 8^2 * a13 + ... + 8^14 * a1 + 8^15 * a0 at the beginning of the first iteration,
        # ==> Then A = a14 + 8 * a13 + 8^2 * a12 + ... + 8^13 * a1 + 8^14 * a0 at the end of the first iteration
        # ==> And A is set to a14 + 8 * a13 + 8^2 * a12 + ... + 8^13 * a1 + 8^14 * a0 at the beginning of the second iteration
        # And so on until A = 0 at the end of the 16th iteration 
        # (a0, a1, ... a15 are integers between 0 and 7)
        #
        # The first instruction is 2,4 : B = get_combo_operand(4) % 8 = A % 8
        # With A the last value of A in the previous iteration
        # ==> At the beginning of the iteration i, B = (a(16-i) + 8 * a(16-i-1) + ... + 8^(16-i) * a0) % 8 = a(16-i)
        # 
        # SO
        # If A = a0 is the correct input so that the program iterate one time and returns the correct output (program[-1] = "0")
        # We can search a1 so that with A = a1 + 8 * a0, the first iteration returns the correct output (program[-2] = "3")
        # And then at the end of the first iteration, A = a0 and the second iteration gives the correct output (program[-1] = "0")
        # => A = a1 + 8 * a0 will be the correct input so that the program iterate two times and returns the correct output (program[-2:] = "3,0")
        # And so on :
        # With the correct a0, a1, ... a15, the program will iterate 16 times and return the correct output : the program.

        a_possibilities = [0]
        for i in range(len(program)) :
            new_possibilities = []
            for a in a_possibilities :
                # Search of a(i) so that the program iterate i times and returns the correct output programs[-i:]
                a_i_possibilities = []
                for a_i in range(8) :
                    A = a_i + 8 * a
                    instruction_pointer = 0
                    ouputs = []
                    while instruction_pointer < len(program) :
                        opcode = int(program[instruction_pointer])
                        operand = int(program[instruction_pointer+1])
                        output, instruction_pointer = perform_instruction(opcode, operand, instruction_pointer)
                        if output != None :
                            ouputs.append(output)
                    
                    # print(a, a_i, ','.join([str(ouput) for ouput in ouputs]), ','.join(program[len(program)-1-i:]))
                    if ','.join([str(ouput) for ouput in ouputs]) == ','.join(program[len(program)-1-i:]) :
                        a_i_possibilities.append(a_i)
                        # print(a,a_i)
                
                for a_i in a_i_possibilities :
                    new_possibilities.append(a_i + 8 * a)
            a_possibilities = new_possibilities
                
        # print(a_possibilities)
        return min(a_possibilities)  # Answer is 190615597431823
    
    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
