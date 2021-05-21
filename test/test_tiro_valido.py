from src.CuatroEnLinea import tiroValido

def test_tiro_valido():
    secuencia = [1, 2, 3, 4, 5, 6, 10]

    assert not tiroValido(secuencia) 
