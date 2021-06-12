from src.CuatroEnLinea import tiroValido

def test_tiro_valido():
    secuencia = [1, 2, 3, 4, 5, 6]

    assert tiroValido(secuencia) 

def test_tiro_no_valido():
    secuencia = [0,10]

    assert tiroValido(secuencia) == False