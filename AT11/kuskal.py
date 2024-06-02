import math

def prim(matriz):
    numVertices = len(matriz)
    custoTotal = 0
    vertice = 0
    verSelec = []
    verNaoSelec = [i for i in range(1, numVertices)]
    arestasAGM = []

    verSelec.append(vertice)

    while len(arestasAGM) < numVertices - 1:
        custo = math.inf

        for u in verSelec:
            for v in verNaoSelec:
                if matriz[u][v] != 0 and matriz[u][v] < custo:
                    custo = matriz[u][v]
                    aresta = (u, v)

        verSelec.append(aresta[1])
        verNaoSelec.remove(aresta[1])
        arestasAGM.append(aresta)
        custoTotal += custo

    return arestasAGM, custoTotal

def kruskal(matriz):
    numVertices = len(matriz)
    custoTotal = 0
    listaArestas = []
    arestasAGM = []

    for i in range(numVertices):
        for j in range(i + 1, numVertices):
            if matriz[i][j] != 0:
                listaArestas.append((i, j, matriz[i][j]))

    listaArestas = sorted(listaArestas, key=lambda x: x[2])

    pai = [-1] * numVertices

    for aresta in listaArestas:
        raiz1 = find(pai, aresta[0])
        raiz2 = find(pai, aresta[1])

        if raiz1 != raiz2:
            arestasAGM.append((aresta[0], aresta[1]))
            union(pai, raiz1, raiz2)
            custoTotal += aresta[2]

    return print(arestasAGM, custoTotal)

def find(pai, vertice):
    if pai[vertice] == -1:
        return vertice
    return find(pai, pai[vertice])

def union(pai, raiz1, raiz2):
    pai[raiz2] = raiz1