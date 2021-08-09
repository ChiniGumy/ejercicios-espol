# Tema 2

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