def color(adj_list,pos):
    q = [] #lista de vertices
    v = [] #lista de visitados
    q.append(pos)
    i = 1
    while q:
        vertice = q.pop(0) #tira o primeiro elemento de q 
        v.append(vertice, 1) #marca com uma cor
        for adj_idx in adj_list[vertice]: #ve os vertices adjacentes 
            if adj_idx in v: 
                i = i + 1
                v[adj_idx] = (v[adj_idx][0], i)
            else:
                q.append(adj_idx)

        if set(adj_list.keys()) == set(v): #se a lista de visitados é igual a lista de existentes acaba
            print(v)
            return print(v)
        else:
            for chaves in adj_list:
                if chaves not in v:
                    q.append(chaves)
