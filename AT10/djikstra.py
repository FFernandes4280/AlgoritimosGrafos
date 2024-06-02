import numpy as np

def dijkstra(matriz, vOrigem, vDestino):
    n,y = np.shape(matriz)
    infinito = float('inf')
    custo = [infinito] * n
    custo[vOrigem] = 0
    rota = [-1] * n

    F = set()
    A = set(range(n))
    N = set()

    while A:
        v = min(A, key=lambda u: custo[u])
        
        if v == vDestino:
            break
        
        A.remove(v)
        F.add(v)

        for u in range(n):
            
            if u in A and matriz[v][u] != -1:
                wvu = matriz[v][u]
                novaDistancia = custo[v] + wvu
                
                if novaDistancia < custo[u]:
                    custo[u] = novaDistancia
                    rota[u] = v
                    N.add(u)

        A.update(N)
        N.clear()


    caminho = []
    vertice = vDestino
    
    while vertice != -1:
        caminho.insert(0, vertice)
        vertice = rota[vertice]

    print (caminho, custo[vDestino])