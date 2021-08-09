# lista1 =[3,'A',6]
# lista2 =['A']

# def funcion (lista1, lista2):
#     a=[]
#     for i in lista1:
#         for j in lista2:
#             if i != j:
#                 a.append(str(i) + str(j))
#                 for x in a[:]:                          # por cada elemento que exista en la lista a
#                     a.append(str(i) + str(j))           # se agregara al string i j
#     return a

# print(funcion (lista1, lista2))


def fun(cadena, k):
    L = []
    for elem in set(cadena.split(' ')):                     # set crea un conjunto, conjunto no tiene elementos repetidos
        L.append(elem * k)

    return '#'.join(L)

cadena = 'programar es estupendo estupendo es programar'
print(fun(cadena, 2))