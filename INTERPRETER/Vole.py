

usr_file = 'lets_see.txt'
def problem_detected(instruccion, problem_num):
    match problem_num:
        case '0':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 0:                                  |')
            print(f"|    Promblems with line number {instruccion}     |")
            print(f"|    The lenth? Invalid charachter?        |")
            print("|                                           |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '203':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 203:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    There's nothing in resgister {instruccion[4]} -^      |")
            print("|    Register empty                         |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")

        case '102':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 102:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't move '{registros[instruccion[5]]}' to register '{instruccion[4]}'       |")
            print("|    Invalid value                          |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '101':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 101:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't load '{instruccion[4]}{instruccion[5]}' to register '{instruccion[3]}'     |")
            print("|    Invalid value                          |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '605':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 605:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't jump to instruction '{instruccion[4]}{instruccion[5]}'      |")
            print("|    It isn't an instruction                |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '600':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 600:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't  compare register {instruccion[3]} --^       |")
            print("|    Register doesn't exist                 |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '406':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 406:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't find register {instruccion[3]} ------^       |")
            print("|    Register doesn't exist                 |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '507':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 507:                                     |')
            print(f"|    Promblems with instruction: {instruccion}          |")
            print(f"|    There's nothing in memory location  '{instruccion[4]}{instruccion[5]}'    |")
            print("|    Memory location empty                       |")
            print('|                                                |')
            print("º''''''''''''''''''''''''''''''''''''''''''''''''º")
        case '506':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 506:                               |')
            print(f"|    Promblems with instruction: {instruccion}    |")
            print(f"|    Couldn't find memory location '{instruccion[4]}{instruccion[5]}'    |")
            print("|    Memory location doesn't exist         |")
            print('|                                          |')
            print("º''''''''''''''''''''''''''''''''''''''''''º")
        case '500':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 500:                                     |')
            print(f"|    Promblems with instruction: {instruccion}          |")
            print(f"|    There's nothing in memory location  '{registros[instruccion[5]]}'    |")
            print("|    Memory location empty                       |")
            print('|                                                |')
            print("º''''''''''''''''''''''''''''''''''''''''''''''''º")
        case '505':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 505:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't find memory location:  '{registros[instruccion[5]]}'   |")
            print("|    Memory location doesn't exist          |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '202':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 202:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    There's nothing in resgister {instruccion[5]} --^     |")
            print("|    Register empty                         |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '405':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 405:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't find register {instruccion[5]} --------^     |")
            print("|    Register doesn't exist                 |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
        case '404':
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| Error 404:                                |')
            print(f"|    Promblems with instruction: {instruccion}     |")
            print(f"|    Couldn't find register {instruccion[4]} -------^      |")
            print("|    Register doesn't exist                 |")
            print('|                                           |')
            print("º'''''''''''''''''''''''''''''''''''''''''''º")
    global problem
    problem = True
def inizializer(execution_file):
    global problem
    problem = False
    global instruction_set
    instruction_set = []
    global memory
    memory = {}
    global registros
    global hex_numbers
    hex_numbers = [format(i, 'x') for i in range(16)]
    registros = {}
    for num_registro in hex_numbers:
        registros[f'{num_registro}'] = ''
    main = False
    memory_inizialize = False
    global hex_combinations
    hex_combinations = [format(i, '02X') for i in range(256)]

    for inizialize_space in hex_combinations:
        memory[inizialize_space] = ''
    File = open(execution_file, 'r')
    breaking = False
    iteration = 0
    for line in File:
        #instructions
        if line[0] == '}':
            main = False
            iterador = 0
            for instruction in range(len(instruction_set)):
                memory[hex_combinations[iterador]] = instruction_set[instruction]
                iterador += 2
            global instruction_new
            instruction_new = []
            iterador = 0
            for i in range(len(instruction_set)):
                instruction_new.append(hex_combinations[iterador])
                iterador += 2
        if main:

            if line[0:2] == '0x':
                instruction_set.append(line[:6])
        if line[:7] == 'main(){':
            main = True
        # Memory
        if memory_inizialize and line[0:2] in hex_combinations:
            value = False
            for char in range(2,len(line)):
                if value and line[char] not in (' ', '\n'):
                    memory[line[0:2]] = line[char:char+2]
                    break
                if line[char] == '=':
                    value = True
        if line[:20] == 'memory.inizialize(){':
            memory_inizialize = True
        if breaking:
            break
        iteration += 1
inizializer(usr_file)
##############################
def load_mem(instruccion):
    global registros
    global memory
    global hex_combinations
    value = memory.get(f'{instruccion[4]}{instruccion[5]}', "NOPE")
    if value == "NOPE":
        problem_detected(instruccion, '506')
    elif value == "":
        problem_detected(instruccion, '507')
    elif registros.get(instruccion[3], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '406')
    else:
        registros[f'{instruccion[3]}'] = value
def jump(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[3], "NOPE") == 'NOPE':
        problem_detected(instruccion, '600')
    elif f'{instruccion[4]}{instruccion[5]}' not in memory_location:
        problem_detected(instruccion, '605')
    elif registros['0'] == registros[f'{instruccion[3]}']:
        return True
def load_bit(instruccion):
    global registros
    global memory
    global hex_combinations
    value = instruccion[4:]
    if value not in hex_combinations:
        problem_detected(instruccion, '101')
    elif registros.get(instruccion[3], "NOPE") == 'NOPE':
        problem_detected(instruccion, '406')
    else:
        registros[f'{instruccion[3]}'] = value
def store(instruccion):
    global registros
    global memory
    global hex_combinations
    if memory.get(f'{instruccion[4]}{instruccion[5]}', "NOPE") == 'NOPE':
        problem_detected(instruccion, '506')
    elif registros.get(instruccion[3], "NOPE") == 'NOPE':
        problem_detected(instruccion, '406')
    elif registros.get(instruccion[3]) == '':
        problem_detected(instruccion, '202')
    else:
        memory[f'{instruccion[4]}{instruccion[5]}'] = registros[f'{instruccion[3]}']
def move(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[4], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '404')
    elif registros.get(instruccion[5], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '405')
    else:
        registros[f'{instruccion[4]}'] = registros[f'{instruccion[5]}']
        registros[f'{instruccion[5]}'] = ''
def complemento_2(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[4], "NOPE") == 'NOPE':
        problem_detected(instruccion, '404')
    elif registros.get(instruccion[5], "NOPE") == 'NOPE':
        problem_detected(instruccion, '405')
    elif registros.get(instruccion[3], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '406')
    else:
        a = int(registros[f'{instruccion[4]}'], 16)
        b = int(registros[f'{instruccion[5]}'], 16)
        num_bits = 8
        a = format(a, f'0{num_bits}b')
        b = format(b, f'0{num_bits}b')
        iterador = 7
        c = 0
        char = ''
        for i in a[::-1]:
            sum = int(i) + int(b[iterador]) + int(c)
            if sum == 0:
                char += '0'
            if sum == 1:
                char += '1'
                c = 0
            if sum == 2:
                char += '0'
                c = 1
            if sum == 3:
                char += '1'
                c = 1
            iterador -= 1
        char_2 = ''
        for reversing in char[::-1]:
            char_2 += reversing
        char_2 = int(char_2, 2)
        char_2 = format(char_2, '02x')
        if len(char_2) == 2:
            registros[f'{instruccion[3]}'] = char_2
        else:
            print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
            print('| OVERFLOW | instruction |', instruccion, "|")
            print("º'''''''''''''''''''''''''''''''''º")
def pointer_load(instruccion):
    global registros
    global memory
    global hex_combinations
    memory_location = registros.get(instruccion[5], "NOPE")
    if memory_location == 'NOPE':
        problem_detected(instruccion, '405')
    elif memory_location == '':
        problem_detected(instruccion, '202')

    elif memory.get(memory_location, 'NOPE') == "NOPE":
        problem_detected(instruccion, '505')

    elif memory.get(memory_location) == '':
        problem_detected(instruccion, '500')
    else:
        registros[f'{instruccion[4]}'] = memory[f'{memory_location}']
def and_comp(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[4], "NOPE") == 'NOPE':
        problem_detected(instruccion, '404')
    elif registros.get(instruccion[5], "NOPE") == 'NOPE':
        problem_detected(instruccion, '405')
    elif registros.get(instruccion[3], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '406')
    elif registros.get(instruccion[4]) == '':
        problem_detected(instruccion, '203')
    elif registros.get(instruccion[5]) == '':
        problem_detected(instruccion, '202')
    else:
        a = int(registros[f'{instruccion[4]}'], 16)
        b = int(registros[f'{instruccion[5]}'], 16)
        num_bits = 8
        a = format(a, f'0{num_bits}b')
        b = format(b, f'0{num_bits}b')
        c = ''
        for bit in range(len(a)):
            if a[bit] == '1' and b[bit] == '1':
                c += '1'
            else:
                c += '0'
        c = int(c, 2)
        c = format(c, '02x')
        registros[f'{instruccion[3]}'] = c
def or_comp(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[4], "NOPE") == 'NOPE':
        problem_detected(instruccion, '404')
    elif registros.get(instruccion[5], "NOPE") == 'NOPE':
        problem_detected(instruccion, '405')
    elif registros.get(instruccion[3], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '406')
    elif registros.get(instruccion[4]) == '':
        problem_detected(instruccion, '203')
    elif registros.get(instruccion[5]) == '':
        problem_detected(instruccion, '202')
    else:
        a = int(registros[instruccion[4]], 16)
        b = int(registros[instruccion[5]], 16)
        num_bits = 8
        a = format(a, f'0{num_bits}b')
        b = format(b, f'0{num_bits}b')
        c = ''
        for bit in range(len(a)):
            if a[bit] == '1' or b[bit] == '1':
                c += '1'
            else:
                c += '0'
        c = int(c, 2)
        c = format(c, '02x')
        registros[f'{instruccion[3]}'] = c
def xor_comp(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[4], "NOPE") == 'NOPE':
        problem_detected(instruccion, '404')
    elif registros.get(instruccion[5], "NOPE") == 'NOPE':
        problem_detected(instruccion, '405')
    elif registros.get(instruccion[3], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '406')
    elif registros.get(instruccion[4]) == '':
        problem_detected(instruccion, '203')
    elif registros.get(instruccion[5]) == '':
        problem_detected(instruccion, '202')
    else:
        a = int(registros[instruccion[4]], 16)
        b = int(registros[instruccion[5]], 16)
        num_bits = 8
        a = format(a, f'0{num_bits}b')
        b = format(b, f'0{num_bits}b')
        c = ''
        for bit in range(len(a)):
            if a[bit] == '1' and b[bit] == '0':
                c += '1'
            elif a[bit] == '0' and b[bit] == '1':
                c += '1'
            else:
                c += '0'
        c = int(c, 2)
        c = format(c, '02x')
        registros[f'{instruccion[3]}'] = c
def rotate(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[3], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '406')
    else:
        a = int(registros[f'{instruccion[3]}'], 16)
        num_bits = 8
        a = format(a, f'0{num_bits}b')
        for rotations in range(int(instruccion[5])):
            byte = []
            byte_1 = ''
            for bit in a:
                byte.append(bit)
            a = a[7]
            for bit in range(len(byte) - 1):
                a += byte[bit]
        a = int(a, 2)
        a = format(a, '02x')
        registros[instruccion[3]] = a
def sum_float(instruccion):
    global registros
    global memory
    global hex_combinations
    if registros.get(instruccion[4], "NOPE") == 'NOPE':
        problem_detected(instruccion, '404')
    elif registros.get(instruccion[5], "NOPE") == 'NOPE':
        problem_detected(instruccion, '405')
    elif registros.get(instruccion[3], 'NOPE') == 'NOPE':
        problem_detected(instruccion, '406')
    else:
        a = int(registros[instruccion[4]], 16)
        b = int(registros[instruccion[5]], 16)
        num_bits = 8
        a = format(a, f'0{num_bits}b')
        b = format(b, f'0{num_bits}b')
        # getting exponent
        bias = -3
        first_exponent = int(a[1:4], 2) + bias
        secound_exponent = int(b[1:4], 2) + bias
        # getting mantisa
        mantisa_1 = a[4:]
        mantisa_2 = b[4:]
        if first_exponent > secound_exponent:
            mantisa_2 = '0' * (first_exponent - secound_exponent) + mantisa_2
            final_exponent = first_exponent + 3
        elif secound_exponent > first_exponent:
            mantisa_1 = '0' * (secound_exponent - first_exponent) + mantisa_1
            final_exponent = secound_exponent + 3
        else:
            final_exponent = first_exponent + 3
        c = 0
        char = ''
        iterador = 3
        # adding
        if len(mantisa_2) < len(mantisa_1):
            for i in mantisa_2[::-1]:
                sum = int(i) + int(mantisa_1[iterador]) + int(c)
                if sum == 0:
                    char += '0'
                    c = 0
                if sum == 1:
                    char += '1'
                    c = 0
                if sum == 2:
                    char += '0'
                    c = 1
                if sum == 3:
                    char += '1'
                    c = 1
                iterador -= 1
            final = f'{b[0]}'
        if len(mantisa_2) >= len(mantisa_1):
            for i in mantisa_1[::-1]:
                sum = int(i) + int(mantisa_2[iterador]) + int(c)
                if sum == 0:
                    char += '0'
                if sum == 1:
                    char += '1'
                    c = 0
                if sum == 2:
                    char += '0'
                    c = 1
                if sum == 3:
                    char += '1'
                    c = 1
                iterador -= 1
            final = f'{a[0]}'
        final += str(format(final_exponent, f'0{3}b'))
        char_2 = char[::-1]
        final += char_2[0:4]
        if a == "00000000":
            final = b
        if b == '00000000':
            final = a
        final = int(final, 2)
        final = format(final, '02x')
        registros[instruccion[3]] = final
def main_execution():
    global memory
    global instruction_set
    halt = False
    start_pos = 0
    while not halt and not problem:
        for ins_pos in range(start_pos, len(instruction_set)):
            instruccion = memory[instruction_new[ins_pos]]
            if problem:
                break
            match instruccion[2]:
                case '1':
                    load_mem(instruccion)
                case '2':
                    load_bit(instruccion)
                case '3':
                    store(instruccion)
                case '4':
                    move(instruccion)
                case '5':
                    complemento_2(instruccion)
                case '6':
                    sum_float(instruccion)
                case '7':
                    or_comp(instruccion)
                case '8':
                    and_comp(instruccion)
                case '9':
                    xor_comp(instruccion)
                case 'a':
                    rotate(instruccion)
                case 'b':
                    if jump(instruccion):
                        espacio = instruccion[4:5]
                        start_pos = instruction_set.index(espacio)
                        break
                case 'c':
                    halt = True
                    break
                case 'd':
                    pointer_load(instruccion)
    finish_execution()
def finish_execution():
    if not problem:
        # printing registers
        iterador = 0
        print('.,,,,,,,,,,,,,,,,,,,,,.')
        for prt in registros:
            registers = ''
            if registros[prt] != '' and iterador != 16:
                registers += f"| Registro | 0x{hex_numbers[iterador]} | {registros[prt]} |"
                print(registers)

            iterador += 1
        print("º'''''''''''''''''''''º")
        ################################################################################
        # printing memory
        iterador = 0
        print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
        for prt in memory:
            memory_position = ''
            if memory[prt] != '' and iterador != 256:
                if len(memory[prt]) == 6:
                    memory_position += f'| Memory Position | 0x{hex_combinations[iterador]} | {memory[prt]} |'
                    iterador += 1
                else:
                    memory_position += f'| Memory Position | 0x{hex_combinations[iterador]} |   {memory[prt]}   |'
                print(memory_position)

            iterador += 1
        print("º'''''''''''''''''''''''''''''''''º")
main_execution()
