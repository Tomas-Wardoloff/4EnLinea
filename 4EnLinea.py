def tablerovacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
def soltarfichaencolumna(ficha, columna, tablero):
    for row in range(6, 0, -1):
        if tablero[row - 1][int(columna) - 1] == 0:
            tablero[row - 1][int(columna) - 1] = ficha
            return

tablero = tablerovacio()
for row in tablero:
    print(row)
secuencia = [1, 2, 3, 1]

for a in range(6, 0, -1):
    if a % 2 == 0:
        ficha=1
    else:
        ficha=2
    columna = input("\nInsertar Numero de Columna: ")
    soltarfichaencolumna(ficha, columna, tablero)
    for row in tablero:
        print(row)
