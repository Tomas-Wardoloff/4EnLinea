from src.FuncionesValidacion import *
from src.CuatroEnLinea import completarTableroEnOrden

def jugar(tablero, column, turno, gameOver):
    if tiroValido(column):
        completarTableroEnOrden(column, turno, tablero)
        dibujarTablero(tablero)

    gameOver = True

if __name__ == "__main__":
    gameOver = False
    while not gameOver:
        turno = 1
        tablero = tableroVacio()

        column = int(input("\nIngrese una fila: "))
        
        jugar(tablero, column, turno, gameOver)
