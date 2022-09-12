
# populationSize = input("Ingrese el tamaño de la población")

populationSize = 10
seed = 2
boardSize = 3
crossover = 5
mutation = 5
iteration = 100
error = ""
print(" \n 1. Tamaño población (Actual {}) \n 2. Valor de la semilla (Actual {}) \n 3. Tamaño tablero (Actual {}) \n 4. Probabilidad cruza (Actual {}) \n 5. Probabilidad mutación (Actual {}) \n 6. Cantidad iteraciones (Actual {}) \n 0. Salir del menú"  .format(populationSize,seed,boardSize,crossover,mutation, iteration))
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
            populationSize = input('Ingrese el tamaño de la población: ')
            if not isNumber(populationSize):
                error = "No has ingresado un número"
                populationSize = 10 
        case '2':
            seed = input('Ingrese el valor de la semilla: ')
            if not isNumber(seed):
                error = "No has ingresado un número"
                seed = 2
        case '3':
            boardSize = input('Ingrese el tamaño del tablero: ')
            if not isNumber(boardSize):
                error = "No has ingresado un número"
                boardSize = 3
        case '4':
            crossover = input('Ingrese la probabilidad de cruza: ')
            if not isNumber(crossover):
                error = "No has ingresado un número"
                crossover = 5
        case '5':
            mutation = input('Ingrese la probabilidad de mutación: ')
            if not isNumber(mutation):
                error = "No has ingresado un número"
                mutation = 5
        case '6':
            iteration = input('Ingrese la cantidad de iteraciones: ')
            if not isNumber(iteration):
                error = "No has ingresado un número"
                iteration = 100
        case other:
            error = "No has ingresado una opción valida"
    print(" \n 1. Tamaño población (Actual {}) \n 2. Valor de la semilla (Actual {}) \n 3. Tamaño tablero (Actual {}) \n 4. Probabilidad cruza (Actual {}) \n 5. Probabilidad mutación (Actual {}) \n 6. Cantidad iteraciones (Actual {}) \n 0. Salir del menú"  .format(populationSize,seed,boardSize,crossover,mutation, iteration))
    print(error)
    command = input('Seleccione un valor a modificar: ')




