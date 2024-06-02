import numpy as np
#Como cria uma condição pra aplicar na bfs para que atue em todos os vértices existentes
def bfs(adj_list, pos):
    q = [] #lista de VERTICES
    v = [] #lista de VERTICES visitados
    q.append(pos) #adciona o primeiro vertice na lista q
    while q:
        vertice = q.pop(0) #tira o primeiro elemento de q
        if vertice not in v: 
            v.append(vertice) #marca ele como visitado o colocando em v
            for adj_idx in adj_list[vertice]: #ve os vertices adjacentes 
                if adj_idx not in v: #se ele já não tiver sido visitado é adcionado a fila
                    q.append(adj_idx)

    if set(adj_list.keys()) == set(v): #se a lista de visitados é igual a lista de existentes acaba
        print(v)
        return print(v)
    else:
        for chaves in adj_list:
            if chaves not in v:
                v.append(chaves)
        return print(v)
    



            


