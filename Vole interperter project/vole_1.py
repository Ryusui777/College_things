def test(instruction_file):
#######################################################################
    #inizializing memory locations
    f = open(instruction_file,'r')
    hex_combinations = [format(i, '02x') for i in range(256)]
    memory = {}
    for inizialize_line in hex_combinations:
        memory[f'{inizialize_line}'] = ''
    inizialize = False
    for mem_space in f:
        val_com = ''
        if inizialize:
            for char in range(len(mem_space)):
                if char != '\n':
                    val_com += mem_space[char]
            space = ''
            val = ''
            for i in range(2):
                space += val_com[i]
                val += val_com[i+3]
            memory[space] = val
        if mem_space == 'memory\n':
            inizialize = True
    f.close()
    memory_location = []
########################################################################
    #Placing instructions in memory
    instruciones = []
    f = open(instruction_file,'r')
    done = False
    for instruccion in f:
        comparing_value = ''
        for char in range(len(instruccion)-1):
            comparing_value += instruccion[char]

        if comparing_value == 'memory':
            done = True

        if not done:
            inserting_val = ''
            for x in range(6):
                inserting_val += instruccion[x]
            instruciones.append(inserting_val)
    iterador = 0
    for inserting in instruciones:
        memory[f'{hex_combinations[iterador]}'] = inserting
        memory_location.append(hex_combinations[iterador])
        del memory[hex_combinations[iterador+1]]
        iterador += 2
    f.close()
#############################################################################
    #inizializando registros
    hex_numbers = [format(i, 'x') for i in range(16)]
    registros = {}
    for num_registro in hex_numbers:
        registros[f'{num_registro}'] = ''
#############################################################################
    # Instructions
    def load_mem(instruccion):
        value = memory[f'{instruccion[4]}{instruccion[5]}']
        registros[f'{instruccion[3]}'] = value
    def jump(instruccion):
        if registros['0'] == registros[f'{instruccion[3]}']:
            return True
    def load_bit(instruccion):
        value = instruccion[4]
        value += instruccion[5]
        registros[f'{instruccion[3]}'] = value
    def store(instruccion):
        memory[f'{instruccion[4]}{instruccion[5]}'] = registros[f'{instruccion[3]}']
    def move(instruccion):
        registros[f'{instruccion[4]}'] = registros[f'{instruccion[5]}']
        registros[f'{instruccion[5]}'] = ''
    def complemento_2(instruccion):

        a = registros[f'{instruccion[4]}']
        b = registros[f'{instruccion[5]}']
        a = int(a, 16)
        b = int(b, 16)
        num_bits = 8  # Specify the number of bits you want
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
        memory_location = registros[f'{instruccion[5]}']
        registros[f'{instruccion[4]}'] = memory[f'{memory_location}']
###############################################################################
    # Insructions decoding
    halt = False
    start_pos = 0
    while not halt:
        for ins_pos in range(start_pos,len(memory_location)):
            instruccion = memory[memory_location[ins_pos]]
            match instruccion[2]:
                case '1':
                    load_mem(instruccion)
                case'2':
                    load_bit(instruccion)
                case'3':
                    store(instruccion)
                case '4':
                    move(instruccion)
                case '5':
                    complemento_2(instruccion)
                case'b':
                    if jump(instruccion):
                        espacio = ''
                        espacio += instruccion[4]
                        espacio += instruccion[5]
                        start_pos = memory_location.index(espacio)
                        break
                case'c':
                    halt = True
                    break
                case 'd':
                    pointer_load(instruccion)
################################################################################
    #printing registers
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
    #printing memory
    iterador = 0
    print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
    for prt in memory:
        memory_position = ''
        if memory[prt] != '' and iterador != 256:
            if len(memory[prt]) == 6:
                memory_position += f'| Memory Position | 0x{hex_combinations[iterador]} | {memory[prt]} |'
                iterador += 1
            else:

                memory_position += f'| Memory Position | 0x{hex_combinations[iterador]} | {memory[prt]}     |'

            print(memory_position)

        iterador += 1
    print("º'''''''''''''''''''''''''''''''''º")
#################################################################################
test('demofile.txt.txt')