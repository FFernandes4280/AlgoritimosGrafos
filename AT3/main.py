import numpy as np
import functions as fc

adj_list ={0: [2, 2, 3], 1: [3], 2: [0, 0, 3], 3: [0, 1, 2]}
a = 0
b = 1
fc.verificaAdjacenciaLista(adj_list, a, b)