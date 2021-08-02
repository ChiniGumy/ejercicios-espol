def buscar(lista_anidada, valor):
    for sublista in lista_anidada:                      # por sublista en lista_anidada
        if valor in sublista:                           # si esta el valor buscado en sublista
            return True
    return False                                        # como sublista recorrio todo lista_anidada y no encontro el valor entonces
                                                        # es false por eso esta afuera de la condicion if

L = [[3, 2, 5], [1], [7, 9]]
X = int(input('Ingrese valor por teclado'))
if buscar(L,X):                                         # se puede llamar a funciones que devuelven valores booleanos a una linea de if
    print("valor si existe")
else:
    print("valor no existe")


# argumento es cuando son llamados, por ejemplo: en la llamada buscar de la linea 10 los argumentos son L y X

# parametro es cuando se definen la funcion, por ejemplo: en la linea 1 lista_anidada y valor son los parametros

def calculadora(lista_anidada, operacion = "suma"):     # Se le puede dar un valor por defecto a los parametros de las funciones
    if operacion == "suma":
        suma_total = 0
        for lista in lista_anidada:
            suma_total += sum(lista)                    # la funcion sum suma todos los valores de una lista, y con el operador += es un shorthand para evitar a = a+b / a += b
        return suma_total
    elif operacion == "multiplicacion":
        multiplicacion_total = 1                        # esto se inicializa en 1 porque si se pone en 0 el resultado de la multiplicacion seria 0
        for lista in lista_anidada:
            for numero in lista:
                multiplicacion_total *= numero          # *= evita escribir a = a*b / a *= b
        return multiplicacion_total
    else:
        return -1

print(calculadora(L, "multiplicacion"))
