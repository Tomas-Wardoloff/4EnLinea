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

def tiroValido(column):
	if column < 1 or column > 7:
	    return False
	return True

#----------------------------TEST-READY----------------------------#
