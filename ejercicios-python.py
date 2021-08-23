# -*- coding: utf-8 -*-
"""

Ejercicios varios

Curso de Analisis de Datos con Python de Udemy
Profesor: Manuel Garrido


"""

#%%

#
"""
Ejercicio: Crear una función que muestre las 5 letras más repetidas de una frase

- Se utiliza la estructura de datos "Counter" que permite revisar la cantidad de repeticiones de cada elemento
- replace para eliminar espacios entre palabras, sino serian parte de los elementos contados
- funcion most_common(n) para mostrar los más repetidos
"""
from collections import Counter

def contar_letras(frase):
    
    frase_rep = frase.replace(" ", "")
    
    frase_count = Counter(frase_rep)
    
    return print(frase_count.most_common(5))
    

contar_letras("Un unicornio amarillo con piel de dinosaurio se comia tres murcielagos")


#%%

"""
Ejercicio: crear una funcion que devuelva su coeficiente de jaccard. El coef. de jaccard es una medida de
similaridad entre dos grupos y se define como el numero de elementos en los dos grupos dividido entre el 
numero de elementos de uno u otro grupo.

Para resolver este ejercicio voy a utilizar el tipo Set y sus operaciones intersection y union, para obtener y dividir
la cardinalidad de la intersección con la cardinalidad de la unión.

"""

def jaccard(A,B):
    
    #argumetnos A y B son los grupos de entrada
    
    g_A = set(A)
    g_B = set(B)
    
    #se hace interseccion de ambos grupos
    interseccion_AB = len(g_A.intersection(g_B))
    
    #se hace union de ambos grupos
    union_AB = len(g_A.union(g_B))
    
    #se calcula el coeficiente
    coeficiente = interseccion_AB/union_AB
    
    return print("Coeficiente de similitud: {}".format(coeficiente))

grupo_A = ["Aviones", "Perros", "Manzanas", "Gatos", "Cucarachas", "Vacunas", "Aviones", "Autos", "Manzanas"]
grupo_B = ["Aviones", "Manzanas", "Gatos", "Cucarachas", "Vacunas", "Peras", "Duraznos", "Autos", "Manzanas"]

#se calcula el coeficiente de jaccard
jaccard(grupo_A,grupo_B)

#%%



#%%

#para el proximo ejercicio necesito un archivo asi que lo escribire primero

import os

#verifico carpeta actual
archivos_carpeta_actual = os.listdir(".")
print(archivos_carpeta_actual)

#creamos archivo con varias lineas de texto aleatorio

with open("texto_ejemplo.txt", "w") as fname:
    texto_lorem = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.","Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.","Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.","Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]
    
    for linea in texto_lorem:
        fname.write(linea)
        fname.write("\n")

#%%
"""
Ejercicio: Hacer una funcion que con el nombre de un archivo lo lea y devuelva la linea con mayor longitud.
Se usa el texto generado arriba



"""
def linea_mas_larga(nombre_archivo):
    #se abre archivo y se guardan las lineas en un array
    with open(nombre_archivo) as fname:
        #strip para quitar el \n del salto de linea
        lineas = [linea.strip("\n") for linea in fname.readlines()]
    
    #se asume que la primera linea siempre es la mas larga, para comparar
    linea_mas_larga = lineas[0]
    #se recorre el array de lineas de texto y se compara y reasigna la variable con la linea mas larga
    for linea in lineas:
        if len(linea) > len(linea_mas_larga):
            linea_mas_larga = linea
    #se devuelve el resultado
    return linea_mas_larga

#se prueba la funcion
print(linea_mas_larga("texto_ejemplo.txt"))

#%%
"""
Ejercicio: Hacer una funcion que tenga como argumento el nombre del archivo y un numero "n". La funcion debe devolver
las n ultimas lineas.

Usare el texto del ejercicio anterio

"""
#Asi como esta la funcion ya se resuelve el ejercicio, pero le incluire una comparacion 
# respecto a la cantidad de lineas del texto para reducir errores

# def devolver_n_lineas(nombre_archivo, n):
#     with open(nombre_archivo, "r") as fname:
#         #hacemos las modificaciones al texto quitamos \n
#         lineas = [linea.strip("\n") for linea in fname.readlines()]
    
#     #usamos -n: para obtener los ultimos n del array
#     return lineas[-n:]

def devolver_n_lineas(nombre_archivo, n):
    with open(nombre_archivo, "r") as fname:
        lineas = [linea.strip("\n") for linea in fname.readlines()]
        #comparamos cantidad de lineas vs numero n
        if len(lineas) < n:
            return "Ha ocurrido un error. El numero n es mayor a la cantidad de lineas del documento"
        else:
            return lineas[-n:]

#con n=1        
print(devolver_n_lineas("texto_ejemplo.txt", 1))

#con n=5
print(devolver_n_lineas("texto_ejemplo.txt", 5))


#%%
"""
Ejercicio: Hacer una funcion que escriba los valores de un diccionario en un archivo .csv
"""

#Creamos el diccionario

personas = {
    "nombre": ["Javier", "Juan", "Pedro"],
    "edad": [25,36,48],
    "ciudad": ["Santiago", "Rancagua", "Concepcion"]
    }

def convertir_a_csv(datos, nombre_archivo):
    #lista de datos keys
    claves = list(datos.keys())
    #longitud de la primera clave
    n_items = len(datos[claves[0]])
    
    #escribimos el archivo
    with open(nombre_archivo, "w") as fname:
        #escribimos las claves (que serian los "titulos" de las columnas en la tabla de csv)
        fname.write(",".join(claves))
        fname.write("\n")
        
        #luego escribimos los datos de cada fila
        for i in range(n_items):
            fila = ",".join([str(datos[clave][i]) for clave in claves])
            fname.write(fila)
            fname.write("\n")
            
#probamos
convertir_a_csv(personas, "tabla_ejemplo.csv")


#%%
