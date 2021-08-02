# Examen 2016 1 Semestre 2 Parcial

>## Tema 1
Suponga que existe un diccionario de tendencias con un string que representa una fecha (mm - dd - aaaa)
como clave y como valor un conjunto de las etiquetas(hashtags) que fueron tendencia en Twitter para esa fecha.
Por ejemplo:

```
tendencias = {
    "08-22-2016":{"#Rio2016", "#BSC", "#ECU"},
    "08-25-2016":{"#GYE", "#BRA"},
    "08-27-2016":{"#YoSoyEspol", "#GYE","#BSC"}
}
```

### Implementa las siguientes funciones:

1. cuentaEtiquetas(tendencias, listaFechas) que recibe el diccionario de tendencias una lista con strings que
    representan fechas ( mm - dd - aaaa). La funcion debe retornar un nuevo diccionario con la etiqueta como clave
    y como valor, el numero de dias que esta etiqueta fue tendencia durante las fechas especificadas en listaFechas.
    Por ejemplo:

```
cuentaEtiquetas(tendencias,[’08-22-2016’, ’08-25-2016', '08-27-2016']) retorna

{'#Rio2106':1, '#GYE':2, '#YoSoyEspol':1, '#BSC':2, '#ECU':1, '#BRA':1}
```

2. reportaTendencias(tendencias, listaFechas) que recibe el diccionario de tendencias y una lista con strings que
    representan fechas ( mm - dd - aaaa ). La funcion debe mostrar por pantalla:
```
1. Las etiquetas que fueron tendencia todas las fechas en listaFechas
2. Las etiquetas que fueron tendencia al menos en una de las fechas en listaFechas
```
3.  tendenciasExcluyentes(tendencias, fecha1, fecha2) que recibe diccionario de tendencias y dos strings que
    representan fechas ( mm - dd - aaaa ). La funcion debe mostrar por pantalla las etiquetas que fueron tendencias
    o en fecha1 o en fecha2, pero no en las dos.

    NOTA: Suponga que fecha1 y fecha2 existen en el diccionario como claves.

>## Tema 2
Las distancias en km, expresadas en valores enteros positivos, entre ciudades del Ecuador conectadas
directamente por una carretera estan dadas en el archivo Ecuador_distancias.txt con el siguiente formato:

    Ciudad de Partida | Ambato, 318 | Azogues, 555 
    Ambato | Azogues, 280 | Babahoyo, 212 | ... | Pedernales, 318
    Azogues | Pedernales, 555 | ... | Babahoyo, 125

### Implemente las siguientes funciones:
1. cargar_datos(nombre_archivo) que recibe el nombre del archivo como string y retorna el diccionario
distancias con el siguiente formato:

```
{‘Ambato’:{‘Azogues’:280, ‘Babahoyo’:212, … ,‘Pedernales’:318}, … {‘Babahoyo’:{‘Ambato’:250}}}
```

2. ciudades_cercanas(ciudades, km) donde km es un valor entero positivo y distancias es el diccionario generado
    en el literal a. La funcion retorna una lista de tuplas con todos los pares de ciudades conectadas directamente
    por uan carretera que esten a una separacion menor o igual que Km. La tupla incluye ciudad1, ciudad2 y distancia
    que las separa. Por ejemplo:

```
ciudadesCercanas(distancias, 300)
retorna [(‘Ambato’,’Azogues’,280), (‘Ambato’,’Babahoyo’,212), (‘Azogues’,’Babahoyo’,125), (‘Babahoyo’,’Ambato’,250)]
```

3.  guardar_ciudades_cercana(distancias, listaKms) que recibe el diccionario de distancias generado en el literal a
    y una lista de valores enteros positivos. La funcion debera generar por cada valor de la lista un archivo con las
    ciudades separadas al maximo dicho valor. Por ejemplo:

    guardar_ciudades_cercana(distancias, [300, 100, 250]) genera los siguientes tres archivos:

```
ciudades300.txtm, ciudades100.txt, ciudades250.txt
```

El archivo ciudades300.txt tendria el siguiente contenido:

```
Ambato, Azogues, 280
Ambato, Babahoyo, 212
Azogues, Babahoyo, 125
Babahoyo, Ambato, 250
```

>## Tema 3

1. Implementa una funcion buscar(lista_anidada, valor) que recibe una lista de listas y retorna
verdadero o falso si *valor* existe en *lista_anidada*.
```


```

2. Utilice la funcion *buscar* del literal a para determinar si el valor X existe en la lista
    anidada L y mostrar por pantalla 'Valor si existe' o 'Valor no existe'.

```
L = [[3, 2, 5], [1], [7, 9]]
X = int(input(‘Ingrese valor por teclado’)
#su código aquí
```

3. Implementa una funcion que sume o multiplique valores enteros almacenados en una lista anidada.
    Si se invoca la funcion unicamente con la lista como argumento, la funcion debe retornar suma de los valores.
    Si se invoca con un segundo argumento con valor 'multiplicar', la funcion debe retornar la multiplicacion
    de los valores. Para cualquier otro valor para el segundo argumento, la funciom debera retornar -1.

```


```