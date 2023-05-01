
import igraph
import numpy as np

#classifica em : Simples, Dirigido, Multigrafo , Pseudografo , Multigrafo dirigido e Pseudografo dirigido
def tipoGrafo(matrix): 
    matrix = np.array(matrix)
    flag1 = flag2 = flag3 = 0 # uma flag
    for vi in range(0, np.shape(matrix)[0]):  # Para cada vértice vi
        for vj in range(0, np.shape(matrix)[0]): # Para cada vértice vj
            if matrix[vi][vj] != matrix[vj][vi]: # se é dirigido
                flag1 = 1 #quer dizer que é dirigido
            if matrix[vi][vj] > 1: # se tem arestas paralelas
                flag2 = 1 #quer dizer que tem aresta paralela
        if matrix[vi][vi] > 0: #se tem laço
            flag3 = 1 #tem laço

    if flag1 == 0 and flag2 == 0 and flag3 == 0:
        print( '0' )
        return 0 #simples
    elif flag1 == 1 and flag2 == 0 and flag3 == 0:
        print( '1' )
        return 1 #digrafo
    elif flag1 == 0 and flag2 == 1 and flag3 == 0:
        print( '20' )
        return 20 #multigrafo
    elif flag1 == 1 and flag2 == 1 and flag3 == 0:
        print( '21' )
        return 21 #multigrafo dirigido
    elif flag1 == 0 and flag2 == 1 and flag3 == 1:  
        print( '30' )     
        return 30 #pseudogrado
    elif flag1 == 1 and flag2 == 1 and flag3 == 1:   
        print( '31' ) 
        return 31 #pseudografo dirigido
    elif flag1 == 0 and flag2 == 0 and flag3 == 1:   
        print( '30' )
        return 30
    elif flag1 == 1 and flag2 == 0 and flag3 == 1:   
        print( '31' )
        return 31
def verificaAdjacencia(matrix, vi, vj):
    if matrix[vi][vj] or matrix[vj][vi]:
        return True
    else:
        return False
def calcDensidade(matrix):
    matrix = np.array(matrix)
    n = np.shape(matrix)[0]
    m = 0
    for vi in range(0, n):  # Para cada vértice vi
        for vj in range(0, n): # Para cada vértice vj
            m = m + 1
            
    res = float((m / (n * (n-1))))
    print("%.3f"%res)
    return ((m) / (n * (n-1)))
    
def  insereAresta(matrix, vi, vj):
    if matrix[vi][vj] == matrix[vj][vi]:
        matrix[vi][vj] = matrix[vi][vj] + 1
        matrix[vj][vi] = matrix[vj][vi] + 1
    else:
        matrix[vi][vj] = matrix[vi][vj] + 1
    return matrix
def insereVertice(matrix, vi):
    matrix = np.array(matrix)
    matrix = np.insert(matrix, vi , 0 , 1)
    matrix = np.insert(matrix, vi , 0 , 0)
    return matrix
def removeAresta(matrix, vi, vj): 
    if matrix[vi][vj] == matrix[vj][vi]:
        matrix[vi][vj] = -1
        matrix[vj][vi] = -1
    else:
        matrix[vi][vj] = -1
    return matrix
def  removeVertice(matrix, vi):
    for n in range(0, np.shape(matrix)):  
        matrix[vi][n] = -1
        matrix[n][vi] = -1
    return matrix
         


 


