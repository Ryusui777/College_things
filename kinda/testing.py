# 1: test works by creating a file with vole instructions and a diccionary with preestablish memory positions
# memory diccionary can be like = {'a0': 'af'} which then will be storage in the memory position 'a0' with the value 'af'

# 2: for the file it has to be a txt file, like 'instructions.txt', and has to be inputed between '' like 'instructions.txt'
# and each instruccion has to be on a separate lines, there can't be any line blank and each one has to be an instuction

# 3: Every characther after the intruction will not be compilled so that space can be use to add comments about your code like
# 0x12fe this loads to the register......
#    Keep In Mind   #
#### every characther has to be lower case ###
### at the end of the program the register that were used and the memory that was used will be printed ####
### as a recommendation the instruction_file should be in the same directory(folder) that you're in ###
### that's all (I think)###

def test(instruction_file):
    #inizializing memory locations
    hex_combinations = [format(i, '02x') for i in range(256)]
    memory_dup = memory
    memory = {}
    for inizialize_line in hex_combinations:
        memory[f'{inizialize_line}'] = ''
    for complete_memory in memory_dup:
        memory[complete_memory] = memory_dup[complete_memory]
    memory_location =[]
################################################################
    #putting intrucions in memory
    f = open(instruction_file)
    instruciones = []
    for instruccion in f:
        instruciones.append(instruccion)
    iterador = 0
    for inserting in instruciones:
        inserting_val = ''
        for x in range(6):
            inserting_val += inserting[x]
        memory[f'{hex_combinations[iterador]}'] = inserting_val

        memory_location.append(hex_combinations[iterador])

        iterador += 2
    f.close()
#################################################################
    #inizializando registros
    hex_numbers = [format(i, 'x') for i in range(16)]
    registros = {}
    for num_registro in hex_numbers:
        registros[f'{num_registro}'] = ''
########################################################################
    #Instruciones
    def load_mem(instruccion):
        value = memory[f'{instruccion[4]}{instruccion[5]}']
        registros[f'{instruccion[3]}'] = value
        print(registros[f'{instruccion[3]}'])
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
    def sum_com(instruccion):
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
            print('| OVERFLOW | instruction |',instruccion,"|")
            print("º'''''''''''''''''''''''''''''''''º")

    def float_float(instruccion):
        execces_nums = {"000": '-4' ,"001":'-3',"010":'-2',"011":'-1',"100":'0',"101":'1',"110":'2',"111":'3'}

        bin_str_1 = registros[f'{instruccion[4]}']
        bin_str_2 = registros[f'{instruccion[5]}']
        bin_str_1 = int(bin_str_1, 16)
        bin_str_2 = int(bin_str_2, 16)
        num_bits = 8
        bin_str_1 = format(bin_str_1,f'0{num_bits}b')
        bin_str_2 = format(bin_str_2, f'0{num_bits}b')

        def convert_to_int(bin_str):
            exponent = ''
            for i in range(1, len(bin_str)-4):
                exponent += bin_str[i]
            for expo in execces_nums:
                if exponent == expo:
                    steps = execces_nums[f'{expo}']

            if  exponent[0] == '1':
                integer_part = ''
                for i in range(4,(4+int(steps))):
                    integer_part += bin_str[i]
                integer_part = int(integer_part, 2)
                fraction_part = 0
                prestablish_value = 0.5
                for x in range(4+int(steps),len(bin_str)):
                    fraction_part += int(bin_str[x])*prestablish_value
                    prestablish_value = prestablish_value/2
                float_num = float(integer_part)+float(fraction_part)
                if bin_str[0] == '1':
                    float_num = float_num*(-1)
                return float_num
            else:
                condicion = 0
                fractions_part = ''
                for i in range(0,(int(steps)*-1)):
                    fractions_part += '0'
                    condicion += 1

                for w in range(4, len(bin_str)):
                    fractions_part += bin_str[w]

                fraction = 0
                prestablish_value = 1/2
                for y in fractions_part:
                    fraction += int(y)*prestablish_value
                    prestablish_value = prestablish_value/2
                if bin_str[0] == '1':
                    fraction = fraction*(-1)
                return fraction

        val_1 = convert_to_int(bin_str_1)
        val_2 = convert_to_int(bin_str_2)
        val_total = val_1 + val_2
        prestablish_value = 1/2
        tot = ''

        for i in range(4):

            if (val_total*-1) > prestablish_value:
                tot += "1"
                val_total = ((val_total*-1)-prestablish_value)*-1
                prestablish_value = prestablish_value/2
            else:
                tot += "0"
                prestablish_value = prestablish_value / 2
        print(tot)










    #######################################################################
    #etapa de decodificacion
    start = 0
    stop = False
    while not stop:
        for i in range(start, len(memory_location)):
            print(instruccion)
            print(instruccion)
            if instruccion[2] == "1":
                load_mem(instruccion)
            if instruccion[2] == "2":
                load_bit(instruccion)
            if instruccion[2] == "3":
                store(instruccion)
            if instruccion[2] == "4":
                move(instruccion)
            if instruccion[2] == "5":
                sum_com(instruccion)
            if instruccion[2] == "6":
                float_float(instruccion)
            if instruccion[2] == "7":
                print("Not available yet")
            if instruccion[2] == "8":
                print("Not available yet")
            if instruccion[2] == "9":
                print("Not available yet")
            if instruccion[2] == "b":
                if jump(instruccion):
                    espacio = ''
                    espacio += instruccion[4]
                    espacio += instruccion[5]
                    start = memory_location.index(espacio)
                    starting = start
                    break

            if instruccion[2] == 'c':
                stop = True


                break
################################################################################
    #printing registers

    iterador = 0
    print('.,,,,,,,,,,,,,,,,,,,.')
    for prt in registros:
        registers = ''
        if registros[prt] != '':
            registers += f"| Registro | {hex_numbers[iterador]} | {registros[prt]} |"
            print(registers)
        iterador += 1
    print("º'''''''''''''''''''º")

################################################################################
    #printing memory
    iterador = 0
    print('.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.')
    for prt in memory:
        memory_position = ''
        if memory[prt] != '':
            if len(memory[prt]) == 6:
                memory_position += f'| Memory Position | {hex_combinations[iterador]} | {memory[prt]} |'

            else:
                esp = ''
                for i in range(6-(len(memory[prt]))):
                    esp += ' '
                memory_position += f'| Memory Position | {hex_combinations[iterador]} | {memory[prt]} {esp}|'
            print(memory_position)

        iterador += 1
    print("º'''''''''''''''''''''''''''''''º")
test('demofile.txt', {'d1':'07', 'd0':'10'})


