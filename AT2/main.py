'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
ALGORITMOS EM GRAFOS
Filipe Castro Fernandes 2022002088
Atividade 01 -> 29/03/2023
===================================================='''

from igraph import *
import numpy as np
import functions as fc

inst = 'ponte.txt' #seleciona o nome da instancia desejada
matrix = np.loadtxt(inst) #copia os dados do .txt para a matriz numpy
res = fc.calcDensidade(matrix)


    

