def tablerovacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def soltarFichaEnColumna(ficha, column, tablero):
		for row in range(6, 0, -1):
				if tablero[row - 1][column - 1] == 0:
						tablero[row -1][column -1] = ficha
						return
#-----------------------------------------------------------#
def completarTableroEnOrden(secuencia, tablero):
	c = 0
	for column in secuencia:
		if c % 2 != 0:
			soltarFichaEnColumna(2, column, tablero)
		else:
			soltarFichaEnColumna(1, column, tablero)
		c += 1
	return tablero

def dibujarTablero(tablero):
		for row in tablero:
			print(row)

def tiroValido(secuencia):
	for column in secuencia:
		if column < 1 & column > 7:
			return False
	return True

secuencia = [1, 2, 3, 1, 8]
if tiroValido(secuencia):
	dibujarTablero(completarTableroEnOrden(secuencia,tablerovacio()))
	print("La secuencia es valida")
else:                                                        #IndexError: list index out of range, ver porque me muestra el problema antes que el mensaje
	print("Para que la secuencia sea valida los valores tienen que estar comprendidos entre el 1 y el 7")