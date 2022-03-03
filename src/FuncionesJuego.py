def soltarFichaEnColumna(ficha, column, tablero):
		for row in range(6, 0, -1):
				if tablero[row - 1][column - 1] == 0:
						tablero[row -1][column - 1] = ficha
						return

#----------------------------TEST-READY----------------------------#

def completarTableroEnOrden(column, turno, tablero):
    if turno == 1:
        soltarFichaEnColumna(1, column, tablero)
    else:
        soltarFichaEnColumna(2, column, tablero)

    return tablero

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

def contenidoTodasLasFilas(tablero):
	rows_all = []
	for row in tablero:
		rows_all.append(row)
	return rows_all

#----------------------------TEST-READY----------------------------#

def contenidoTodasLasColumnas(tablero):
	columns_all = []
	for nro_column in range(1, 8):
		columns_all.append(contenidoColumna(nro_column,tablero))
	return columns_all

#----------------------------TEST-READY----------------------------#
