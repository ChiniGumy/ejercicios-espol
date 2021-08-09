# Tema 3

1. Considere el siguiente codigo e indique que se muestra por pantalla, Justifique su respuesta.

``` python
lista1 =[3,'A',6]
lista2 =['A']

def funcion (lista1, lista2):
    a=[]
    for i in lista1:
        for j in lista2:
            if i != j:
                a.append(str(i) + str(j))
                for x in a[:]:
                    a.append(str(i) + str(j))
    return a
```

2. Considere el siguiente codigo e indique que se muestra por pantalla, Justifique su respuesta.

``` python
def fun(cadena, k):
    L = []
    for elem in set(cadena.split(' ')):
        L.append(elem * k)

    return '#'.join(L)

cadena = 'programar es estupendo estupendo es programar'
print(fun(cadena, 2))
```