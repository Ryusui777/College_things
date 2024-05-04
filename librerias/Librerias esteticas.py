def cool_square(message):
    suma = 0
    num_de_lineas = 1
    lineas = []
    comas =""
    apostrofes =""
    new_string = ""
    num_de_char = 30
    for i in message:
        suma += 1
    print(suma)
    if suma > 1:
        for i in range(suma):
            comas += ","
            apostrofes += "'"

    comas += ",,"
    apostrofes += "''"
    for char in range(suma):
        if char == num_de_char:

            num_de_lineas += 1
            rango = num_de_char-30

            for i in range(rango,num_de_char):
                print(i)
                new_string += f"{message[i]}"
            num_de_char += 30
            print(new_string, 's')
            lineas.append(new_string)
            new_string = ""




    coma = f".{comas}."


    apostrofe =f"º{apostrofes}º "

    print(coma)
    for linea in lineas:
        mes = f"| {linea} |"

        print(mes)
    print(apostrofe)
    print(lineas)

hello = "hello my life, hello new world, hello, hello, hello everyonee"

cool_square(hello)