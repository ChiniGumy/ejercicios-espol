import random

numeros_generados = []                                          # creo una lista llamada numeros generados

for i in range(0,10):                                           # hago un bucle para que haga 10 numeros
    numero = random.randrange(0,15)                             # numero es igual a numero random entre 0 y 15
    while numero in numeros_generados:                          # validacion para que no se repitan numeros
        numero = random.randrange(0,15)             
    numeros_generados.append(numero)                            # agrego el numero a la lista creada

numeros_generados.sort()                                        # map genera un iterable con los valores procesados por la funcion del arreglo original
numeros_generados = map(lambda x: str(x), numeros_generados)    # lambda es una palabra reservada para definir una funcion anonima
numeros_generados = list(numeros_generados)

archivo_numeros = open("numeros.txt", "w")                      # abro un archivo llamada archivo_numeros para escribir "w"    
archivo_numeros.write("\n".join(numeros_generados))             # escribo la lista en el archivo con salto de linea con "\n"
archivo_numeros.close()                                         # cierro el archivo


archivo_numeros = open("numeros.txt", "r")                      # abro el archivo para leerlo
diccionario_nums = {}                                           # creo un diccionario

for linea in archivo_numeros:                                   # por cada linea en archivos_numeros("numeros.txt")
    linea = int(linea)                                          # hago que las lineas se conviertan en numeros enteros
    diccionario_nums[linea] = "numero no jugado"                # y ahora agrego como calve los numeros y como valor "numero no jugado" para identidicar que numero se jugo y cual no en el diccionario como lo pide el ejercicio


coincidencias = 0                                               # creo una variable llamada coincidencias
while coincidencias < 8:                                        # mientras que coincidencias sea menor a 8
    numero_ingresado = int(input("ingresar numero:.. "))        # pedir el ingreso de un numero

    if numero_ingresado in diccionario_nums.keys():             # si el numero ingresado esta en las claves
        coincidencias += 1                                      # entonces se le sumara un punto a coincidencia
        diccionario_nums[numero_ingresado] = "numero jugado"    # y en el diccionario se le atualiza el valor al numero ingresado a "ya jugado", si es que esta en el diccionario
        print("acertaste un numero\n")
    else:
        print("no acertaste\n")

print("ganaste!!")