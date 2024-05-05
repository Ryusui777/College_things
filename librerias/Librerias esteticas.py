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
                num_de_char += 31
                lineas.append(new_string)
                new_string = ""
            elif len(message) < num_de_char:

                num_de_char = len(message)
                rango += 31
                for y in range(rango, len(message)):
                    new_string += f"{message[y]}"
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
        if len(linea) < longitud:
            lon = longitud - len(linea)
            for i in range(lon):
                esp+=" "
        mes = f"| {linea}{esp} |"

        print(mes)
    print(apostrofe)


hello = "Hello, my life, hello, new world Hello, hello, hello, everyone Hello, hello 叫んで oh-oh, it's alright だってもしかしたら明日空が割れて堕ちてくるね? どんな瞬間も永遠にしたい 鳴り止まないでこの心 羽ばたき舞え With you"

cool_square(hello)