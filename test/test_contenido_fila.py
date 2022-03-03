from src.FuncionesJuego import contenidoFila

def test_contenido_fila():
    tablero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 2, 1, 2, 0, 0, 0],
    ]
    
    assert [1, 2, 1, 2, 0, 0, 0] == contenidoFila(6, tablero)
