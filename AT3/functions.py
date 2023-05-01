
def verificaAdjacenciaLista(adj_list, vi , vj):
    if vi in adj_list[vj] or vj in adj_list[vi]:
        print(True)
        return True
    else:
        print(False)
        return False