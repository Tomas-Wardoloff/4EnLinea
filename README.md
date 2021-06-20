# Cuatro en línea
Este es un trabajo para la materia  **Adaptación del ambiente de trabajo** 2021 del **Intituto Politécnico Superiro** de la ciudad de Rosario, Argentina. En esta materia aprendemos sobre herramientas que nos permiten trabajar con software de forma profecional, tales como: *sistemas de control de versiones*, *testing automatizado*, *integración continua*, entre otras herramientas.

En este archivo `README.dm` se encuentran documentadas las distintas clases de esta materia

---------------

##Primer Cuatrimestre
####Tabla de contenidos
   * [Clase 1](#Clase 1)
   * [Clase 2 parte 1](#Clase 2 parte 1)
   * [Clase 2 parte 2](#Clase 2 parte 2)
   * [Clase 3](#Clase 3)
   * [Clase 4](#Clase 4)
   * [Clase 5](#Clase 5)
   * [Clase 6](#Clase 6)
   * [Clase 7](#Clase 7)
   * [Clase 8](#Clase 8)
   * [Clase 9](#Clase 9)

# Cuatro en línea
Este es un trabajo para la materia  **Adaptación del ambiente de trabajo** 2021 del **Instituto Politécnico Superior** de la ciudad de Rosario, Argentina. En esta materia aprendemos sobre herramientas que nos permiten trabajar con software de forma profesional, tales como: *sistemas de control de versiones*, *testing automatizado*, *integración continua*, entre otras herramientas.

En este archivo `README.dm` se encuentran documentadas las distintas clases de esta materia

---------------

##Primer Cuatrimestre
####Tabla de contenidos
* [Clase 1](#Clase 1)
* [Clase 2](#Clase 2)
	* [Parte 1](#Parte 1)
	* [Parte 2](#Parte 2)
* [Clase 3](#Clase 3)
* [Clase 4](#Clase 4)
* [Clase 5](#Clase 5)
* [Clase 6](#Clase 6)
* [Clase 7](#Clase 7)
* [Clase 8](#Clase 8)
* [Clase 9](#Clase 9)

##Clase 1

<p align="center">
	<a href="https://www.youtube.com/watch?v=I6sT5VgwFUE" target="_blank"><img src="https://i.ytimg.com/vi/I6sT5VgwFUE/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**
Todos los años se elige un juego como eje temático de la materia, este año utilizamos el [Cuatro en línea](http:/https://es.wikipedia.org/wiki/Conecta_4/ "Cuatro en línea"), el cual vamos a intentar recrear en python. Para poder desarrollarlo debemos saber que el tablero se encuentra conformado por 6 filas y 7 columnas y que las posiciones en la que se van a soltar las fichas van a estar dadas por una secuencia conformada por las columnas del tablero, donde el primer valor corresponde al jugador 1 y el segundo al jugador 2 y así con todos los valores. 

El programa en python sería de la siguiente manera:
```python
secuencia = [1, 2, 3, 1]
dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
```
Tenemos la secuencia de las columnas en las que se van a tirar las fichas y tres funciones encargadas de crear el tablero vacío, completar el tablero con la secuencia dada y por último dibujar el tablero.

También sabemos que las fichas pueden tomar los valores de 1 o 2, representando a los jugadores y que el valor 0 representa la ausencia de fichas. Para facilitar la tarea, se nos brinda las siguientes funciones:
```python
def tableroVacio():
	return [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
]
```
```python
def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range(6, 0, -1):
		if tablero[fila - 1][columna - 1] == 0:
			tablero[fila -1][columna -1] = ficha
		return
```
**Tarea:**
Definir la función *completarTableroEnOrden* la cual toma como parámetros la secuencia y el tablero vacío y retornara el tablero ya completo y definir la función *dibujarTablero*, la cual debe representar el tablero en formato de texto en la terminal.

##Clase 2
<a name="Parte 1"/>
**Parte 1:**
<p align="center">
	<a href="https://youtu.be/BEs03e0Lkkw" target="_blank"><img src="https://img.youtube.com/vi/BEs03e0Lkkw/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

<a name="Parte 2"/>
**Parte 2:**
<p align="center">
	<a href="https://youtu.be/yIUBjWA1LDE" target="_blank"><img src="https://img.youtube.com/vi/yIUBjWA1LDE/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

##Clase 3
<p align="center">
	<a href="https://youtu.be/8jL0scwxzSw" target="_blank"><img src="https://i.ytimg.com/vi/8jL0scwxzSw/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

##Clase 4
<p align="center">
	<a href="https://youtu.be/X6CP4by3s-Y" target="_blank"><img src="https://img.youtube.com/vi/X6CP4by3s-Y/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

##Clase 5
<p align="center">
	<a href="https://youtu.be/3UU_Yg3Zda0" target="_blank"><img src="https://img.youtube.com/vi/3UU_Yg3Zda0/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

##Clase 6
<p align="center">
	<a href="https://youtu.be/69fZF0xUnjA" target="_blank"><img src="https://img.youtube.com/vi/69fZF0xUnjA/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

##Clase 7 
<p align="center">
	<a href="https://youtu.be/djuiI8CqFdA" target="_blank"><img src="https://img.youtube.com/vi/djuiI8CqFdA/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

##Clase 8
<p align="center">
	<a href="https://youtu.be/DivoEmsAo0g" target="_blank"><img src="https://img.youtube.com/vi/DivoEmsAo0g/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

##Clase 9
<p align="center">
	<a href="https://youtu.be/iV9UfirtV44" target="_blank"><img src="https://img.youtube.com/vi/iV9UfirtV44/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

