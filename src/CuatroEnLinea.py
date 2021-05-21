#----------------------------TEST-READY----------------------------#

def tableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

#----------------------------TEST-READY----------------------------#

def soltarFichaEnColumna(ficha, column, tablero):
		for row in range(6, 0, -1):
				if tablero[row - 1][column - 1] == 0:
						tablero[row -1][column - 1] = ficha
						return

#----------------------------TEST-READY----------------------------#

def completarTableroEnOrden(secuencia, tablero):
	c = 0
	for column in secuencia:
		if c % 2 != 0:
			soltarFichaEnColumna(2, column, tablero)
		else:
			soltarFichaEnColumna(1, column, tablero)
		c += 1
	return tablero

#-----------------------------------------------------------#

def dibujarTablero(tablero):
	for row in range(0,6):
		print(' | ', end='')
		for cell in range(0,7):
			if tablero[row][cell] == 0:
				print('   ',end='')
			else:
				print(f' {tablero[row][cell]} ',end='')
		print(' | ', end='')
		print()
	print(" +- - - - - - - - - - - -+",end="")

#----------------------------TEST-READY----------------------------#

def tiroValido(secuencia):
	for column in secuencia:
		if column < 1 or column > 7:
			return False
	return True

#----------------------------TEST-READY----------------------------#

def contenidoColumna(nro_column, tablero):
	columns = []
	for row in tablero:
		cell = row[nro_column-1]
		columns.append(cell)#append sirve para agregar un elemento a una lista
	return columns

#----------------------------TEST-READY----------------------------#

def contenidoFila(nro_row, tablero):
	rows = []
	for indice, row in enumerate(tablero):
		if indice == (nro_row - 1):
			rows = tablero[indice]
			return rows

#----------------------------TEST-READY----------------------------#

def contenidoTodasLasColumnas(tablero):
	columns = []
	for nro_column in range(1, 8):
		columns.append(contenidoColumna(nro_column,tablero))
	return columns

#-----------------------------------------------------------#

secuencia = [1, 2, 3, 7]
tablero = tableroVacio()
if tiroValido(secuencia):
	tablero = completarTableroEnOrden(secuencia, tablero)
	dibujarTablero(tablero)
	print("\nLa secuencia es valida")
else:
	print("Para que la secuencia sea valida los valores tienen que estar comprendidos entre el 1 y el 7")

print("#-----------------------------------------------------------#")
print(contenidoColumna(7, tablero))
print("#-----------------------------------------------------------#")
print(contenidoFila(6, tablero))
print("#-----------------------------------------------------------#")
print(contenidoTodasLasColumnas(tablero))