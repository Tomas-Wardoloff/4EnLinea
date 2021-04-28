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
			for cell in row:
				if cell == 0:
					print(' ', end='')
				else:
					print(' %s ' % cell, end='')
			print('')

def tiroValido(secuencia):
	for column in secuencia:
		if 1 > column > 7:
			return False
	return True
	

def contenidoColumna(nro_column, tablero):
	columns = []
	for row in tablero:
		cell = row[nro_column - 1]
		columns.append(cell)#append sirve para agregar un elemento a una lista
	return columns

def contenidoFilas(nro_row, tablero):
	rows = []
	for column in tablero:
		cell = column[nro_row - 1]
		rows.append(cell)
	return rows

def contenidoTodasLasColumnas(tablero):
	columns = []
	for nro_column in range(0, 7):
		columns.insert(7,contenidoColumna(nro_column,tablero))
	return columns
#-----------------------------------------------------------#
secuencia = [1, 2, 3, 1]
tablero = tablerovacio()
if tiroValido(secuencia):
	tablero = completarTableroEnOrden(secuencia, tablero)
	dibujarTablero(tablero)
	print("La secuencia es valida")
else:#IndexError: list index out of range, ver porque me muestra el problema antes que el mensaje
	print("Para que la secuencia sea valida los valores tienen que estar comprendidos entre el 1 y el 7")

print("#-----------------------------------------------------------#")
print(contenidoColumna(1, tablero))
print("#-----------------------------------------------------------#")
print(contenidoFilas(1, tablero))
print("#-----------------------------------------------------------#")
