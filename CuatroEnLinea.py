def tablerovacio():
    return[
        ['|', 0, 0, 0, 0, 0, 0, 0, '|'],
        ['|', 0, 0, 0, 0, 0, 0, 0, '|'],
        ['|', 0, 0, 0, 0, 0, 0, 0, '|'],
        ['|', 0, 0, 0, 0, 0, 0, 0, '|'],
        ['|', 0, 0, 0, 0, 0, 0, 0, '|'],
        ['|', 0, 0, 0, 0, 0, 0, 0, '|'],
        ['+','-','-','-','-','-','-','-','+']
    ]

#-----------------------------------------------------------#

def soltarFichaEnColumna(ficha, column, tablero):
		for row in range(6, 0, -1):
				if tablero[row - 1][column] == 0:
						tablero[row -1][column] = ficha
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

#-----------------------------------------------------------#

def dibujarTablero(tablero):
	for row in tablero:
		for cell in row:
			if cell == 0:
				print('   ', end='')
			else:
				print(f' {cell} ', end='')
		print('')

#-----------------------------------------------------------#

def tiroValido(secuencia):
	for column in secuencia:
		if column < 1 or column > 7:
			return False
	return True

#-----------------------------------------------------------#

def contenidoColumna(nro_column, tablero):
	columns = []
	for row in tablero:
		cell = row[nro_column]
		if cell != '-':
			columns.append(cell)#append sirve para agregar un elemento a una lista
	return columns

#-----------------------------------------------------------#

def contenidoFila(nro_row, tablero):
	rows = []
	for indice, row in enumerate(tablero):
		if indice == (nro_row - 1):
			rows = tablero[indice]
			del rows[0]
			del rows[7]
			return rows

#-----------------------------------------------------------#

def contenidoTodasLasColumnas(tablero):
	columns = []
	for nro_column in range(0, 7):
		columns.insert(7,contenidoColumna(nro_column,tablero))
	return columns

#-----------------------------------------------------------#

secuencia = [1, 2, 3, 7, 1, 7,]
tablero = tablerovacio()
if tiroValido(secuencia):
	tablero = completarTableroEnOrden(secuencia, tablero)
	dibujarTablero(tablero)
	print("La secuencia es valida")
else:
	print("Para que la secuencia sea valida los valores tienen que estar comprendidos entre el 1 y el 7")

print("#-----------------------------------------------------------#")
print(contenidoColumna(7, tablero))
print("#-----------------------------------------------------------#")
print(contenidoFila(6, tablero))
print("#-----------------------------------------------------------#")
