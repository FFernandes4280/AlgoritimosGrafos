def classificaAresta():
    return 0

def verificaDAG(adj_list):
    q = [] #lista de VERTICES
    v = [] #lista de VERTICES visitados
    c = [] #lista que verifica ciclos
    q.append(0) #adciona o primeiro vertice na lista q
    while q:
        vertice = q.pop() #tira o ultimo elemento de q
        if vertice not in v: 
            v.append(vertice) #marca ele como visitado o colocando em v
            c.append(vertice)
            for adj_idx in adj_list[vertice]: #ve os vertices adjacentes 
                if adj_idx in c:
                    return print("NÃO DAG")
                if adj_idx not in v: #se ele já não tiver sido visitado é adcionado a fila
                    c = []
                    q.append(adj_idx)
        
    return print("DAG")

            
