import func as f

adj_list = {0: [1, 4], 1: [0, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}
pos = 0

f.verificaDAG(adj_list)