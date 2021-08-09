import random

def sensar_cultivos(tupla_pocision):
    return random.randint(1,10)

def generar_plantacion(tupla_dimension_plantacion):
    matriz = []
    for fila in range(0, tupla_dimension_plantacion[0]):
        lista_filas = []
        for columna in range(0, tupla_dimension_plantacion[1]):
            lista_filas.append(sensar_cultivos((fila, columna)))
        matriz.append(lista_filas)
    return matriz

respuesta_literal_a = generar_plantacion((3,4))
for lista in respuesta_literal_a:
    print(lista)
print("")

def analizar_densidad(plantacion, limite = 4):
    matriz_densidad = []
    for linea in plantacion:
        lista_filas = []
        for numero in linea:
            if numero < limite:
                lista_filas.append("BAJO")
            else:
                lista_filas.append("ALTO")

        matriz_densidad.append(lista_filas)

    return matriz_densidad

respuesta_literal_b = analizar_densidad(respuesta_literal_a)
for lista in respuesta_literal_b:
    print(lista)
print("")

def reporte_crecimiento(plantacion, desnidad):
    
    promedio_surco = []
    for linea in plantacion:
        promedio_surco.append(sum(linea) / len(linea))
    
    pocisiones_relativas = []
    for linea in plantacion:
        pocisiones_relativas.append(linea.index(max(linea)))

    promedio_cultivo = []
    lista_ALTOS = []
    lista_BAJOS = []
    for i in range(0, len(desnidad)):
        for j in range(0, len(desnidad[0])):
            if desnidad[i][j] == "ALTO":
                lista_ALTOS.append(plantacion[i][j])
            else:
                lista_BAJOS.append(plantacion[i][j])
    
    promedio_cultivo.append(sum(lista_ALTOS) / len(lista_ALTOS))
    promedio_cultivo.append(sum(lista_BAJOS) / len(lista_BAJOS))

    return (promedio_surco, pocisiones_relativas, promedio_cultivo)

print(reporte_crecimiento(respuesta_literal_a, respuesta_literal_b))


