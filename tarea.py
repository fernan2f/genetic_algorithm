import numpy as np

populationSize = 5
seed = 2
boardSize = 5
crossover = 5
mutation = 5
iteration = 100
error = ""

#Para inicializar la población inicial , size = numero de reinas
def starterPob(populationSize, boardSize):
    i=0
    populationArray = []
    while(i < populationSize):
        my_array = np.arange(0, boardSize, 1, dtype=int)
        np.random.shuffle(my_array)
        populationArray.append(my_array)
        i+=1
    
    return populationArray

#Calcula el fitness de todos los individuos y retorna un array 
def fitness(array):
    fitnessArray = np.zeros(len(array),dtype=int) #Array que contiene las colisiones de cada individuo
    my_matrix = np.zeros((len(array),len(array)), dtype=int)
    
    for n in range(len(array)):
        my_matrix[array[n]][n] = 1;
    
    for n in range(len(array)):
        values = [array[n],n]  # 0 es fila, 1 es columna
        for x in range(1,len(array)):
            if(values[0]-x >= 0 and values[1]+x <= len(array)-1):
                # sup derecha
                if(my_matrix[values[0]-x][values[1]+x]== 1):
                    fitnessArray[n]+=1
                    # print("sup derecha ",values," con ",values[0]-x,values[1]+x) 
                    
            if(values[0]+x <= len(array)-1  and values[1]-x >= 0):
                # inf izq
                if(my_matrix[values[0]+x][values[1]-x]== 1):
                    fitnessArray[n]+=1
                    # print("inf izq ",values," con ",values[0]+x,values[1]-x)
                    
            if(values[0]-x >=0  and values[1]-x >= 0):
                # sup izq
                if(my_matrix[values[0]-x][values[1]-x]== 1):
                    fitnessArray[n]+=1
                    # print("sup izq ",values," con ",values[0]-x,values[1]-x)
                    
            if(values[0]+x <= len(array)-1  and values[1]+x <= len(array)-1 ):
                # inf der
                if(my_matrix[values[0]+x][values[1]+x]== 1):
                    fitnessArray[n]+=1
                    # print("inf der ",values," con ",values[0]+x,values[1]+x)
    return sum(fitnessArray)
    # print(my_matrix.reshape((len(array),len(array))))
    

print(" \n 1. Tamaño población (Actual {}) \n 2. Valor de la semilla (Actual {}) \n 3. Tamaño tablero (Actual {}) \n 4. Probabilidad cruza (Actual {}%) \n 5. Probabilidad mutación (Actual {}%) \n 6. Cantidad iteraciones (Actual {}) \n 0. Ejecutar código"  .format(populationSize,seed,boardSize,crossover,mutation, iteration))
command = input('Seleccione una opción: ')

def isNumber(value):
    try:
        float(value)
    except ValueError:
        return bool(False)
    return bool(True)

while command != '0':
    error = ""
    match command:
        case '1':
            populationSize = int(input('Ingrese el tamaño de la población: '))
            if not isNumber(populationSize):
                error = "No has ingresado un número"
                populationSize = 5 
        case '2':
            seed = int(input('Ingrese el valor de la semilla: '))
            if not isNumber(seed):
                error = "No has ingresado un número"
                seed = 2
        case '3':
            boardSize = int(input('Ingrese el tamaño del tablero: '))
            if not isNumber(boardSize):
                error = "No has ingresado un número"
                boardSize = 5
        case '4':
            crossover = int(input('Ingrese la probabilidad de cruza: '))
            if not isNumber(crossover):
                error = "No has ingresado un número"
                crossover = 5
        case '5':
            mutation = int(input('Ingrese la probabilidad de mutación: '))
            if not isNumber(mutation):
                error = "No has ingresado un número"
                mutation = 5
        case '6':
            iteration = int(input('Ingrese la cantidad de iteraciones: '))
            if not isNumber(iteration):
                error = "No has ingresado un número"
                iteration = 100
        case other:
            error = "No has ingresado una opción valida"
    print(" \n 1. Tamaño población (Actual {}) \n 2. Valor de la semilla (Actual {}) \n 3. Tamaño tablero (Actual {}) \n 4. Probabilidad cruza (Actual {}%) \n 5. Probabilidad mutación (Actual {}%) \n 6. Cantidad iteraciones (Actual {}) \n 0. Ejecutar código"  .format(populationSize,seed,boardSize,crossover,mutation, iteration))
    print(error)
    command = input('Seleccione un valor a modificar: ')




population = starterPob(populationSize, boardSize)

print(population)