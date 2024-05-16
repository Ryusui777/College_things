
def cool_square(message):
    total_de_char = 0
    lineas = []
    comas =""
    apostrofes =""
    new_string = ""
    num_de_char = 31
    longitud = 31
    esp = ""
    if len(message) < longitud:

        longitud = len(message)

    for i in message:
        total_de_char += 1
    if total_de_char >= 1:
        for char in range(total_de_char):

            if char == num_de_char:
                rango = num_de_char - 31
                for i in range(rango,num_de_char):
                    new_string += message[i]
                for y in range(len(new_string)):
                    if message[num_de_char-1] != ' ' and message[num_de_char] != ' ':
                        new_string += message[num_de_char]
                        if len(new_string)  > longitud:
                            longitud += 1
                        num_de_char += 1



                new_string_2 = new_string
                if new_string[0] == ' ':
                    new_string_2 = ''
                    for i in range(1,len(new_string)):
                        new_string_2 += new_string[i]

                new_string = new_string_2

                num_de_char += 31

                lineas.append(new_string)

                new_string = ""
            elif len(message) < num_de_char:

                new_string_2 = new_string
                rango = num_de_char-31
                num_de_char = len(message)

                for y in range(rango, len(message)):
                    new_string += f"{message[y]}"
                if len(new_string) > 0:
                    if new_string[0] == ' ':
                        new_string_2 = ''
                        for i in range(1,len(new_string)):
                            new_string_2 += new_string[i]
                        new_string = new_string_2
                lineas.append(new_string)


        for i in range(longitud):

            comas += ","
            apostrofes += "'"
        comas += ",,"
        apostrofes += "''"
    coma = f".{comas}."
    apostrofe =f"º{apostrofes}º "
    print(coma)
    for linea in lineas:
        esp_2 = esp
        if len(linea) < longitud:
            lon = longitud - len(linea)
            for i in range(lon):
                esp+=" "
        mes = f"| {linea}{esp} |"
        esp = esp_2
        print(mes)
    print(apostrofe)

def interpretar(instrucciones, print_proccess, memory):
    hex_combinations = [format(i, '02x') for i in range(256)]
    hex_numbers = [format(i, 'x') for i in range(16)]
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
        registros[f'{hex_numbers[gogo]}'] = ''
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
        print(sum,type(sum))

    while not stop:
        for i in range(starting, len(instrucciones)):
            instruccion = instrucciones[i]
#
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
                    start = memory['instrucciones']
                    start = start[f'{espacio}']
                    starting = start
                    break
                else:
                    starting = starting

            if instruccion[2] == 'c':
                stop = True
                print("Success")
    print_str = ''
    iterador_1 = 0
    cool_square("Registros")
    for i in registros:
        if registros[i] != '':
            cool_square(f'El registro {hex_numbers[iterador_1]}: {registros[i]}')
        iterador_1 += 1
    iterador_2 = 0
    print("______________________________________________________________________________________________________")
    cool_square("Memoria")
    for i in memory:
        if memory[i] != '' and i != "instrucciones":
            cool_square(f'la memoria {hex_combinations[iterador_2]}: {memory[i]}')
        iterador_2 += 1







#
ram = {'f0':'23','da':'32','d0':'05','d1':'0a'}
interpretar(["0x2064",'0x11d0','0x12d1','0x5312', '0xb30c', '0xb010','0x33e0','0xb012','0x33f0', '0xc000'], False, ram)

