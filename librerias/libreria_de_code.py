#funcion que devuelve lista sin duplicados
def no_dup(lista_de_numeros):
    lista_de_retorno = []
    for i in lista_de_numeros:
        if i not in lista_de_retorno:
            lista_de_retorno.append(i)
    return lista_de_retorno
#funcion que toma un parametro y una lista y devuelve 
#una lista con los indices de los valores de la lista menores al parametro
def menores_que(num_de_com, lista):
    lista_de_retorno = []
    for i in range(0,len(lista)):
        if lista[i] <= num_de_com:
            lista_de_retorno.append(i)

    return lista_de_retorno
#funcion para comprobar una si un input es una float
def comprobar_float(usr_in):
    lista_de_digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','-','.']
    com_punto = 1
    con = False
    con_2 = False

    for i in usr_in:
        if i in lista_de_digitos:
            con = True
        else:
            con = False
            break
        if i == '.' and i != com_punto:
            com_punto = i
            con_2 = True
        elif i == '.':
            con_2 = False

    if con and con_2:
        return True
    else:
        return False


    if con and con_2:
        return True
    else:
        return False
#funcion para encerrar texto en un cuadro
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
hello = "hello my life, hello new world, hello, hello, hello everyonee"
cool_square(hello)