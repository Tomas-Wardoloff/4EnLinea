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
#def tiroValido(columna):
#    if columna <= 7 & columna >= 0:
#        return 1
#    else:
#        return 0

def tiroValido(secuencia):
    for a in secuencia:
        if a >= 0 & a <= 7:
            return True
        else:
            return False


tablero = tablerovacio()

secuencia = [1, 2, 3, 4, 5, 6, 7, 8]
index = 0

for a in secuencia:
    if index == 0:
        ficha = 1
        index += 1
    else:
        if index % 2 == 0:
            ficha = 1
            index += 1
        else:
            ficha = 2
            index += 1
    if(tiroValido(secuencia)):
        soltarfichaencolumna(ficha, a, tablero)
    else:
        print("Ese no es un tiro valido. El valor tiene que estar entre 0 y 7")
        break

for row in tablero:
    print(row)

#for a in len(secuencia):
#    if a % 2 == 0:
#        ficha=1
#    else:
#       ficha=2
#    columna = input("\nInsertar Numero de Columna: ")
#    for columna in secuencia:
#        if(tiroValido(secuencia)):
#            soltarfichaencolumna(ficha, columna, tablero)
#        else:
#            print("Ese no es un tiro valido. El valor tiene que estar entre 0 y 7")
#            break
#        for row in tablero:
#                print(row)