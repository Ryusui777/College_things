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