# Tema 1
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

## Implementa las siguientes funciones:

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
