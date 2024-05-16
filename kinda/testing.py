from librerias.efficient import fit_in_square
def test(instruction_file, memory):
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
            sum = hex(int(a, 16) + int(b, 16))
            sum_app = ''
            for i in range(2, len(sum)):
                sum_app += sum[i]
            if len(sum_app) == 2:

                registros[f'{instruccion[3]}'] = sum_app
            else:
                print("OVERFLOW")
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
    print(registers)
################################################################################
    memory_positions = ''
    iterador = 0
    for prt in memory:
        if memory[prt] != '':
            memory_positions += f'Memory Position #{hex_combinations[iterador]} : {memory[prt]} '
        iterador += 1
    print(memory_positions)
    fit_in_square(memory_positions, 24)



RAM = {'d1':'0a','d0':'0e'}
test('demofile.txt', RAM)