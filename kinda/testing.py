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

def test(instruction_file, memory):
    #astethic purpose function
    def fit_in_square(message, length_of_line):
        num_of_char = 0
        length_of_line_2 = length_of_line
        lineas = []
        for i in message:
            num_of_char += 1
        if num_of_char > 0:
            new_length = length_of_line

            for char in range(len(message)):
                line_to_append = ""
                if char == new_length:
                    first = False
                    if message[new_length - length_of_line] == " ":
                        first = True
                    for digit in range(new_length - length_of_line, new_length):
                        if not first:
                            line_to_append += message[digit]
                        first = False
                    for last_digit in range(len(message)):
                        if message[(new_length - 1)] != " " and message[new_length] != " ":
                            line_to_append += message[new_length]
                            if len(line_to_append) > length_of_line_2:
                                length_of_line_2 += 1
                            new_length += 1

                    new_length += length_of_line
                    lineas.append(line_to_append)
                elif len(message) < new_length:
                    new_length = len(message)
                    first = False
                    if message[char] == " ":
                        first = True
                    for digit in range(char, new_length):
                        if not first:
                            line_to_append += message[digit]
                        first = False
                    lineas.append(line_to_append)
                    new_length = char

        comas = ""
        apostrofes = ""
        for i in range(length_of_line_2 + 2):
            comas += ","
            apostrofes += "'"
        print(f".{comas}.")
        for mes in lineas:
            esp = ""
            if len(mes) < length_of_line_2:
                for i in range(length_of_line_2 - len(mes)):
                    esp += " "
            print(f"| {mes}{esp} |")
        print(f"º{apostrofes}º")

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



    def sume(instruccion):
        a = registros[f'{instruccion[4]}']
        b = registros[f'{instruccion[5]}']
        if a == '' or b == '':
            print('Invalid number to add')
        else:
            # Convert hex strings to integers, add them, and then convert back to hex
            sum_decimal = int(a, 16) + int(b, 16)
            sum_hex = hex(sum_decimal)
            # Store the result in the destination register
            registros[f'{instruccion[3]}'] = str(sum_hex[2:].zfill(2))  # Convert back to hex and pad with zeros if necessary

    #######################################################################
    #etapa de decodificacion
    start = 0
    stop = False
    while not stop:
        for i in range(start, len(memory_location)):
            instruccion = memory[f'{memory_location[i]}']
            if instruccion[2] == "1":
                load_mem(instruccion)
            if instruccion[2] == "2":
                load_bit(instruccion)
            if instruccion[2] == "3":
                store(instruccion)
            if instruccion[2] == "4":
                move(instruccion)
            if instruccion[2] == "5":
                sume(instruccion)
            if instruccion[2] == "6":
                print("Not available yet")
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
    registers = ''
    iterador = 0
    for prt in registros:
        if registros[prt] != '':
            registers += f"Registro {hex_numbers[iterador]}: {registros[prt]} "

        iterador += 1
    fit_in_square(registers, 15)

################################################################################
    memory_positions = ''
    iterador = 0
    for prt in memory:
        if memory[prt] != '':
            memory_positions += f'Memory Position | {hex_combinations[iterador]} | {memory[prt]} '
        iterador += 1

    fit_in_square(memory_positions, 25)



