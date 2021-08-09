# Tema 1

Una empresa de telecomunicaciones necesita automatizar el cálculo del costo de enviar un mensaje
basado en el número de palabras, el tamaño de cada palabra y el tipo de palabra. Para el cálculo:

    1. se determina que una palabra corta tiene máximo M caracteres
    2. se determina que una palabra larga tiene más de M caracteres
    3. se define como palabra especial los verbos en infinitivo, es decir, palabras terminadas en “ar”, “er”, “ir”, 
       sin importar su tamaño.

Para calcular el costo total del mensaje usted debe cobrar un valor por las palabras cortas, otro valor por las palabras largas
y otro valor por los infinitivos. Suponga que todos los costos para este problema  están dados en dólares americanos.

## Implementar las siguientes funciones:

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