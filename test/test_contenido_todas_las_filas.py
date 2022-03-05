from src.FuncionesJuego import contenidoTodasLasFilas

def test_contenido_todas_las_columna():
    tablero = [
        [2, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 1],
    ]

    assert [[2, 0, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 0, 1]] == contenidoTodasLasFilas(tablero)
