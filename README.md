# Cuatro en línea
Este es un trabajo para la materia  **Adaptación del ambiente de trabajo** 2021 del **Instituto Politécnico Superior** de la ciudad de Rosario, Argentina. En esta materia aprendemos sobre herramientas que nos permiten trabajar con software de forma profesional, tales como: *sistemas de control de versiones*, *testing automatizado*, *integración continua*, entre otras herramientas.

En este archivo `README.dm` se encuentran documentadas las distintas clases de esta materia.

**Alumno:** *Tomás Wardoloff*

**Profesor**: *Mariano D'agostino*

---------------

## Primer Cuatrimestre
#### Tabla de contenidos
* [Clase 1](#Clase1)
* [Clase 2](#Clase2)
	* [Parte 1](#Parte1)
	* [Parte 2](#Parte2)
* [Clase 3](#Clase3)
* [Clase 4](#Clase4)
* [Clase 5](#Clase5)
* [Clase 6](#Clase6)
* [Clase 7](#Clase7)
* [Clase 8](#Clase8)
* [Clase 9](#Clase9)

<a name="Clase1"/>

## Clase 1
<p align="center">
	<a href="https://www.youtube.com/watch?v=I6sT5VgwFUE" target="_blank"><img src="https://i.ytimg.com/vi/I6sT5VgwFUE/maxresdefault.jpg" 
alt="Miniatura Clase 1" width="426" height="240" border="10"/></a>
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

<a name="Clase2"/>

## Clase 2

<a name="Parte1"/>

**Parte 1:**
<p align="center">
	<a href="https://youtu.be/BEs03e0Lkkw" target="_blank"><img src="https://img.youtube.com/vi/BEs03e0Lkkw/maxresdefault.jpg" 
alt="Miniatura Clase 2 Parte 1" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

En esta clase se nos brinda una posible solución a la tarea de la clase anterior y se nos explica el funcionamiento de las distintas funciones que conforman el programa. Soluciones dadas:
```python
def completarTableroEnOrden(secuencia, tablero):
	for indice, columna in enumerate(secuencia):
		fichaNumero = 1 + (indice % 2)
		soltarFichaEnColumna(fichaNumero, columna, tablero)
	return tablero
```
```python
def dibujarTablero(tablero):
	for fila in tablero:
		for celda in fila:
			if celda == 0:
				print(' ', end='')
			else:
				print(' %s ' % celda, end='')
		print('')
```
**Tarea:**

No hay tarea para esta clase.

<a name="Parte2"/>

**Parte 2:**
<p align="center">
	<a href="https://youtu.be/yIUBjWA1LDE" target="_blank"><img src="https://img.youtube.com/vi/yIUBjWA1LDE/maxresdefault.jpg" 
alt="Miniatura Clase 2 Parte 2" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

Las empresas que trabajan con software viven de vender sus servicios, por ende no se pueden dar el lujo de no tener una copia de seguridad de sus principal activo. Dichas empresas para tener un respaldo de su código, utilizan un sistema de control de versiones en lugar de un sistema de copias de seguridad.

Estos sistemas de control de versiones funcionan tomando instantáneas del contenido de los archivos y así crear un historial de las distintas versiones de un archivo donde podemos ver como el contenido del mismo se fue modificando con el pasar del tiempo.
Algunos de los sistema de control de versiones más conocido son: [Git](https://git-scm.com/), [Azure DevOps Server](https://azure.microsoft.com/), [Mercurial](http://mercurial.selenic.com/). Para esta materia vamos a utilizar [Git](https://git-scm.com/), el cual podes instalar desde su página oficial.

[Git](https://git-scm.com/) nos permite crear repositorios, los cuales son como cajas que nos permiten poner cosas las cuales vamos a poder versionar a medida qeu pasa el tiempo. Con el comando `git init .` vamos a inicializar un repositorio en nuestro directorio actual, en el cual debemos tener nuestro prototipo del *Cuatro en línea*. Cuando chequeamos el estado de nuestro repositorio con el comando `git status`, nos va a decir que tenemos un archivo *untracked*, es decir, que git sabe de su existencia pero no está siguiendo sus modificaciones. Para poder hacer el seguimiento de un archivo debo ejecutar el siguiente comando `git add archivo` y utilizaremos el comando `git commit -m "nombre del commit"` para tomar una instantánea de los archivos que se hayan agregado.

Diferentes estados de un archivo en [Git](https://git-scm.com/)
<p align="center">
    <img src="https://i.stack.imgur.com/3rFpi.png" alt="File Status"/>
</p>
    
> Para poder hacer un commit, previamente nos tenemos que identificar, con un nombre de usuario y un email `git config user.name "user name"` y `git config user.email "user@email.com"`

Ahora si realizamos cualquier cambio en el archivo y luego verificamos el estado del repositorio veremos que el archivo ha sido modificado. Si queremos podemos ver las líneas del archivo que sea modificado con `git diff`. Si quisiéramos agregar al repositorio este cambio que realizamos deberíamos repetir la secuencia de comandos que se detallo anteriormente.

> Con el comando `git log --oneline` podemos ver en una única línea los distintos commits que se realizaron en nuestro repositorio

**Tarea:**

Instalar Git, crear un repositorio y agregar el archivo del prototipo y crear un función que valide que las columnas donde se sueltan las fichas estén entre el 1 y el 7.

<a name="Clase3"/>

## Clase 3
<p align="center">
	<a href="https://youtu.be/8jL0scwxzSw" target="_blank"><img src="https://i.ytimg.com/vi/8jL0scwxzSw/maxresdefault.jpg" 
alt="Miniatura Clase 3" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

<a name="Clase4"/>

## Clase 4
<p align="center">
	<a href="https://youtu.be/X6CP4by3s-Y" target="_blank"><img src="https://img.youtube.com/vi/X6CP4by3s-Y/maxresdefault.jpg" 
alt="Miniatura Clase 4" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

<a name="Clase5"/>

## Clase 5
<p align="center">
	<a href="https://youtu.be/3UU_Yg3Zda0" target="_blank"><img src="https://img.youtube.com/vi/3UU_Yg3Zda0/maxresdefault.jpg" 
alt="Miniatura Clase 5" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea:**

<a name="Clase6"/>

## Clase 6
<p align="center">
	<a href="https://youtu.be/69fZF0xUnjA" target="_blank"><img src="https://img.youtube.com/vi/69fZF0xUnjA/maxresdefault.jpg" 
alt="Miniatura Clase 6" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

<a name="Clase7"/>

## Clase 7
<p align="center">
	<a href="https://youtu.be/djuiI8CqFdA" target="_blank"><img src="https://img.youtube.com/vi/djuiI8CqFdA/maxresdefault.jpg" 
alt="Miniatura Clase 7" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

<a name="Clase8"/>

## Clase 8
<p align="center">
	<a href="https://youtu.be/DivoEmsAo0g" target="_blank"><img src="https://img.youtube.com/vi/DivoEmsAo0g/maxresdefault.jpg" 
alt="Miniatura Clase 8" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

<a name="Clase9"/>

## Clase 9
<p align="center">
	<a href="https://youtu.be/iV9UfirtV44" target="_blank"><img src="https://img.youtube.com/vi/iV9UfirtV44/maxresdefault.jpg" 
alt="Miniatura Clase 9" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

**Tarea**

