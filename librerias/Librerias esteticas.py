def cool_square(message):
    suma = 0
    lineas = []
    comas =""
    apostrofes =""
    new_string = ""
    num_de_char = 31
    longitud = 31
    esp = ""
    for i in message:
        suma += 1
    print(suma)


    if suma > 1:
        for char in range(suma):
            if char == num_de_char:
                print('ASDF')
                rango = num_de_char-31

                for i in range(rango,num_de_char):
                    new_string += message[i]
                new_string_2 = new_string

                if new_string[0] == ' ':
                    new_string_2 = ''
                    for i in range(1,len(new_string)):
                        new_string_2 += new_string[i]
                new_string = new_string_2
                num_de_char += 31
                lineas.append(new_string)
                print(new_string)
                new_string = ""
            elif len(message) < num_de_char:
                new_string_2 = new_string
                num_de_char = len(message)
                rango += 31
                for y in range(rango, len(message)):
                    new_string += f"{message[y]}"
                if new_string[0] == ' ':
                    new_string_2 = ''
                    for i in range(1,len(new_string)):
                        new_string_2 += new_string[i]
                    new_string = new_string_2
                lineas.append(new_string)
                new_string = ""
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


hello = "I laughed and shook hand And made my way back home I searched for form and land For years and years I roamed I gazed a gazeless stare We walked a million hills I must have died alone A long, long time ago"

cool_square(hello)