import numpy as np
'''''''''
def dfs(adj_list, pos): #Interativo
    p = [] #pilha de VERTICES
    v = [] #lista de VERTICES visitados
    p.append(pos) #adciona a posição inicial a lista
    while p:
        vertice = p.pop() #remove o ultimo elemento da pilha
        if vertice not in v: #somente se não tiver sido visitado
            v.append(vertice) #é visitado
            for atual in reversed(adj_list[vertice]):
                if atual not in v:
                    p.append(atual) #adiciona a pilha
        if set(adj_list.keys()) != set(v) and not p: #ve se todos os vertices já 
            dif = set(adj_list.keys()) - set(v)                                     
            p.append(min(dif)) #adciona o menor vertices da lista de valores                                        
                               #que nao foram visitados a pilha
    return print(v)
'''''''''
def dfs(lista_adj, pos):
    v=[]
    for pos in lista_adj.keys():
        if pos not in v:
            v += busca(lista_adj, pos, [])
    return print(v)
    
def busca(lista_adj, pos, v):
    v.append(pos)
    for vizinho in lista_adj[pos]: 
        if vizinho not in v:
            busca(lista_adj, vizinho, v)
    return v
  

                

