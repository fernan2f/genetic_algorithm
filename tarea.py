import numpy as np
import sys
import random


if len(sys.argv) == 7 :
   seed = sys.argv[1]
   boardSize = int(sys.argv[2])
   populationSize = int(sys.argv[3])
   probCruza = float(sys.argv[4])
   probMutation = float(sys.argv[5])
   numIteration = int(sys.argv[6])
else:
   print('Formato de argumentos ingresados no es válido: <Valor de la semilla> <Tamaño del tablero> <Tamaño de la población> <Probabilidad de cruza> <Probabilidad de mutación> <Número de iteraciones>.')
   exit()

if populationSize <= 1:
    print("La poblacion tiene que ser mayor a uno para poder generar los hijos.")
    exit()

random.seed(seed)

#Valor random entre 0 y 1
def ValueRandom():
    value = random.random()
    return value

#Valor random entre 1 y N
def Value_N(x):
    value = random.randint(1,x)
    return value  

#Valor random entre 0 y N
def Value_0_N(x):
    value = random.randint(0,x)
    return value 

#Para inicializar la población inicial , size = numero de reinas
def starterPob(populationSize, boardSize):
    i=0
    populationArray = np.empty([populationSize,boardSize],dtype=int)
    while(i < populationSize):
        my_array = np.arange(0, boardSize, 1, dtype=int)
        np.random.shuffle(my_array)
        populationArray[i] = my_array
        i+=1
    return populationArray

#Calcula el fitness de todos los individuos de la poblacion y retorna un array 
def arrayFitness(poblacion):
    arrayFitness = np.empty(populationSize)
    for i in range(0,populationSize):
        collisions = 0
        for j in range(0,boardSize-1):
            for k in range(j+1,boardSize):
                if abs(j-k)-abs(poblacion[i][j]-poblacion[i][k]) == 0 :
                    collisions = collisions + 1
        arrayFitness[i] = collisions
    return arrayFitness

#Calcula la probabilidad que tiene un individuo de cruzarse con otro
def arrayProbCruza(arrayFitness):
    arrayProbCruza = np.empty(populationSize)
    totalInv = np.sum(arrayFitness)
    for i in range(0,populationSize):
        arrayProbCruza[i] = 1/(arrayProbCruza[i]/totalInv)
    totalReal = np.sum(arrayProbCruza)
    acc = 0
    for i in range(0,populationSize):
        acc = acc + arrayProbCruza[i]/totalReal
        arrayProbCruza[i] = acc
    return arrayProbCruza

#Se obtiene el indice de un individuo de la poblacion randomicamente segun la probabilidad de cruza
def getIndexCruza(random, arrayProbCruza):
    for i in range(0, populationSize):
        if random <= arrayProbCruza[i]:
            return i

#Se cruzan dos individuos de la poblacion y retorna los dos
def cruzover(p_1, p_2):
    corte = Value_N(boardSize)
    h_1 = np.concatenate((p_1[:corte],p_2[corte:]))
    h_2 = np.concatenate((p_2[:corte],p_1[corte:]))
    return np.vstack((h_1,h_2))
    
def rectification(test_list):
    ## valores repeditos  
    u, c = np.unique(test_list, return_counts=True)
    repetidos = u[c > 1]
    ## valores restantes
    res = np.array(list(set(range(len(test_list))) - set(test_list)))
    for i in repetidos:
        y = np.where(test_list== i)
        y = y[0]
        rango = y.size       
        for j in range(0,rango-1):
            ## seleccion posicion repetido al azar
            Select = Value_0_N(rango-1) 
            position = y[Select]
            y = np.delete(y ,Select)
            ## seleccionar valor faltante
            indexRest = Value_0_N(len(res)-1)
            valueRest = res[indexRest]
            res = np.delete(res ,indexRest)
            test_list[position] = valueRest
    return test_list

#Se intercambia la posicion de dos elementos de un individuo de la poblacion randomicamente y se retorna
def mutation(array):
    index1 = Value_0_N(boardSize-1)
    index2 = Value_0_N(boardSize-1)
    while index1 == index2:
        index1 = Value_0_N(boardSize-1)
        index2 = Value_0_N(boardSize-1)
    array[index1], array[index2] = array[index2], array[index1]
    return array

Poblacion = starterPob(populationSize,boardSize) # Se inicializa la poblacion
iterations = 0 # Se inicializa el numero de iteraciones
FitnessPoblacion = arrayFitness(Poblacion)

while (iterations < numIteration):
    if 0 in FitnessPoblacion: # Se consulta al comienzo de cada iteracion (incluyendo la poblacion inicializada) si es que existe un individuo que es solucion 
        break
    descendencia = [] # Se inicializa la descendencia de la Poblacion
    FitnessPoblacion = arrayFitness(Poblacion) #Se consulta el fitness de la poblacion que ingresa a la iteracion o sea de una *generacion anterior*
    ProbCruza = arrayProbCruza(FitnessPoblacion)  #Se consulta la probabilidad de cruza de la poblacion de la generacion   
    while len(descendencia) < populationSize: # Se comienza una iteracion hasta que la nueva generacion sea del mismo tamaño que la poblacion inicial
        randomCruza = ValueRandom() # Se obtiene el valor randomicamente para determinar si se cruza o no
        if randomCruza <= probCruza: # Se consulta si se cruza
            index_p1 = 0
            index_p2 = 0
            while index_p1 == index_p2: # Ciclo para obtener indices distintos o sea que se cruzaran dos padres diferentes de la poblacion inicial
                prob = ValueRandom()
                index_p1 = getIndexCruza(prob,ProbCruza)
                prob = ValueRandom()
                index_p2 = getIndexCruza(prob,ProbCruza)
            cruza = cruzover(Poblacion[index_p1],Poblacion[index_p2]) # Se obtienen los dos hijos retornados de la cruza
            for i in range(0, np.size(cruza,0)):
                cruza[i] = rectification(cruza[i]) # Se rectifica cada hijo
            randomMutation = ValueRandom() # se obtiene el valor randomicamente para saber si se van a mutar los hijos
            if randomMutation <= probMutation: # Se consulta si se muta
                childMutate = Value_0_N(len(cruza)-1) # Se obtiene un el indice del hijo de forma randomica a mutar
                cruza[childMutate] = mutation(cruza[childMutate]) # se reemplaza el hijo por el hijo mutado
            if(len(descendencia)==0):#se consulta si la descendencia esta vacia para inicializarla 
                descendencia = cruza #Se inicializa la poblacion 
            else:
                if len(descendencia) - populationSize == 1: # En caso de que la poblacion sea de tamaño impar se debe consultar para que cuando llegue a la ultima cruza solo agrege un hijo a la descendencia 
                    SelectChild = Value_0_N(len(cruza)-1) # Se selecciona randomicamente el hijo a agregar en la descendencia 
                    descendencia = np.vstack((descendencia,cruza[SelectChild])) 
                else:
                    descendencia = np.vstack((descendencia,cruza)) # Se agregan los dos hijos resultantes de la cruza a la descendencia 
    Poblacion = descendencia
    FitnessPoblacion = arrayFitness(Poblacion)
    iterations = iterations + 1

(MejorSolucion,) = np.where(FitnessPoblacion == np.amin(FitnessPoblacion)) # Se Consulta el Valor minimo en el Array de Fitness y tambien su posicion(es)
print(Poblacion[MejorSolucion[0]]) # Se imprime por panttalla el Mejor individuo 
