import functions as fc
import numpy as np

matrix = ([[0, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]])
print(np.array(matrix))
print()
fc.euleriano(matrix)