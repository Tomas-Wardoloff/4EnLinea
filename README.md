# Cuatro en línea
Este es un trabajo para la materia  **Adaptación del ambiente de trabajo** 2021 del **Instituto Politécnico Superior** de la ciudad de Rosario, Argentina. En esta materia aprendemos sobre herramientas que nos permiten trabajar con software de forma profesional, tales como: *sistemas de control de versiones*, *testing automatizado*, *integración continua*, entre otras herramientas.

En este archivo `README.dm` se encuentran documentadas las distintas clases de esta materia.

**Alumno:** *Tomás Wardoloff*

**Profesor:** *Mariano D'agostino*

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
Resolución propuesta de la tarea de la clase anterior:
```python
def secuenciaValida(secuencia):
    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True
```
Hasta ahora todos los commits que hicimos viven en nuestro repositorio local, si quisiéramos hacer un respaldo de estos commits en la nube, tenemos que utilizar un repositorio remoto. Hay varias empresas que ofrecen estos servicios de repositorios remotos, tales como [GitHub](https://github.com), [GitLab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/product/), [Gogs](https://gogs.io/). Para esta materia vamos a utilizar [GitHub](https://github.com), donde deberemos crearnos una cuenta antes de poder crear un repositorio remoto.

Al crear un nuevo repositorio se nos va a pedir un nombre para el mismo y si queremos que el repositorio sea público o privado. Luego de este paso se nos brindan varias opciones para poder hacer nuestros primeros commits a este repositorio. Como nosotros ya tenemos un repositorio con commits de forma local, lo que vamos a hacer es subir dicho commits al repositorio remoto. Para ello, primero debemos conectar nuestro repositorio local con el repositorio remoto, con el comando `git remote add origin https://dirección-del-repostorio.git`, luego subimos nuestros commits al mismo con el comando `git push origin master`, donde origin hace referencia al repositorio remoto y master hace referencia a la rama en la que nos encontramos (tema que se vera más adelante).

> [GitHub](https://github.com) nos provee dos formas para conectarse al repositorio remoto: mediante *HTTPS* o mediante *SSH*. Si utilizamos *HTTPS* vamos a tener que escribir nuestra contraseña cada vez que queramos sincronizar los commits entre el repositorio remoto y el local. En cambio con *SSH*, se crea un juego de clave pública-privada y la conexión se hace automáticamente.

Ahora si vamos a nuestra cuenta de [GitHub](https://github.com) y entramos al repositorio que creamos podremos ver el archivo con el que estuvimos trabajando las otras clases, los commits que realizamos, entre otras cosas.

**Tarea:**

Crear un repositorio público en [GitHub](https://github.com) y hacer un push de todos los commits que tengamos en nuestro repositorio local.

<a name="Clase4"/>

## Clase 4
<p align="center">
	<a href="https://youtu.be/X6CP4by3s-Y" target="_blank"><img src="https://img.youtube.com/vi/X6CP4by3s-Y/maxresdefault.jpg" 
alt="Miniatura Clase 4" width="426" height="240" border="10"/></a>
</p>

**Resumen:**

En esta clase vimos el funcionamiento de los comandos `git pull` y `git push`. Para poder entender mejor cómo funcionan estos comandos, se planteó la situación en la cual debemos trasladar nuestro trabajo en casa a una oficina de trabajo y viceversa, sin utilizar pendrives o correo electrónico, solo con el sistema de control de versiones.
Una opción para esto es clonar el repositorio, con el comando `git clone https://dirección-del-repostorio.git`, el cual nos traerá una copia idéntica del repositorio que se encuentra en Github. Luego de clonar el repositorio tenemos que identificarnos como hicimos anteriormente con los comandos `git config user.name "user name"` y `git config user.email "user@email.com"`para posteriormente poder realizar commits.

> En el caso que se trate de un repositorio público este se clonara sin más, en cambio, si es privado git nos consultara por nuestra contraseña o nuestro juego de llave pública-privada dependiendo de la seguridad que use el repositorio

En esta clase también desarrollamos la función contenidoColumna, la cual toma como parámetro la posición de la columna a mostrar y el tablero.
```python
def contenidoColumna(nro_columna, tablero):
    columna = []
    for file in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda)
    return columna
```
Luego de modificar nuestro código y de haber hecho el commit, con el comando `git status` podremos ver que nuestro repositorio local se encuentra x cantidad de commits por delante de nuestro repositorio remoto, es decir, que lo que tenemos en nuestra computadora no es igual a lo que se encuentra en [GitHub](https://github.com). Para migrar dichos cambios al repositorio ejecutamos el comando `git push origin master` o `git push origin main` según corresponda. En caso contrario, si el repositorio de [GitHub](https://github.com) se encuentra x cantidad de commits por delante de nuestro repositorio local, podemos traernos los cambios con el comando `git pull origin master`

> En el caso de que queramos hacer un commit de una posición de nuestro código, debemos utilizar el comando `git add -p prototipo.py` el cual nos permite hacer una instantánea de lo que vemos en pantalla y no de todo el código.

**Tarea:**

Definir la función contenidoFila, contenidoTodasLasFilas y contenidoTodasLasColumnas.

<a name="Clase5"/>

## Clase 5
<p align="center">
	<a href="https://youtu.be/3UU_Yg3Zda0" target="_blank"><img src="https://img.youtube.com/vi/3UU_Yg3Zda0/maxresdefault.jpg" 
alt="Miniatura Clase 5" width="426" height="240" border="10"/></a>
</p>

**Resumen:**
En esta clase vimos que son las ramas. Las ramas son simplemente etiquetas, las cuales apuntan al último commit de una historia de commits, es decir, que nuestra rama main que tenemos en nuestro repositorio es básicamente una flecha que apunta al último commit que hicimos y al mismo tiempo este apunta a un commit anterior.

> Para poder entender mejor el funcionamiento de las ramas podes visitar la página [Learn Git Branching](https://learngitbranching.js.org/?locale=es_ES) la cual se uso en esta clase.

Si deseamos crear otra rama en nuestro repositorio debemos ejecutar el comando `git branch NombreDeLaRama`, pero luego de crearlas debemos trasladarnos a la misma con el comando `git checkout NombreDeLaRama`, ya que sino todos los commits que hagamos van a seguir perteneciendo a la rama main.

> Podemos crear una rama y movernos a ella, al mismo tiempo, con el comando `git checkout -b NombreDeLaRama`.

En caso de queramos unir dos ramas, lo podemos hacer mediante un commit que las unifique, lo cual se denomina merge(mezclar). Estando en una de las ramas le indicamos a git que queremos mezclar los commits de la otra rama, con el comando `git merge NombreDeLaRama`, el cual lo que hace es crear un nuevo commit que tiene como ancestros a los últimos commits de las ramas que estoy mezclando. En caso de querer borrar una rama, en la cual no nos encontremos, debemos ejecutar el comando `git branch -D NombreDeLaRama`.
También cabe destacar la existencia de un puntero/rama especial llamada *Head* la cual apunta al último commit de la rama en la que nos encontramos.

Algo interesante que podemos ver con el tema de las ramas es el pull request. Supongamos que creamos una rama, hacemos commits en la misma y trasladamos dichos commits al repositorio remoto con el comando `git push origin NombreDeLaRama`. Cuando hacemos el push podremos ver que se nos da la opción de crear una pull request, lo cual es una instrucción que le damos a [GitHub](https://github.com) para crear una "petición" para mezclar el contenido de dos ramas. Desde la interfaz visual que nos brinda [GitHub](https://github.com) podemos ver varias cosas como las ramas a mezclar, los archivos que han sido modificados y también nos permite rechazar, aceptar y hacer comentarios sobre la pull request.

**Tarea:**

Crear una nueva rama en nuestro repositorio, en la cual debes modificar el prototipo del cuatro en línea para mostrar el borde del tablero, crear un pull request y finalmente hacer un merge entre la rama principal y la rama recién creada.

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

En esta clase hicimos uso del sistema de dependencias de paquetes, las dependencias son programas que escribe la comunidad, los cuales podemos descargar y utilizar. Para esta clase utilizamos un paquete el cual nos permite crear test, los test son pruebas que nos permiten comprobar el correcto funcionamiento de distintas partes de nuestro código.

Para poder instalar dicha dependencia vamos a hacer uso de pip, el cual es el gestor de dependencias de python (viene instalado junto python), con el comando `pip install pytest` o `pip3 install pytest` (dependiendo de la versión de python que estemos utilizando) y en su defecto con el comando `py -m pip install pytest`.

Antes de poder hacer uso de pytest debemos reorganizar la estructura de nuestro proyecto, creando dos carpetas llamadas *src* y *test*, donde la carpeta *src* contendrá un archivo llamado *_init_.py* (el nombre del archivo está compuesto por dos guiones bajos tanto del lado izquierdo de init como del lado derecho, pero Github no me deja ponerlos) y el archivo de nuestro proyecto. Hay que tener en cuenta que no podemos mover el archivo de nuestro proyecto así sin más, ya que git interpretará que el archivo ha sido borrado, por ende lo tenemos que mover desde la consola usando git, con el comando ``git mv prototipo.py src/``. Por otro lado la carpeta *test* contendrá un archivo *_init__.py* (al igual que la carpeta *src*) y todos los test que vayamos a realizar.

Una vez ya reorganizado nuestro proyecto, podemos realizar nuestra primera prueba automatizada. Crearemos un nuevo archivo en el directorio *test*, llamado *test_tablero_vacio.py*, la estructura de este test será la siguiente:

```python
from src.prototipo import tableroVacio

def test_tablero_vacio_tiene_6_filas():
    tablero = tableroVacio()
    
    assert len(tablero) == 6
```
Este código lo que hace es importar la función tableroVacio desde nuestro prototipo y desde la función definida, comprueba que la longitud del tablero creado sea de 6. Ten en encuenta que todos los test que queramos hacer deben estar dentro de una función llamada test_algo y la instrucción encargada de la validación es assert. Para ejecutar nuestros test usaremos el comando ``python -m py.test``.

De la misma manera, en el archivo anterior, podemos definir otra función que compruebe que el tablero posee 7 columnas, de la siguiente manera:
```python
from src.prototipo import tableroVacio

def test_tablero_vacio_tiene_7_columnas():
    tablero = tableroVacio()
    
    assert len(tablero[0]) == 7
```
Siguiendo esta estructura podemos validar las distintas partes de nuestro código, así mejorar la calidad de nuestro software. 

**Tarea**

Crear un test para cada una de las funciones del programa, menos de la función que imprime el contenido del tablero en la pantalla.


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

En esta clase se ven ejemplos de proyectos que utilizan las distintas herramientas que estuvimos viendo a lo largo de las clases anteriores, tales como: [Visual Studio Code](https://github.com/microsoft/vscode), [Inskcap](https://gitlab.com/inkscape/inkscape), [Grafana](https://github.com/grafana/grafana)

**Tarea**

No hay tarea para esta clase.
