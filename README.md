# Algoritmo genético para el problema de las N-reinas

En este algoritmo se resolverá el problema de las N reinas, el cual consiste en posicionar N reinas sin colisión entre ellas en el tablero. mediante el algoritmo genético a través del lenguaje de programación python . 


## Instalación

1. Asegurate de tener instalado <a href="https://www.python.org/">Python</a> >= `3.0`

2. Instalar libreria numpy 
   ```sh
   pip install numpy
   ```
 
 ## Ejecución
 
   1. Para iniciar el algoritmo de debe ejecutar por consola el siguiente comando
   ```sh
   python3 tarea.py <Valor de la semilla> <Tamaño del tablero> <Tamaño de la población> <Probabilidad de cruza> <Probabilidad de mutación> <Número de iteraciones>
   ```
Los parámetros de entradas serán de tipo:

* Valor de la semilla: Generador de los valores aleatorios. (Para una misma semilla se obtendrá siempre los mismos valores aleatorios) Es de cualquier tipo de variable
* Tamaño del tablero : Es la dimensión  del tablero de tipo NxN de tipo `entero`  
* Tamaño de la población :  Número de tableros de tipo `entero` que tiene que ser mayor o igual a 2
* Probabilidad de cruza : Variable que nos da la probabilidad de cruza, es de tipo `decimal` entre 0 y 1
* Probabilidad de mutación : Variable que nos da la probabilidad de mutación, es de tipo `decimal` entre 0 y 1
* Número de iteraciones : Variable de tipo `entero` del número de siglos que se representa en la cantidad de generaciones que se van a crear 


## Parámetros de salida

* Array del tamaño del tablero, con las posiciones de las reinas de la mejor solución

## Desarrolladores

* Fernando Fuentealba
* Bernardo Fernández
* Alexis Pinto
