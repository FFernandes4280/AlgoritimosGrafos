import numpy as np

def warshall(matrix):
    n = np.shape(matrix)[0]
    aux = np.array(matrix)

    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if aux[i][j] == 1 or (aux[i][k] == 1 and aux[k][j] == 1):
                    aux[i][j] = 1
                else:
                    aux[i][j] = aux[i][j]

    
    print(aux)
    return aux

def euleriano(matrix):
    n = np.shape(matrix)[0]
    impar = 0
    i = 0

    while (i < n):
       grau = np.sum(matrix[i])
       i += 1
       if grau%2 != 0:
           impar += 1

         
    if impar > 2:
        print(False)
        return False
    else:
        print(True)
        return True

