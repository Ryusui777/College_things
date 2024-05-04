def cool_square(message):
    suma = 0
    comas =""
    apostrofes =""
    for i in message:
        suma += 1
    if suma > 1:
        for i in range(suma):
            comas += ","
            apostrofes += "'"
    comas += ",,"
    apostrofes += "''"


    coma = f".{comas}."
    mes = f"| {message} |"
    apostrofe =f"º{apostrofes}º "

    print(coma)
    print(mes)
    print(apostrofe)

hello = "hello"

