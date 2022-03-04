import random
from src.FuncionesValidacion import *
from src.FuncionesJuego import completarTableroEnOrden

def jugar(tablero, column, turno, gameOver):
    if tiroValido(column):
        completarTableroEnOrden(column, turno, tablero)
        dibujarTablero(tablero)

def cambioTurno(turno):
    if turno == "X":
        return "O"
    else:
        return "X"

if __name__ == "__main__":
    gameOver = False
    tablero = tableroVacio()
    turno = random.choice(["X","O"])
    
    while not gameOver:     
        column = int(input(f"\nEs el turno de: {turno}. Ingrese una fila: "))
        jugar(tablero, column, turno, gameOver)
        turno = cambioTurno(turno)
