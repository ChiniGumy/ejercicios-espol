from os import write


def cargar_datos(nombre_archivo):
    diccionario_datos = {}
    archivo_datos = open(nombre_archivo, "r")

    lineas = archivo_datos.readlines()
    archivo_datos.close()                           # depues de un readlines ya se puede cerrar el archivo, ya que no se lo llama despues

    diccionario_datos["M"] = int(lineas[0])
    diccionario_datos["Corta"] = float(lineas[1])
    diccionario_datos["Larga"] = float(lineas[2])
    diccionario_datos["Infinitivo"] = float(lineas[3])

    return diccionario_datos

#print(cargar_datos("costos.txt"))

def calcular_costos(datos, nombre_archivo):
    archivo_texto = open(nombre_archivo, "r")

    suma_total = 0
    for linea in archivo_texto:
        palabras = linea.replace(".","").strip().split(" ")             # el metodo replace() remplaza caracteres en un string, los deseados tendran que ponerse adentro como argumentos
        for palabra in palabras:
            if palabra.endswith("ar") or palabra.endswith("er") or palabra.endswith("ir"):      # el metodo endswith() valida si un string termina con: # lo que se ponga en el argumento
                suma_total += datos["Infinitivo"]
            elif len(palabra) <= datos["M"]:
                suma_total += datos["Corta"]
            else:
                suma_total += datos["Larga"]
    archivo_texto.close()
    return round(suma_total, 2)
    
#print(calcular_costos(cargar_datos("costos.txt"), "texto.txt"))

def cambiar_mensaje(datos, nombre_archivo1, nombre_archivo2):
    archivo1 = open(nombre_archivo1 ,"r")
    archivo2 = open(nombre_archivo2, "w")
    longitud_maxima = datos["M"] - 1

    for linea in archivo1:
        palabras = linea.strip().split(" ")
        for palabra in palabras:
            if "." not in palabra:
                if len(palabra) > datos["M"]:
                    archivo2.write(f"{palabra[:longitud_maxima]}#")             # estoy tomando los caracteres de palabra del indice 0 a longitd_maxima( datos["M"] - 1 )
                else:
                    archivo2.write(palabra)
            else:
                palabra = palabra.replace(".","")
                if len(palabra) > datos["M"]:
                    archivo2.write(f"{palabra[: longitud_maxima]}#END") 
                else:
                    archivo2.write(f"{palabra}END") 

            archivo2.write(" ")
        archivo2.write("\n")

    archivo1.close()
    archivo2.close()

cambiar_mensaje(cargar_datos("costos.txt"),"texto.txt","texto traducido.txt")

