

def interpretar(instrucciones, print_proccess, memory):
    hex_combinations = [format(i, '02x') for i in range(256)]
    stop = False
    registros = {}
    to = {}
    memory_dup = memory
    memory = {}
    for goddamn in range(len(hex_combinations)):
        memory[hex_combinations[goddamn]] = ''
    for giro in memory_dup:
        memory[giro] = memory_dup[giro]
    
    for gogo  in range(16):
        registros[f'{gogo}'] = ''
    iterador = 0
    for place in range(0,len(instrucciones)):
        pla = hex_combinations[iterador]
        to[pla] = place
        iterador += 2

    memory['instrucciones'] = to

    starting = 0
    stop = False
    def load_mem(instruccion):
        value = memory[f'{instruccion[4]}{instruccion[5]}']
        registros[f'{instruccion[3]}'] = value
    def jump(instruccion):
        print("bunnie happy")
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
        sum = hex(int(a, 16) + int(b, 16))
        registros[f'{instruccion[3]}'] = sum

    while not stop:
        for i in range(starting, len(instrucciones)):
            instruccion = instrucciones[i]
#
            if instruccion[2] == "1":
                print(instruccion, 'load')
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
                print("___________________________________________________________________")

                if jump(instruccion):
                    espacio = ''
                    espacio += instruccion[4]
                    espacio += instruccion[5]
                    start = memory['instrucciones']
                    start = start[f'{espacio}']
                    starting = start
                    break
                else:
                    starting = starting

            if instruccion[2] == 'c':
                stop = True
                print("Success")






#
ram = {'f0':'23','da':'32'}
interpretar(['0x10da','0x13da','0x11da','0x2a32','0x3ae0','0x40ca','0xba0c','0xc00'], False, ram)

