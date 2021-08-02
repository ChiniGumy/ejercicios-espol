tendencias = {
    "08-22-2016":{"#Rio2016", "#BSC", "#ECU"},
    "08-25-2016":{"#GYE", "#BRA"},
    "08-27-2016":{"#YoSoyEspol", "#GYE","#BSC"}
}

lista_fechas = [
    "08-22-2016",
    "08-25-2016",
    "08-27-2016",
]

def cuenta_etiquetas(dic_tendencia, lista_fechas):
    print("")

    dias_tendencia = {}                                                         # primero creo el diccionario
    
    for dia in lista_fechas:                                                    # se recorre el listado de fechas
        tendencias_dia = dic_tendencia[dia]                                     # estoy obteniendo el valor de las tendencias del dia, es un conjunto de strings
        for tendencia in tendencias_dia:                                        # itero sobre las tendencias del dia
            if tendencia in dias_tendencia:                                     # si tendencias esta en dias tendencias
                dias_tendencia[tendencia] = dias_tendencia[tendencia] + 1       # entonces se incrementa en uno el valor de aparicion
            else:
                dias_tendencia[tendencia] = 1                                   #caso contrario, solo sera 1

    return dias_tendencia                                                       # retorno dias tendencia


print(cuenta_etiquetas(tendencias, lista_fechas))
print("")

def reporta_tendencias(dic_tendencia, lista_fechas):

    diccionario_conteo = cuenta_etiquetas(dic_tendencia, lista_fechas)          # hago un diccionario de conteo

    print("estos hashtags estuvieron en todas los dias:")                       # por for tendencia, conteo en los items de diccionario_conteo
    for tendencia, conteo in diccionario_conteo.items():                        # ITEMS TE DEVUELVE UN ITERABLE DE TUPLAS, ENTONCES tendencia SERA CLAVE y conteo SERA EL VALOR
        if conteo == len(lista_fechas):                                         # si conteo es igual a la longitud de la lista_fechas
            print(tendencia)                                                    # imprimo la tendencia

    print("")

    print("estos hashtags estuvieron al menos un dia en tendencia:")            
    for tendencia in diccionario_conteo.keys():                                 # bucle de: por cada que tendencia este en las llaves de diccionario_conteo
        print(tendencia)                                                        # imprimir tendencia

reporta_tendencias(tendencias, lista_fechas)
print("")

def tendencias_excluyentes(dic_tendencia, fecha1, fecha2):

    tendencias_fecha1 = dic_tendencia[fecha1]                                   # obteniendo el conjunto de hashtags de la clave fecha 1                       
    tendencias_fecha2 = dic_tendencia[fecha2]                                   # obteniendo el conjunto de hashtags de la clave fecha 2

    print(tendencias_fecha1 ^ tendencias_fecha2)                                # operador "^ diferencia simetrica entre conjuntos, que es una diferencia simterica? es la union de conjuntos quitando los elementos que se repiten  

tendencias_excluyentes(tendencias,"08-25-2016", "08-27-2016")                   # llamando la funcion con las fechas como parametros