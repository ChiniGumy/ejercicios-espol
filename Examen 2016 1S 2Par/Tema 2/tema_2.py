def cargar_datos(nombre_archivo):
    diccionarios_distancias = {}
    archivo_distancias = open(nombre_archivo, "r")

    for linea in archivo_distancias:                            # | = pipe
        ciudades = linea.strip().split("|")                     # el metodo strip elimina sin parametros saltos de linea
        ciudades_distancias = {}
        for ciudad in ciudades[1:]:                             # ahora ciudad recorrera ciudades desde el indice 1 hasta el final
            nom_ciudad, distancia = ciudad.split(",")
            ciudades_distancias[nom_ciudad] = int(distancia)
        diccionarios_distancias[ciudades[0]] = ciudades_distancias
    archivo_distancias.close()

    return diccionarios_distancias

resultado_literal_a = cargar_datos("Ecuador_Distancias.txt")        # almaceno la funcion en una variable ya que la usare en un futuro

def ciudades_cercanas(distancias, km):
    lista_tuplas = []                                               # creo una lista en donde estaran las tuplas
    for ciudad_incial, distancias in distancias.items():            # por ciudad inicial y distancias en los items de distancias(parametro de la funcion)
        for ciudad_final, distancia in distancias.items():          # por ciudad final y distancia en los items de distancias(parametro de la funcion)
            if distancia <= km:                                                     # si la distancia es menor o igual a los km(parametro de la funcion)
                lista_tuplas.append((ciudad_incial, ciudad_final, distancia))       # agregar a lista_tuplas, ciudad_inicial, ciudad_final, distancia

    return lista_tuplas

print(ciudades_cercanas(resultado_literal_a, 300))

def guardar_ciudades_cercanas(distancias, lista_kms):
    for kms in lista_kms:                                           # por kms en lista_kms
        archivo_kms = open(f"ciudades{kms}.txt","w")                # abrira (f"ciudades{cifra de km}.txt","w")
        near_cities = ciudades_cercanas(distancias, kms)            # near cities es igual a ciudades cercanas(con parametros distancias y kms)
        for ciudades in near_cities:                                                # por ciudades en near_cities
            archivo_kms.write(f"{ciudades[0]},{ciudades[1]},{ciudades[2]}\n")       # se escribira en el archivo (archivo_kms) la ciudad y el indice
        archivo_kms.close()                                                         # se cierra el archivo

guardar_ciudades_cercanas(resultado_literal_a, [300])