from src.FuncionesValidacion import tiroValido

def test_tiro_valido():
    secuencia = 5

    assert tiroValido(secuencia) 

def test_tiro_no_valido():
    secuencia = 10

    assert tiroValido(secuencia) == False
