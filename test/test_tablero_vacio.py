from src.CuatroEnLinea import tableroVacio#traigo lo que quiero probar del codigo principal

def test_tablero_vacio_tiene_6_filas():
    tablero = tableroVacio()
    
    assert len(tablero) == 6#chequea 

def test_tablero_vacio_tiene_7_columnas():
    tablero = tableroVacio()

    assert len(tablero[0]) == 7

