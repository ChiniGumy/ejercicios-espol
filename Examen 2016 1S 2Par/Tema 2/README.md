# Tema 2
Las distancias en km, expresadas en valores enteros positivos, entre ciudades del Ecuador conectadas
directamente por una carretera estan dadas en el archivo Ecuador_distancias.txt con el siguiente formato:

    Ciudad de Partida | Ambato, 318 | Azogues, 555 
    Ambato | Azogues, 280 | Babahoyo, 212 | ... | Pedernales, 318
    Azogues | Pedernales, 555 | ... | Babahoyo, 125

## Implemente las siguientes funciones:
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