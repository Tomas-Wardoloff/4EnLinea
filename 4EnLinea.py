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
def tiroValido(columna):
    if columna <= 7 & columna >= 0:
        return 1
    else:
        return 0

tablero = tablerovacio()
for row in tablero:
    print(row)

for a in range(6, 0, -1):
    if a % 2 == 0:
        ficha=1
    else:
        ficha=2
    columna = input("\nInsertar Numero de Columna: ")
    if(tiroValido(columna)==1):
        soltarfichaencolumna(ficha, columna, tablero)
        for row in tablero:
            print(row)
    else:
        print("Ese no es un tiro valido. El valor tiene que estar entre 0 y 7")
        break
