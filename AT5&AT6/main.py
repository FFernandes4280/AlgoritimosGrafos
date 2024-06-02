import dfs as dfs
import numpy as np

adj_list ={0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}
           


dfs.dfs(adj_list, 0)
