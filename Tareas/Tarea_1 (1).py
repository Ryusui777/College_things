#Minimize las 2 funciones para entender mejor
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

sad_message = """
_____________________________________________________.
　　　　　🌸＞　　フ This is Jane                                       
　　　　　| 　_　 _ l   and she is sad                 
　 　　　／` ミ＿xノ        because you didn't enter any 
　　 　 /　　　 　 |           valid number
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ
_____________________________________________________.
"""

#El codigo en si comienza desde aqui

#Nota: intente poner solo un 0

multiplicacion = 1
usr_input = 2
num_list = []
number = False
comprobacion_de_0 = []
# Este while pide numeros de punto flotante hasta que se ingrese un 0
while float(usr_input) != 0.0:
    usr_input = input("Ingrese un numero con punto flotante: ")
    #Se usa la fucion para comprobar si el input es un numero de punto flotante
    if comprobar_float(usr_input):

        if float(usr_input) != 0.0:
            num_list.append(usr_input)
            number = True
    else:
        #Si el input no es 0 o un numero flotante como "f"
        #entonces su valor se cambia a 1 ya que sino el while daria error
        comprobacion_de_0 = []
        com = True
        for i in usr_input:
            comprobacion_de_0.append(i)
        for y in comprobacion_de_0:
            if y != '0':
                com = False
        if com:
            usr_input = 0
        if not(com):
            message = f"{usr_input} no es un numero de punto flotante"
            cool_square(message)
            usr_input = 1

#La variable 'number' equivale a False cuando el programa comienza y si un numero de punto flotante esta cambiia a True
if number:
    for x in range(len(num_list)):
        print(f'Indice {x}: {num_list[x]}')

    for z in num_list:
        multiplicacion = multiplicacion * float(z)
    message_2 = f"La multiplicacion de todos los numeros es {multiplicacion}"
    cool_square(message_2)
    print('(˶ᵔ ᵕ ᵔ˶)')
    print('Thank you ♡')
else:
    print(sad_message)