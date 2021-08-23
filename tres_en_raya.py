# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 18:31:25 2021

@author: paolo

Ejercicio: Tres en raya

Hacer un programa que permita jugar el "tres en raya" desde la terminal, para dos jugadores.

El juego debe validar que las casillas que elija el jugador esten vacias antes de poder poner una ficha "X" u "O"


ayuda grafica de las coordenadas:
    Para el array
    ["(0,0)", "(0,1)", "(0,2)"]
    ["(1,0)", "(1,1)", "(1,2)"]
    ["(2,0)", "(2,1)", "(2,2)"]
    
    para el jugador
    ["(1,1)", "(1,2)", "(1,3)"]
    ["(2,1)", "(2,2)", "(2,3)"]
    ["(3,1)", "(3,2)", "(3,3)"]

"""
from collections import deque

turno = deque(["O", "X"])

tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

#FUNCIONES

#funcion para mostrar el tablero
def mostrar_tablero():
    print("")
    for fila in tablero:
        print([cuadrado for cuadrado in fila])
        
#funcion para cambiar de turno        
def cambiar_turno():
    turno.rotate()
    return turno[0]

#funcion para procesar la posicion del jugador, se usa split para dividir la coordenada (fila,columna) en dos variables
def procesar_posicion(posicion):
    fila, columna = posicion.split(",")
    return int(fila) - 1, int(columna) - 1

#funcion para validar si la posicion es correcta
def validar_posicion(posicion):
    #se evalua si la fila y la columna son mayores o iguales a 0 y menores o iguales a 2
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
        #se evalua si la posicion esta vacia o si tiene una marca "X" u "O"
        if tablero[posicion[0]][posicion[1]] == " ":
            #si se cumplen las condiciones la funcion devuelve True, sino devuelve False
            return True
    return False

#funcion para actualizar el tablero, se vincula la posicion con el jugador y se escribe la "X" u "O" en el tablero
def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador

#funcion para evaluar la victoria. j es jugador ("X" u "O")
def evaluar_victoria(j):
    if tablero[0] == [j, j, j] or tablero[1] == [j, j, j] or tablero[2] == [j, j, j]:
        return True
    elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
        return True
    elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
        return True
    elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
        return True
    elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
        return True
    elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
        return True
    else:
        return False
    
#funcion para evaluar empate
def evaluar_empate():
    return set(tablero[0]).union(set(tablero[1])).union(set(tablero[2])) == set(["X","O"])

#Funciones principales

def main():
    jugador = cambiar_turno()
    
    while True:
        posicion_str = input("Jugador {} ingresa una posicion (fila,columna) de 1 a 3. Escribe 'salir' para salir\n".format(jugador))
        if posicion_str == "salir":
            print("Juego cerrado")
            break
        try:
            posicion_procesada = procesar_posicion(posicion_str)
        except:
            print("Error: la posicion {} no es valida. El formato debe ser (fila,columna)".format(posicion_str))
            continue
        if validar_posicion(posicion_procesada):
            #se modifica la posicion en el tablero
            actualizar_tablero(posicion_procesada, jugador)
            #se muestra el tablero ya actualizado
            mostrar_tablero()
            if evaluar_victoria(jugador):
                print("Jugador {} ha ganado! \nJuego finalizado".format(jugador))
                break
            if evaluar_empate():
                print("Esto es un empate. \nJuego finalizado")
                break
            jugador = cambiar_turno()
        else:
            print("Posicion {} no valida".format(posicion_str))
        
if __name__ == "__main__":
    print("Bienvenido al juego de Tres en Raya")
    #ejecutamos funcion principal
    main()
else:
   print("Ha ocurrido un error al iniciar el programa")