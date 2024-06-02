import numpy as np

def dijkstra(adj_list, vOrigem, vDestino):
    n = len(adj_list)
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

        for u, wvu in adj_list[v]:
            if u in A:
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

    return caminho

 
adj_list = {
    0: [(1, 3)],
    1: [(0, 3), (2, 5)],
    2: [(1, 5), (3, 11), (9, 1)],
    3: [(2, 11), (4, 8), (11, 2)],
    4: [(3, 8), (5, 5), (10,2)],
    5: [(4, 5), (6, 3)],
    6: [(5, 3), (7, 3)],
    7: [(6, 3), (8, 2)],
    8: [(7, 2)],
    9: [(2, 1), (10, 11)],
    10: [(9, 11), (14, 2), (17, 8)],
    11: [(10, 2), (12, 2)],
    12: [(11, 2), (13, 1)],
    13: [(12, 1)],
    14: [(10, 2), (15, 2)],
    15: [(14, 2), (16, 1)],
    16: [(15, 1)],
    17: [(10, 8), (18, 5)],
    18: [(17, 5), (19, 7)],
    19: [(18, 7), (20, 3)],
    20: [(19, 3), (21, 9)],
    21: [(20, 9), (22, 4)],
    22: [(21, 4), (23, 2), (26, 4)],
    23: [(22, 2), (24, 2)],
    24: [(23, 2), (25, 1)],
    25: [(24, 1)],
    26: [(22, 4), (27, 7)],
    27: [(26, 7), (28, 11)],
    28: [(27, 11), (29, 6)],
    29: [(28, 6), (30, 4)],
    30: [(29, 4), (31, 4)],
    31: [(30, 4), (32, 18)],
    32: [(31, 18), (33, 10)],
    33: [(32, 10), (34, 2)],
    34: [(33, 2), (35, 7)],
    35: [(34, 7), (36, 12)],
    36: [(35, 12), (37, 4), (45, 7)],
    37: [(36, 4), (38, 10), (54, 14)],
    38: [(37, 10), (39, 9)],
    39: [(38, 9), (40, 5)],
    40: [(39, 5), (41, 8)],
    41: [(40, 8), (42, 2)],
    42: [(41, 2), (43, 2)],
    43: [(42, 2)],
    45: [(36, 7), (46, 2), (49, 8)],
    46: [(45, 2), (47, 2)],
    47: [(46, 2), (48, 1)],
    48: [(47, 1)],
    49: [(45, 8), (50, 6)],
    50: [(49, 6), (51, 2)],
    51: [(50, 2), (52, 2)],
    52: [(51, 2)],
    54: [(37, 14), (55, 2)],
    55: [(54, 2), (0, 14)]
}

vertice_inicio = 12
vertice_final = 52

caminho_minimo= dijkstra(adj_list, vertice_inicio, vertice_final)
if caminho_minimo:
    print(f"Percorra o caminho: {caminho_minimo}")
else:
    print("Não foi encontrado um caminho.")

