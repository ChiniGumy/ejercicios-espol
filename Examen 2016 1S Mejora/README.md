# Examen 2016 1 Semestre Mejora

>## Tema 1

Una empresa de telecomunicaciones necesita automatizar el cálculo del costo de enviar un mensaje
basado en el número de palabras, el tamaño de cada palabra y el tipo de palabra. Para el cálculo:

    1. se determina que una palabra corta tiene máximo M caracteres
    2. se determina que una palabra larga tiene más de M caracteres
    3. se define como palabra especial los verbos en infinitivo, es decir, palabras terminadas en “ar”, “er”, “ir”, 
       sin importar su tamaño.

Para calcular el costo total del mensaje usted debe cobrar un valor por las palabras cortas, otro valor por las palabras largas
y otro valor por los infinitivos. Suponga que todos los costos para este problema  están dados en dólares americanos.

### Implementar las siguientes funciones:

1. cargar_datos(nombre_archivo) que recibe el nombre del archivo que especifica en lineas separadas el tamano de M,
    el costo de las palabras cortas, el costo de las palabras largas, y el costo de los infinitivos.
    Su funcion debera leer este archivo y retornar un diccionario con el siguiente formato de ejemplo:

``` python
10              cargar_datos("Costos.txt") return
0.2
0.5             {'M':10,'Corta:0.2','Larga:0.5','Infinitivo:0.3'}
0.3
```

2. calcular_costos(datos, nombre_archivo) que recibe el diccionario de datos generado en el literal a y un nombre de arhivo.
El archivo contiene el texto del mensaje grabado linea por linea. Adenasm cada linea contiene multiples palabras separadas
por espacios. El unico signo de puntuacion presente en el texto es un punto '.' al final del mensaje y no debera ser considerado
para determinar el costo de esa palabra. La funcion debe retornar el costo total del mensaje.

```


```

3. cambiar_mensaje(datos, nombre_archivo1, nombre_archivo2) que recibe el diccionario de datos generado en el literal a
y dos nombres de arhivos. La funcion debe leer el texto del mensaje de *nombre_archivo2* el nuevo mensaje, acortando las
palabras largas a M -1 caracteres y colocando '#' al final de cada una de ellas, y remplazando el punto final con 
la palabra especial 'END'.

```


```

># Tema 2

Una empresa agricola ha decidio integrar un dron a una de sus plantaciones de area MxN para poder monitorear el crecimiento
de sus cultivos. El dron a utilizarse tiene la capacidad de sensar el numero de cultivos en una pocision (i,j) por medio 
de la funcion *sensar_cultivos(tupla_posicion)* que mueve el dron a la posicion dada por la tupla y retorna un valor entero
correspondiente al numero de cultivos en dicha posicion. Suponga que la funcion ya existe, por lo tanto no necesita ser
desarrollada por usted.

## Implementar las siguientes funciones

1. generar_plantacion(tupla_dimension_plantacion) que recibe como tupla indicando el tamano total (M,N) de la plantacion
y se procede a sensar los cultivos utilizando sensar_cultivo. la funcion retorn la matriz plantacion que indica el numero 
de cultivos en cada posicion de la plantacion.

```


```

2. analizarDensidad(plantación, limite) que recibe como parámetro la matriz plantación del literal 1 yun valor entero positivo.
    La función debe retornar una nueva matriz indicando los grados decrecimiento de la plantación. Una posición (i,j) de la plantación
    es considerada con crecimiento 'BAJO' si tiene menos de limite cultivos, caso contrario es considerada de crecimiento 'ALTO'.
    Al definir la función, considere que el valor por defecto de limite debe ser 4. Por ejemplo:

```python
Si plantacion = [
    [5, 3, 2],
    [1, 4, 8],
    [2, 3, 1]
]

analizarDensidad(plantacion), retorna:
[[‘ALTO’, ‘BAJO’, ‘BAJO’],
 [‘BAJO’, ‘ALTO’, ‘BAJO’],
 [‘BAJO’, ‘BAJO’, ‘BAJO’]]
```
3. reporteCrecimiento(plantacion, densidad) que recibe como parámetros las matrices de los literales
    1 y 2. Suponga que “surco” es equivalente a una fila de la matriz y “parcela” es equivalente a una
    celda de la matriz. La función debe retornar una tupla de tres elementos con la siguiente
    información:

    1. Los promedios de cultivos por surcos.
    2. Las posiciones, relativas a cada surco, de las parcelas que tienen el mayor número de
    cultivos en dicho surco.
    3. Los promedios de cultivos de las parcelas para los grados de crecimiento ‘ALTO’ y ‘BAJO’
    
```python
Por ejemplo, si plantacion = [
    [5, 3, 2],
    [1, 4, 8],
    [2, 3, 1]
 ]
 
reporteCrecimiento(plantacion, densidad), retorna:
( [3.33333333, 4.33333333, 2.0], [0, 2, 1], [5.66667, 2.0] )
 ```


># Tema 3

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