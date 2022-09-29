from pydoc import describe
from xml.dom.minidom import Childless
import numpy as np
import sys
import random

seed = 1 
boardSize = 4 
populationSize = 5 
probMutation = 0.5 
probCruza = 0.5 
numIteration = 1

#if len(sys.argv) == 7 :
#    seed = sys.argv[1]
#    boardSize = int(sys.argv[2])
#    populationSize = int(sys.argv[3])
#    probCruza = float(sys.argv[4])
#    probMutation = float(sys.argv[5])
#    numIteration = int(sys.argv[6]) 
#else:
#    print('Formato de argumentos ingresados no es válido: <Valor de la semilla> <Tamaño del tablero> <Tamaño de la población> <Probabilidad de cruza> <Probabilidad de mutación> <Número de iteraciones>')
#    sys.exit()

random.seed(seed)

def ValueRandom():
    value = random.random()
    return value

def Value_N(x):
    value = random.randint(1,x)
    return value  

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
        #populationArray.append(my_array)
        populationArray[i] = my_array
        i+=1
    return populationArray

#Calcula el fitness de todos los individuos y retorna un array 
def fitness(array):
    fitnessArray = np.zeros(len(array),dtype=int) #Array que contiene las colisiones de cada individuo
    my_matrix = np.zeros((len(array),len(array)), dtype=int)
    
    for n in range(len(array)):
        my_matrix[array[n]][n] = 1
    
    for n in range(len(array)):
        values = [array[n],n]  # 0 es fila, 1 es columna
        for x in range(1,len(array)):
            if((values[0]-x >= 0 and values[1]+x) <= len(array)-1):
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
    return fitnessArray
    # print(my_matrix.reshape((len(array),len(array))))

def arrayFitness(poblacion):
    arrayFitness = np.empty(populationSize)
    for i in range(0,populationSize):
        collisions = 0
        for j in range(0,boardSize-1):
            for k in range(j+1,boardSize):
                if abs(j-k)-abs(poblacion[i][j]-poblacion[i][k]) == 0 or abs(j-k)-abs(poblacion[i][j]-poblacion[i][k]) == 1:
                    collisions = collisions + 1
        arrayFitness[i] = collisions
    return arrayFitness

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

def getIndexCruza(random, arrayProbCruza):
    for i in range(0, populationSize):
        if random <= arrayProbCruza[i]:
            return i

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
            print(test_list)
    return test_list
            
def mutation(array):
    print("array entrada", array)
    index1 = Value_0_N(boardSize-1)
    index2 = Value_0_N(boardSize-1)
    while index1 == index2:
        index1 = Value_0_N(boardSize-1)
        index2 = Value_0_N(boardSize-1)
    array[index1], array[index2] = array[index2], array[index1]
    print("array salida ", array)
    return array



Poblacion = starterPob(populationSize,boardSize)
iterations = 0
FitnessPoblacion = arrayFitness(Poblacion)  



while (0 in FitnessPoblacion) or (iterations < numIteration):
    descendencia = None
    FitnessPoblacion = arrayFitness(Poblacion)  
    ProbCruza = arrayProbCruza(FitnessPoblacion)     
    index_p1 = 0
    index_p2 = 0
    while index_p1 == index_p2:
        prob = ValueRandom()
        index_p1 = getIndexCruza(prob,ProbCruza)
        prob = ValueRandom()
        index_p2 = getIndexCruza(prob,ProbCruza)
    cruza = cruzover(Poblacion[index_p1],Poblacion[index_p2])
    print(cruza)
    for i in range(0, np.size(cruza,0)):
        cruza[i] = rectification(cruza[i])
    print(cruza)

    iterations = iterations + 1




