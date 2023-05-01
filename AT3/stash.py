import numpy as np

def criaListaAdjacencias(matrix):
    matrix = np.array(matrix)
    adj_list = {}
    for i in range(matrix.shape[0]):
        adj_list[i] = []
        for j in range(matrix.shape[0]):
            weight = matrix[i][j]
            if weight != 0:
                for k in range(weight):
                    adj_list[i].append(j)

    return adj_list
def tipoGrafo(adj_list):
    flag1 = flag2 = flag3 = 0 # uma flag
    for node in adj_list:  
        for edge in adj_list[node]:
            if node not in adj_list[edge]: # se é dirigido
                flag1 = 1 #quer dizer que é dirigido
            if len(adj_list[node]) != len(set(adj_list[node])):# se tem arestas paralelas
                flag2 = 1 #quer dizer que tem aresta paralela
        if node in adj_list[node]:  #se tem laço
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
def calcDensidade(adj_list):
    m = 0
    for node in adj_list:  
        for edge in adj_list[node]:
            m = m + 1
            
    res = float((m / (len(adj_list) * (len(adj_list)-1))))
    print("%.3f"%res)
    return ((m) / (len(adj_list) * (len(adj_list)-1)))

def  insereArestaLista(adj_list, vi, vj):
    adj_list[vi].append(vj)
    adj_list[vi].sort()
    adj_list[vj].append(vi)
    adj_list[vj].sort()

    return print(adj_list)

def  insereVerticeLista(adj_list, vi):
    vi = len(adj_list)
    if vi not in adj_list:
        adj_list[vi] = []
    return print(adj_list)
    
def removeArestaLista(adj_list, vi, vj):
    if vi in adj_list[vj] and vj in adj_list[vi]:
        adj_list[vi].remove(vj)
        adj_list[vj].remove(vi)
    else:
        adj_list[vi].remove(vj)
    return print(adj_list)

def removeVerticeLista(adj_list, vi):
    for v in adj_list:
        while vi in adj_list[v]:
            adj_list[v].remove(vi)
        
    del adj_list[vi]
    return print(adj_list)